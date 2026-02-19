"""
Systems package untuk HRMS.
Berisi sistem-sistem utama untuk mengelola HR operations.
"""

from systems.payroll_system import PayrollSystem
from systems.hr_system import HRManagementSystem

__all__ = [
    'PayrollSystem',
    'HRManagementSystem'
]
