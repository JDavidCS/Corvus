#!/usr/bin/python3 

'''Employee Class Definition'''

from models.basemodel import BaseModel, Base
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship


class Employee(BaseModel, Base):
    '''
Employee class.


        Atributes:
            id - emloyee identification
            names - emloyee names
            forename - emloyee forenames
            job - emloyee job
            worked_hours - hours in all the month
            bonus - payment considerations
'''

    __tablename__ = 'employes'
    id = Column(Integer, primary_key=True)
    names = Column(String(80), nullable=False)
    forenames = Column(String(80), nullable=False)
    position = Column(Integer, ForeignKey('positions.id'))
    worked_hours = Column(Integer, default=0)
    bonus = relationship('Bonus', back_populates='employee', uselist=False)
