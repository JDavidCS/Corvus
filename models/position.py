#!/usr/bin/python3 

'''Position Class Definition'''

from models.basemodel import BaseModel, Base
from sqlalchemy import Column, String, Integer, ForeignKey, Float
from sqlalchemy.orm import relationship


class Position(BaseModel, Base):
    '''
Position class.


        Atributes:
            id - Bonus id
            type - type/name of the bonus
            description - bonus description
            value - value to add to the user payment
'''

    __tablename__ = 'positions'
    id = Column(Integer, primary_key=True)
    type = Column(String(80), nullable=False)
    description = Column(String(250))
    value = Column(Float, nullable=False)
    employee_id = relationship('Employee')
