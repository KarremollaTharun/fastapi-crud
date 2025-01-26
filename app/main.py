from fastapi import FastAPI
from fastapi.params import Body
import psycopg2
from typing import Optional,List
from psycopg2.extras import RealDictCursor
from sqlalchemy.orm import Session
from . import models,schemas,utils
from .database import engine,SessionLocal,get_db
from .router import user



models.Base.metadata.create_all(bind=engine)


app = FastAPI()
    
while True:
    try:
        conn = psycopg2.connect(host= 'localhost',database='****',user='****',
                                password='****',cursor_factory=RealDictCursor)
        cursor = conn.cursor()
        print("database connection successful")
        break
    except Exception as e:
        print('connection fail print')
        print('error',e)
        time.sleep(2)

    
app.include_router(user.router)

@app.get('/')
async def root():
    return {'message' : 'Welcome to API!!!'}



    


