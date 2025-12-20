from sqlalchemy import Column, Integer, String
from .database import Base

class User(Base):
    __tablename__ = "user_info"
    #id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    phone_number = Column(String)
