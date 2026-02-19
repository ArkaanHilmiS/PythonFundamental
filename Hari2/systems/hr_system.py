"""
HR Management System - Sistem utama untuk mengelola HR operations.
"""

from datetime import datetime
from systems.payroll_system import PayrollSystem
from models.employee import Employee
from models.full_time_employee import FullTimeEmployee
from models.contract_employee import ContractEmployee
from models.intern import Intern


class HRManagementSystem:
    """Main HR Management System."""
    
    def __init__(self, company_name):
        self.company_name = company_name
        self.employees = {}  # emp_id -> Employee object
        self.departments = {}  # dept_id -> Department object
        self.payroll_system = PayrollSystem()
        self.created_at = datetime.now()
    
    def add_employee(self, employee):
        """Add employee to system."""
        if employee.emp_id in self.employees:
            return f"❌ Employee ID {employee.emp_id} already exists"
        
        self.employees[employee.emp_id] = employee
        return f"✓ Employee {employee.name} added to system"
    
    def get_employee(self, emp_id):
        """Get employee by ID."""
        return self.employees.get(emp_id)
    
    def remove_employee(self, emp_id):
        """Remove employee from system."""
        if emp_id in self.employees:
            emp = self.employees[emp_id]
            emp.status = "Terminated"
            del self.employees[emp_id]
            Employee.total_employees -= 1
            return f"✓ Employee {emp.name} removed from system"
        return f"❌ Employee ID {emp_id} not found"
    
    def add_department(self, department):
        """Add department to system."""
        if department.dept_id in self.departments:
            return f"❌ Department ID {department.dept_id} already exists"
        
        self.departments[department.dept_id] = department
        return f"✓ Department {department.name} added to system"
    
    def get_department(self, dept_id):
        """Get department by ID."""
        return self.departments.get(dept_id)
    
    def get_all_employees(self):
        """Get all employees."""
        return list(self.employees.values())
    
    def get_employees_by_department(self, department_name):
        """Get all employees in a department."""
        return [emp for emp in self.employees.values() 
                if emp.department == department_name]
    
    def get_employees_by_position(self, position):
        """Get all employees with specific position."""
        return [emp for emp in self.employees.values() 
                if emp.position == position]
    
    def generate_company_report(self):
        """Generate comprehensive company report."""
        total_payroll = sum(
            emp.calculate_salary().get("net_salary", 0) 
            for emp in self.employees.values()
        )
        
        # Group by employee type
        full_time = sum(1 for emp in self.employees.values() if isinstance(emp, FullTimeEmployee))
        contract = sum(1 for emp in self.employees.values() if isinstance(emp, ContractEmployee))
        interns = sum(1 for emp in self.employees.values() if isinstance(emp, Intern))
        
        report = f"""
{'='*70}
{self.company_name.upper()} - COMPANY REPORT
{'='*70}
Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

OVERVIEW:
- Total Employees: {len(self.employees)}
  • Full-time: {full_time}
  • Contract: {contract}
  • Interns: {interns}
- Total Departments: {len(self.departments)}
- Total Monthly Payroll: Rp {total_payroll:,.0f}

DEPARTMENTS:
"""
        for dept in self.departments.values():
            report += f"- {dept.name}: {len(dept)} employees (Payroll: Rp {dept.get_total_payroll():,.0f})\n"
        
        report += "\n" + "="*70
        return report
    
    def get_leave_requests_pending(self):
        """Get all pending leave requests."""
        pending = []
        for emp in self.employees.values():
            for leave in emp.leave_history:
                if leave["status"] == "pending":
                    pending.append({
                        "employee": emp.name,
                        "emp_id": emp.emp_id,
                        "leave": leave
                    })
        return pending
