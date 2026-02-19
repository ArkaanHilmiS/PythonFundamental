"""
HRMS - Main Program
Demo program untuk Human Resource Management System.
"""

from datetime import datetime
from models import (
    FullTimeEmployee, 
    ContractEmployee, 
    Intern, 
    Department
)
from systems import HRManagementSystem


def main():
    """Main program to demonstrate HRMS."""
    
    print("="*70)
    print("HUMAN RESOURCE MANAGEMENT SYSTEM (HRMS)")
    print("Modular Version - Separated by Classes and Features")
    print("="*70)
    print("\nInitializing system...\n")
    
    # Create HR System
    hrms = HRManagementSystem("TechCorp Solutions")
    
    # Create Departments
    print("--- CREATING DEPARTMENTS ---")
    dept_it = Department("DEPT001", "Information Technology")
    dept_it.budget = 500000000
    print(hrms.add_department(dept_it))
    
    dept_hr = Department("DEPT002", "Human Resources")
    dept_hr.budget = 200000000
    print(hrms.add_department(dept_hr))
    
    dept_finance = Department("DEPT003", "Finance")
    dept_finance.budget = 300000000
    print(hrms.add_department(dept_finance))
    
    # Create Employees
    print("\n--- CREATING EMPLOYEES ---")
    
    # Full-time employees
    emp1 = FullTimeEmployee(
        emp_id="EMP001",
        name="Tomas Anderson",
        email="tomas@techcorp.com",
        phone="081234567890",
        date_of_birth="1990-05-15",
        join_date="2020-01-15",
        department="Information Technology",
        base_salary=15000000,
        position="Senior Software Engineer",
        grade="Senior"
    )
    print(hrms.add_employee(emp1))
    dept_it.add_employee(emp1)
    
    emp2 = FullTimeEmployee(
        emp_id="EMP002",
        name="Sarah Connor",
        email="sarah@techcorp.com",
        phone="081234567891",
        date_of_birth="1988-08-20",
        join_date="2019-03-01",
        department="Information Technology",
        base_salary=20000000,
        position="Tech Lead",
        grade="Lead"
    )
    print(hrms.add_employee(emp2))
    dept_it.add_employee(emp2)
    
    emp3 = FullTimeEmployee(
        emp_id="EMP003",
        name="David Miller",
        email="david@techcorp.com",
        phone="081234567892",
        date_of_birth="1992-03-10",
        join_date="2021-06-01",
        department="Finance",
        base_salary=12000000,
        position="Financial Analyst",
        grade="Mid"
    )
    print(hrms.add_employee(emp3))
    dept_finance.add_employee(emp3)
    
    # Contract employee
    emp4 = ContractEmployee(
        emp_id="EMP004",
        name="Lisa Wong",
        email="lisa@techcorp.com",
        phone="081234567893",
        date_of_birth="1993-11-25",
        join_date="2024-01-01",
        department="Information Technology",
        base_salary=10000000,
        position="Frontend Developer",
        contract_end_date="2024-12-31"
    )
    print(hrms.add_employee(emp4))
    dept_it.add_employee(emp4)
    
    # Intern
    emp5 = Intern(
        emp_id="INT001",
        name="Mike Ross",
        email="mike@techcorp.com",
        phone="081234567894",
        date_of_birth="2000-07-10",
        join_date="2024-02-01",
        department="Information Technology",
        base_salary=4000000,
        position="Software Engineering Intern",
        university="MIT",
        mentor_id="EMP001",
        internship_duration_months=6
    )
    print(hrms.add_employee(emp5))
    dept_it.add_employee(emp5)
    
    # Add Performance Ratings
    print("\n--- ADDING PERFORMANCE RATINGS ---")
    print(emp1.add_performance_rating(4.5, "2023-12-31", "Sarah Connor", "Excellent work"))
    print(emp1.add_performance_rating(4.7, "2024-06-30", "Sarah Connor", "Outstanding"))
    print(emp2.add_performance_rating(4.8, "2023-12-31", "CTO", "Great leadership"))
    
    # Simulate Attendance
    print("\n--- SIMULATING ATTENDANCE (February 2024) ---")
    for day in range(1, 21):
        date = datetime(2024, 2, day, 9, 0, 0)
        emp1.clock_in(date)
        emp1.clock_out(date.replace(hour=18, minute=0))
        
        emp2.clock_in(date)
        emp2.clock_out(date.replace(hour=19, minute=0))
    
    print(f"✓ Attendance recorded for 20 days")
    
    # Leave Requests
    print("\n--- LEAVE REQUESTS ---")
    print(emp1.request_leave("annual", "2024-03-15", "2024-03-20", "Family vacation"))
    print(emp2.request_leave("sick", "2024-03-10", "2024-03-12", "Medical treatment"))
    
    # Approve leaves
    print("\n--- APPROVING LEAVES ---")
    print(emp1.approve_leave(0))
    print(emp2.approve_leave(0))
    
    # Employee Information
    print("\n" + emp1.get_info())
    
    # Generate Payslips
    print("\n--- GENERATING PAYSLIPS ---")
    payslip1 = hrms.payroll_system.generate_payslip(emp1, 2, 2024)
    payslip2 = hrms.payroll_system.generate_payslip(emp2, 2, 2024)
    
    print(hrms.payroll_system.print_payslip(payslip1))
    print(hrms.payroll_system.print_payslip(payslip2))
    
    # Department Summary
    print("\n" + dept_it.get_department_summary())
    
    # Intern Progress
    print(f"\n--- INTERN PROGRESS: {emp5.name} ---")
    print(emp5.complete_module("Python Fundamentals"))
    print(emp5.complete_module("OOP Concepts"))
    print(emp5.add_project("HRMS", "Built HR Management System"))
    print(f"Modules Completed: {len(emp5.learning_modules_completed)}")
    
    # Company Report
    print("\n" + hrms.generate_company_report())
    
    print("\n" + "="*70)
    print("DEMO COMPLETED SUCCESSFULLY")
    print("="*70)
    print("\nFile Structure:")
    print("Hari2/")
    print("├── models/")
    print("│   ├── __init__.py")
    print("│   ├── person.py")
    print("│   ├── employee.py")
    print("│   ├── full_time_employee.py")
    print("│   ├── contract_employee.py")
    print("│   ├── intern.py")
    print("│   └── department.py")
    print("├── systems/")
    print("│   ├── __init__.py")
    print("│   ├── payroll_system.py")
    print("│   └── hr_system.py")
    print("└── main.py")
    print("="*70)


if __name__ == "__main__":
    main()
