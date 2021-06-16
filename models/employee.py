#!/usr/bin/python3 

'''Employee Class Definition'''

from models.basemodel import BaseModel, Base
from sqlalchemy import Column, String, Integer, ForeignKey, Float, Boolean
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
    id = Column(String(32), primary_key=True)
    company = Column(ForeignKey('company.id'), nullable=False)
    names = Column(String(80), nullable=False)
    forenames = Column(String(80), nullable=False)
    position = Column(String(80), nullable=False)
    c_type = Column(String(80), nullable=False)
    item = relationship('Item', back_populates='employee')
    risk = Column(String(1), default=1)
    arl_payment = Column(Boolean, default=False)
    base_salary = Column(Float, default=908526)
    worked_hours = Column(Integer, default=0)
    month_payment = Column(Boolean, default=False)
    bonus = relationship('Bonus', back_populates='employee')

    def arl(self):
        if self.c_type == 'Termino Indefinido':
            risks = {'1': 0.00522, '2': 0.01044, '3': 0.02436, '4': 0.0435, '5': 0.0696}
            return risks[self.risk] * self.base_salary
        return 0

    def health(self):
        if self.c_type == 'Termino Indefinido':
            return self.base_salary * 0.125
        return 0

    def pension(self):
        if self.c_type == 'Termino Indefinido':
            return self.base_salary * 0.16
        return 0

    def para_f(self):
        if self.c_type == 'Termino Indefinido':
            return self.base_salary * 0.02
        return 0

    def salary(self):
        salary = 0
        if self.c_type == 'Obra Labor':
            self.base_salary = 0
            for item in self.item:
                salary = item.unitary_value * item.finished
        elif self.c_type == 'Termino Indefinido':
            for bonus in self.bonus:
                salary += bonus.value
        return self.base_salary + salary

    def sub_trans(self):
        if self.base_salary < 908.526 * 2:
            return 106454
        return 0
