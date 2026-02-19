"""
Models package untuk HRMS.
Berisi semua class models yang digunakan dalam sistem.
"""

from models.person import Person
from models.employee import Employee
from models.full_time_employee import FullTimeEmployee
from models.contract_employee import ContractEmployee
from models.intern import Intern
from models.department import Department

__all__ = [
    'Person',
    'Employee',
    'FullTimeEmployee',
    'ContractEmployee',
    'Intern',
    'Department'
]
