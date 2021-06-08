#!/usr/bin/python3 

'''Employee Class Definition'''

from models.basemodel import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import uuid


class Company(BaseModel, Base):
    '''
'''

    __tablename__ = 'company'
    id = Column(String(80), default=uuid.uuid4(), primary_key=True)
    name = Column(String(50), nullable=False)
    admin_users = relationship('Admin')
    employees = relationship('Employee')
