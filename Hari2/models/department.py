"""
Department Model - Manajemen departemen perusahaan.
"""

from datetime import datetime


class Department:
    """Department class untuk mengelola departemen."""
    
    def __init__(self, dept_id, name, manager_id=None):
        self.dept_id = dept_id
        self.name = name
        self.manager_id = manager_id
        self.employees = []
        self.budget = 0
        self.created_at = datetime.now()
    
    def add_employee(self, employee):
        """Add employee to department."""
        if employee not in self.employees:
            self.employees.append(employee)
            employee.department = self.name
            return f"✓ {employee.name} added to {self.name}"
        return f"❌ {employee.name} already in {self.name}"
    
    def remove_employee(self, employee):
        """Remove employee from department."""
        if employee in self.employees:
            self.employees.remove(employee)
            return f"✓ {employee.name} removed from {self.name}"
        return f"❌ {employee.name} not in {self.name}"
    
    def get_headcount(self):
        """Get total number of employees."""
        return len(self.employees)
    
    def get_total_payroll(self):
        """Calculate total department payroll."""
        total = 0
        for emp in self.employees:
            salary_info = emp.calculate_salary()
            total += salary_info.get("net_salary", 0)
        return total
    
    def get_department_summary(self):
        """Get department summary."""
        summary = f"""
{'='*70}
DEPARTMENT: {self.name.upper()}
{'='*70}
Department ID: {self.dept_id}
Manager ID: {self.manager_id or "Not Assigned"}
Total Employees: {self.get_headcount()}
Monthly Payroll: Rp {self.get_total_payroll():,.0f}
Budget: Rp {self.budget:,}

EMPLOYEES:
"""
        for i, emp in enumerate(self.employees, 1):
            years, months = emp.calculate_tenure()
            summary += f"{i}. {emp.name:<25} - {emp.position:<20} ({years}y {months}m)\n"
        
        summary += "=" * 70
        return summary
    
    def __len__(self):
        """Return headcount when len() is called."""
        return len(self.employees)
    
    def __str__(self):
        return f"Department({self.name}) - {len(self.employees)} employees"
