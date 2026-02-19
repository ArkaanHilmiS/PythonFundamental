"""
Contract Employee Model - Karyawan kontrak dengan durasi tertentu.
"""

from datetime import datetime
from models.employee import Employee


class ContractEmployee(Employee):
    """Contract employee dengan durasi kontrak tertentu."""
    
    def __init__(self, emp_id, name, email, phone, date_of_birth,
                 join_date, department, base_salary, position, 
                 contract_end_date, hourly_rate=None):
        super().__init__(emp_id, name, email, phone, date_of_birth,
                        join_date, department, base_salary, position)
        
        self.contract_end_date = contract_end_date
        self.hourly_rate = hourly_rate
        self.hours_worked_this_month = 0
        self.health_insurance = False
        
        # Override leave balance (less for contract)
        self.annual_leave_balance = 6
        self.sick_leave_balance = 6
    
    def calculate_salary(self):
        """Calculate contract employee salary."""
        if self.hourly_rate:
            # Hourly based
            base = self.hourly_rate * self.hours_worked_this_month
        else:
            # Monthly fixed
            base = self.base_salary
        
        return {
            "base_salary": base,
            "hours_worked": self.hours_worked_this_month if self.hourly_rate else "N/A",
            "gross_salary": base,
            "net_salary": base
        }
    
    def is_contract_ending_soon(self, days=30):
        """Check if contract ending within specified days."""
        end_date = datetime.strptime(self.contract_end_date, "%Y-%m-%d")
        days_remaining = (end_date - datetime.now()).days
        return days_remaining <= days, days_remaining
    
    def extend_contract(self, new_end_date):
        """Extend contract."""
        old_end = self.contract_end_date
        self.contract_end_date = new_end_date
        return f"✓ Contract extended from {old_end} to {new_end_date}"
