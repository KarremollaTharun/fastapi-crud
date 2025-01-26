from pydantic import BaseModel,EmailStr


class UserBase(BaseModel):
    name : str 
    email : EmailStr
    password : str

class User(UserBase):
    class config:
        orm_mode = True

class UserDetails(BaseModel):
    id : int
    name : str 
    email : EmailStr

    class config:
        orm_mode = True


