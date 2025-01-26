from fastapi import FastAPI,HTTPException,status,Response,APIRouter,Depends
from .. import models,schemas,utils
from ..database import get_db
from sqlalchemy.orm import Session

router = APIRouter(
    prefix = '/users'
)

@router.post('/',status_code = status.HTTP_201_CREATED,response_model = schemas.UserDetails)
def create_posts(user :schemas.User,db: Session = Depends(get_db)):
    
    hash_password = utils.hash(user.password)
    user.password = hash_password
     
    new_user = models.User(**user.dict())    

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return  new_user
    
    
@router.get('/',response_model = list[schemas.UserDetails] )
def get_users(db: Session = Depends(get_db)):
    details = db.query(models.User).all()
    return details


@router.get('/{id}',response_model = schemas.UserDetails)
def get_users(id: int,db: Session = Depends(get_db)):

    details = db.query(models.User).filter(models.User.id == id).first()
    
    if not details:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,detail = f'User details with id = {id} not found')

    return  details
 

@router.delete('/{id}',status_code = status.HTTP_204_NO_CONTENT)
def delete_user(id : int,db: Session = Depends(get_db)):

    details = db.query(models.User).filter(models.User.id == id)
    if details.first() is None:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,detail = f'User details with id : {id} doesn\'t exist')
    
    details.delete(synchronize_session = False)
    db.commit()
    
    return Response(status_code = status.HTTP_204_NO_CONTENT)



@router.put('/{id}',response_model = schemas.UserDetails)
def update_user(id :int,user : schemas.User,db: Session = Depends(get_db)):

    details_query = db.query(models.User).filter(models.User.id == id)
    user_details = details_query.first()

    if  user_details == None:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,detail = f'User details with id : {id} not found')
    details_query.update(user.dict(),synchronize_session = False)

    db.commit()
    return  details_query.first()