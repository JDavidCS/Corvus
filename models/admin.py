#!/usr/bin/python3 

'''Employee Class Definition'''

from models.basemodel import BaseModel, Base
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
import uuid


class Admin(BaseModel, Base):
    '''
'''

    __tablename__ = 'admin_users'
    id = Column(String(80), default=uuid.uuid4(), primary_key=True)
    name = Column(String(50), nullable=False)
    password = Column(String(50), nullable=False)
    company = Column(ForeignKey('company.id'), nullable=False)
