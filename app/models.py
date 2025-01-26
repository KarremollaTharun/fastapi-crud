from .database import Base
from sqlalchemy.sql.expression import text 
from sqlalchemy import Column,Integer,String,Boolean
from sqlalchemy.sql.sqltypes import TIMESTAMP

class User(Base):
    __tablename__ = 'user_details'

    id = Column(Integer,primary_key = True, nullable = False)
    name = Column(String,nullable = False)
    email = Column(String,nullable = False,unique = True)
    password = Column(String,nullable = False)
    