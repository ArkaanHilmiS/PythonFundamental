"""
========================================================================
PAYROLL API - Services
Business Logic Layer
========================================================================
"""

from typing import List, Dict, Optional
from datetime import datetime
from app.repositories import IEmployeeRepository


# ========================================================================
# PAYROLL SERVICE
# ========================================================================

class PayrollService:
    """Service untuk payroll calculation."""
    
    # Business rules / Tax rates
    TAX_RATE = 0.05  # PPh 21: 5%
    PENSION_RATE = 0.02  # Pension: 2%
    HEALTH_INSURANCE = 500000  # Fixed: Rp 500,000
    
    def __init__(self, repository: IEmployeeRepository):
        self.repository = repository
    
    def calculate_payroll(self) -> Dict:
        """
        Calculate payroll untuk semua karyawan.
        
        Returns:
            Dictionary dengan employees dan summary
        """
        employees = self.repository.load()
        
        if not employees:
            return {
                "employees": [],
                "summary": {
                    "total_employees": 0,
                    "total_gross": 0,
                    "total_deductions": 0,
                    "total_net": 0,
                    "average_net": 0
                }
            }
        
        processed_employees = []
        
        for emp in employees:
            gross_salary = float(emp.get('gaji', 0))
            
            # Calculate deductions
            tax = gross_salary * self.TAX_RATE
            pension = gross_salary * self.PENSION_RATE
            health = self.HEALTH_INSURANCE
            
            total_deductions = tax + pension + health
            net_salary = gross_salary - total_deductions
            
            processed_emp = {
                "id": emp.get('id'),
                "nama": emp.get('nama'),
                "departemen": emp.get('departemen'),
                "gross_salary": gross_salary,
                "tax": tax,
                "pension": pension,
                "health_insurance": health,
                "total_deductions": total_deductions,
                "net_salary": net_salary,
                "processed_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }
            
            processed_employees.append(processed_emp)
            
            # Update employee data dengan calculated fields
            emp.update({
                "gross_salary": gross_salary,
                "tax": tax,
                "pension": pension,
                "health_insurance": health,
                "total_deductions": total_deductions,
                "net_salary": net_salary,
                "processed_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            })
        
        # Save updated data
        self.repository.save(employees)
        
        # Calculate summary
        total_gross = sum(emp["gross_salary"] for emp in processed_employees)
        total_deductions = sum(emp["total_deductions"] for emp in processed_employees)
        total_net = sum(emp["net_salary"] for emp in processed_employees)
        
        summary = {
            "total_employees": len(processed_employees),
            "total_gross": total_gross,
            "total_deductions": total_deductions,
            "total_net": total_net,
            "average_net": total_net / len(processed_employees) if processed_employees else 0
        }
        
        return {
            "employees": processed_employees,
            "summary": summary
        }
    
    def get_department_payroll(self, departemen: str) -> Dict:
        """Get payroll untuk specific department."""
        employees = self.repository.load()
        dept_employees = [emp for emp in employees 
                         if emp.get('departemen') == departemen]
        
        if not dept_employees:
            return {
                "departemen": departemen,
                "total_employees": 0,
                "total_payroll": 0,
                "employees": []
            }
        
        total_payroll = sum(float(emp.get('net_salary', emp.get('gaji', 0))) 
                           for emp in dept_employees)
        
        return {
            "departemen": departemen,
            "total_employees": len(dept_employees),
            "total_payroll": total_payroll,
            "employees": [emp['nama'] for emp in dept_employees]
        }


# ========================================================================
# EMPLOYEE SERVICE
# ========================================================================

class EmployeeService:
    """Service untuk employee management."""
    
    def __init__(self, repository: IEmployeeRepository):
        self.repository = repository
    
    def get_all_employees(self) -> List[Dict]:
        """Get all employees."""
        return self.repository.load()
    
    def get_employee_by_id(self, emp_id: str) -> Optional[Dict]:
        """Get employee by ID."""
        return self.repository.get_by_id(emp_id)
    
    def create_employee(self, employee_data: Dict) -> Dict:
        """Create new employee with validation."""
        # Business validation di sini dilakukan oleh Pydantic schemas
        # Tapi kita bisa add additional business rules if needed
        
        # Add timestamp
        employee_data['created_at'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # Add to repository
        self.repository.add(employee_data)
        
        return employee_data
    
    def update_employee(self, emp_id: str, updated_data: Dict) -> Optional[Dict]:
        """Update employee data."""
        employee = self.repository.get_by_id(emp_id)
        
        if not employee:
            return None
        
        # Update fields
        employee.update(updated_data)
        employee['updated_at'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # Save
        employees = self.repository.load()
        employees = [employee if emp.get('id') == emp_id else emp 
                    for emp in employees]
        self.repository.save(employees)
        
        return employee
    
    def delete_employee(self, emp_id: str) -> bool:
        """Delete employee."""
        return self.repository.delete(emp_id)
    
    def search_employees(self, **criteria) -> List[Dict]:
        """Search employees by criteria."""
        employees = self.repository.load()
        
        if not criteria:
            return employees
        
        results = []
        for emp in employees:
            match = True
            for key, value in criteria.items():
                if key not in emp or str(emp[key]).lower() != str(value).lower():
                    match = False
                    break
            
            if match:
                results.append(emp)
        
        return results
    
    def get_statistics(self) -> Dict:
        """Get employee statistics."""
        employees = self.repository.load()
        
        if not employees:
            return {
                "total_employees": 0,
                "departments": [],
                "average_salary": 0,
                "min_salary": 0,
                "max_salary": 0,
                "salary_range": 0
            }
        
        salaries = [float(emp.get('gaji', 0)) for emp in employees]
        departments = list(set(emp.get('departemen') for emp in employees))
        
        return {
            "total_employees": len(employees),
            "departments": departments,
            "average_salary": sum(salaries) / len(salaries),
            "min_salary": min(salaries),
            "max_salary": max(salaries),
            "salary_range": max(salaries) - min(salaries)
        }


# Make Optional available
from typing import Optional
