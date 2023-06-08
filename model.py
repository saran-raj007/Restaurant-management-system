from sqlalchemy.schema import Column
from sqlalchemy.types import String,Integer,Date,BLOB,BigInteger,DATETIME,ARRAY
from database import base,db_engine

class menu(base):

    __tablename__="MENU"

    id =Column(Integer,primary_key=True,index=True)
    Deshies_name=Column(String(30))
    Deshies_cost=Column(Integer)
    status=Column(String(30))
    
class Admin(base):
      
      __tablename__="admi"
      id =Column(Integer,primary_key=True,index=True)
      ad_id =Column(Integer)
      username=Column(String(30))
      password=Column(String(30))
      status=Column(String(30))

class employee(base):
     
    __tablename__="emp"

    id =Column(Integer,primary_key=True,index=True)
    username=Column(String(30))
    password=Column(String(30))
    status=Column(String(30))

class sales(base):
     
    __tablename__="Sales"

    id =Column(Integer,primary_key=True,index=True)
    cous_name=Column(String(30))
    cous_pno=Column(String(30))
    Deshies_name=Column(String(330))
    Deshies_quantity=Column(String(230))
    Total_cost=Column(Integer)
    status=Column(String(30))

base.metadata.create_all(bind=db_engine)

    