"""
Intern Model - Karyawan magang dengan program pembelajaran.
"""

from datetime import datetime
from models.employee import Employee


class Intern(Employee):
    """Intern dengan program magang tertentu."""
    
    def __init__(self, emp_id, name, email, phone, date_of_birth,
                 join_date, department, base_salary, position,
                 university, mentor_id, internship_duration_months):
        super().__init__(emp_id, name, email, phone, date_of_birth,
                        join_date, department, base_salary, position)
        
        self.university = university
        self.mentor_id = mentor_id
        self.internship_duration_months = internship_duration_months
        self.learning_modules_completed = []
        self.projects = []
        
        # Interns don't get paid leave
        self.annual_leave_balance = 0
        self.sick_leave_balance = 3
    
    def calculate_salary(self):
        """Calculate intern salary (fixed stipend)."""
        return {
            "stipend": self.base_salary,
            "gross_salary": self.base_salary,
            "net_salary": self.base_salary
        }
    
    def complete_module(self, module_name):
        """Complete learning module."""
        self.learning_modules_completed.append({
            "module": module_name,
            "completed_at": datetime.now().strftime("%Y-%m-%d")
        })
        return f"✓ Module completed: {module_name}"
    
    def add_project(self, project_name, description):
        """Add project to intern portfolio."""
        self.projects.append({
            "project": project_name,
            "description": description,
            "added_at": datetime.now().strftime("%Y-%m-%d")
        })
        return f"✓ Project added: {project_name}"
