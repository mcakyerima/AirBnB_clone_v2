#!/usr/bin/python3
'''
This is the Implementation of the User class which inherits from BaseModel
and Base class of sqlAlchemy
'''
from os import getenv
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base


class User(BaseModel, Base):
    '''
    Definition of the User class
    '''
    __tablename__ = "users"
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=True)
    last_name = Column(String(128), nullable=True)
