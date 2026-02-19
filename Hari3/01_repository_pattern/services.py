"""
========================================================================
HARI 3 - BUSINESS LOGIC LAYER (SERVICES)
Services that use Repository Pattern
========================================================================

Ini adalah contoh bagaimana Business Logic menggunakan Repository.
Perhatikan bahwa Service TIDAK PEDULI repository mana yang dipakai!
"""

from typing import List, Dict
from datetime import datetime
from repositories import IEmployeeRepository


# ========================================================================
# 1. PAYROLL SERVICE
# ========================================================================

class PayrollService:
    """
    Service untuk menghitung payroll karyawan.
    
    ARCHITECTURE:
    ============
    
    PayrollService (Business Logic)
         ↓ uses
    IEmployeeRepository (Interface)
         ↑ implements
    ┌────┴────┬────────┬────────┐
    │         │        │        │
    CSV    SQLite   JSON    Mock
    
    KEY POINT:
    PayrollService HANYA TAHU interface, TIDAK TAHU implementation!
    Ini adalah Dependency Inversion Principle (SOLID).
    """
    
    # Tax rates (business rules)
    TAX_RATE = 0.05  # PPh 21: 5%
    PENSION_RATE = 0.02  # Pension: 2%
    HEALTH_INSURANCE = 500000  # Fix: Rp 500,000
    
    def __init__(self, repository: IEmployeeRepository):
        """
        Initialize PayrollService with any repository.
        
        Args:
            repository: Any object that implements IEmployeeRepository
        
        MAGIC:
        ======
        Karena pakai interface, kita bisa pass:
        - EmployeeCSVRepository("data.csv")
        - EmployeeSQLiteRepository("data.db")
        - MockEmployeeRepository([...])
        
        Service code TIDAK BERUBAH!
        """
        self.repository = repository
    
    def calculate_payroll(self) -> List[Dict]:
        """
        Calculate payroll untuk semua karyawan.
        
        Business Logic:
        1. Load employees dari repository
        2. Calculate gross salary
        3. Calculate deductions
        4. Calculate net salary
        5. Save hasil ke repository
        
        Returns:
            List of employees dengan payroll calculated
        """
        print("\n" + "="*70)
        print("CALCULATING PAYROLL")
        print("="*70)
        
        # Step 1: Load employees
        # ----------------------
        # Service TIDAK TAHU dari mana data datang!
        # Mungkin dari CSV, SQLite, API, atau Mock
        employees = self.repository.load()
        
        if not employees:
            print("⚠ No employees found")
            return []
        
        print(f"Processing payroll for {len(employees)} employees...")
        
        # Step 2-4: Calculate payroll
        # ---------------------------
        # Ini adalah PURE BUSINESS LOGIC
        # Tidak ada file handling, no SQL queries
        # Just business rules!
        
        for emp in employees:
            gross_salary = float(emp.get('gaji', 0))
            
            # Deductions
            tax = gross_salary * self.TAX_RATE
            pension = gross_salary * self.PENSION_RATE
            health = self.HEALTH_INSURANCE
            
            total_deductions = tax + pension + health
            net_salary = gross_salary - total_deductions
            
            # Add calculated fields
            emp['gross_salary'] = gross_salary
            emp['tax'] = tax
            emp['pension'] = pension
            emp['health_insurance'] = health
            emp['total_deductions'] = total_deductions
            emp['net_salary'] = net_salary
            emp['processed_at'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            
            print(f"✓ {emp['nama']:<25} Net: Rp {net_salary:>12,.0f}")
        
        # Step 5: Save hasil
        # ------------------
        # Service TIDAK TAHU kemana data disimpan!
        self.repository.save(employees)
        
        print("="*70)
        print("✓ PAYROLL CALCULATION COMPLETED")
        print("="*70)
        
        return employees
    
    def get_payroll_summary(self) -> Dict:
        """
        Get summary of payroll.
        
        Returns:
            Dictionary dengan total gross, deductions, net
        """
        employees = self.repository.load()
        
        if not employees:
            return {
                "total_employees": 0,
                "total_gross": 0,
                "total_deductions": 0,
                "total_net": 0
            }
        
        # Calculate totals
        total_gross = sum(float(emp.get('gross_salary', emp.get('gaji', 0))) 
                         for emp in employees)
        total_deductions = sum(float(emp.get('total_deductions', 0)) 
                              for emp in employees)
        total_net = sum(float(emp.get('net_salary', 0)) 
                       for emp in employees)
        
        return {
            "total_employees": len(employees),
            "total_gross": total_gross,
            "total_deductions": total_deductions,
            "total_net": total_net,
            "average_net": total_net / len(employees) if employees else 0
        }
    
    def get_department_payroll(self, departemen: str) -> Dict:
        """
        Get payroll summary untuk satu department.
        
        Args:
            departemen: Department name
        
        Returns:
            Payroll summary untuk department
        """
        employees = self.repository.load()
        dept_employees = [emp for emp in employees 
                         if emp.get('departemen') == departemen]
        
        if not dept_employees:
            return {
                "departemen": departemen,
                "total_employees": 0,
                "total_payroll": 0
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
# 2. EMPLOYEE SERVICE
# ========================================================================

class EmployeeService:
    """
    Service untuk manage employees.
    
    Responsibilities:
    - Add new employee dengan validation
    - Update employee data
    - Delete employee
    - Search employees
    """
    
    def __init__(self, repository: IEmployeeRepository):
        """Initialize dengan any repository."""
        self.repository = repository
    
    def add_employee(self, employee_data: Dict) -> Dict:
        """
        Add new employee dengan validation.
        
        Args:
            employee_data: Employee information
        
        Returns:
            Added employee data
        
        Raises:
            ValueError: If validation fails
        """
        # BUSINESS VALIDATION
        # ===================
        # Ini adalah business logic responsibility
        # Bukan repository responsibility!
        
        # Validate required fields
        required_fields = ['id', 'nama', 'email', 'departemen', 'gaji']
        for field in required_fields:
            if field not in employee_data:
                raise ValueError(f"❌ Field '{field}' is required")
        
        # Validate email format (simple)
        email = employee_data['email']
        if '@' not in email:
            raise ValueError(f"❌ Invalid email format: {email}")
        
        # Validate salary
        gaji = float(employee_data['gaji'])
        if gaji < 0:
            raise ValueError(f"❌ Salary cannot be negative")
        if gaji < 3000000:  # UMR Jakarta 2024
            print(f"⚠ Warning: Salary below minimum wage (Rp 3,000,000)")
        
        # Add timestamp
        employee_data['created_at'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # Add to repository
        self.repository.add(employee_data)
        
        return employee_data
    
    def update_employee(self, emp_id: str, updated_data: Dict) -> Dict:
        """
        Update employee data.
        
        Args:
            emp_id: Employee ID
            updated_data: Fields to update
        
        Returns:
            Updated employee data
        """
        # Load current data
        employee = self.repository.get_by_id(emp_id)
        
        if not employee:
            raise ValueError(f"❌ Employee ID {emp_id} not found")
        
        # Update fields
        employee.update(updated_data)
        employee['updated_at'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # Save all employees with updated data
        employees = self.repository.load()
        employees = [employee if emp.get('id') == emp_id else emp 
                    for emp in employees]
        self.repository.save(employees)
        
        print(f"✓ Updated employee: {emp_id}")
        return employee
    
    def search_employees(self, **criteria) -> List[Dict]:
        """
        Search employees by criteria.
        
        Args:
            **criteria: Search criteria (nama, departemen, etc.)
        
        Returns:
            List of matching employees
        
        Example:
            service.search_employees(departemen="IT")
            service.search_employees(gaji=15000000)
        """
        employees = self.repository.load()
        
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
        """
        Get employee statistics.
        
        Returns:
            Statistics dictionary
        """
        employees = self.repository.load()
        
        if not employees:
            return {
                "total_employees": 0,
                "departments": [],
                "average_salary": 0,
                "min_salary": 0,
                "max_salary": 0
            }
        
        # Calculate statistics
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


# ========================================================================
# 3. REPORT SERVICE
# ========================================================================

class ReportService:
    """
    Service untuk generate reports.
    
    Responsibilities:
    - Generate payroll reports
    - Generate department reports
    - Export reports to different formats
    """
    
    def __init__(self, repository: IEmployeeRepository):
        """Initialize dengan any repository."""
        self.repository = repository
    
    def generate_payroll_report(self) -> str:
        """
        Generate formatted payroll report.
        
        Returns:
            Formatted report string
        """
        employees = self.repository.load()
        
        report = []
        report.append("=" * 80)
        report.append("PAYROLL REPORT")
        report.append(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        report.append("=" * 80)
        report.append("")
        
        # Header
        report.append(f"{'ID':<10} {'Name':<25} {'Department':<15} {'Net Salary':>15}")
        report.append("-" * 80)
        
        # Data
        total_payroll = 0
        for emp in employees:
            net_salary = float(emp.get('net_salary', emp.get('gaji', 0)))
            total_payroll += net_salary
            
            report.append(
                f"{emp.get('id', ''):<10} "
                f"{emp.get('nama', ''):<25} "
                f"{emp.get('departemen', ''):<15} "
                f"Rp {net_salary:>12,.0f}"
            )
        
        # Summary
        report.append("-" * 80)
        report.append(f"{'TOTAL':<52} Rp {total_payroll:>12,.0f}")
        report.append("=" * 80)
        
        return "\n".join(report)
    
    def generate_department_report(self) -> str:
        """
        Generate department summary report.
        
        Returns:
            Formatted report string
        """
        employees = self.repository.load()
        
        # Group by department
        dept_data = {}
        for emp in employees:
            dept = emp.get('departemen', 'Unknown')
            if dept not in dept_data:
                dept_data[dept] = {
                    'count': 0,
                    'total_salary': 0,
                    'employees': []
                }
            
            dept_data[dept]['count'] += 1
            dept_data[dept]['total_salary'] += float(emp.get('net_salary', 
                                                             emp.get('gaji', 0)))
            dept_data[dept]['employees'].append(emp.get('nama'))
        
        # Build report
        report = []
        report.append("=" * 80)
        report.append("DEPARTMENT REPORT")
        report.append(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        report.append("=" * 80)
        report.append("")
        
        for dept, data in dept_data.items():
            report.append(f"Department: {dept}")
            report.append(f"  Employees: {data['count']}")
            report.append(f"  Total Payroll: Rp {data['total_salary']:,.0f}")
            report.append(f"  Average Salary: Rp {data['total_salary']/data['count']:,.0f}")
            report.append(f"  Staff: {', '.join(data['employees'])}")
            report.append("")
        
        report.append("=" * 80)
        
        return "\n".join(report)
    
    def export_to_file(self, report_type: str, filename: str):
        """
        Export report to file.
        
        Args:
            report_type: 'payroll' or 'department'
            filename: Output filename
        """
        if report_type == 'payroll':
            report = self.generate_payroll_report()
        elif report_type == 'department':
            report = self.generate_department_report()
        else:
            raise ValueError(f"Unknown report type: {report_type}")
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(report)
        
        print(f"✓ Report exported to: {filename}")


# ========================================================================
# DEMO USAGE
# ========================================================================

if __name__ == "__main__":
    from repositories import (
        EmployeeCSVRepository,
        EmployeeSQLiteRepository,
        MockEmployeeRepository
    )
    
    print("="*70)
    print("SERVICES DEMO - Business Logic with Repository Pattern")
    print("="*70)
    
    # Sample data
    sample_data = [
        {
            "id": "EMP001",
            "nama": "Tomas Anderson",
            "email": "tomas@company.com",
            "departemen": "IT",
            "gaji": 15000000,
            "join_date": "2020-01-15"
        },
        {
            "id": "EMP002",
            "nama": "Sarah Connor",
            "email": "sarah@company.com",
            "departemen": "IT",
            "gaji": 20000000,
            "join_date": "2019-03-01"
        },
        {
            "id": "EMP003",
            "nama": "John Wick",
            "email": "john@company.com",
            "departemen": "Finance",
            "gaji": 18000000,
            "join_date": "2021-06-15"
        }
    ]
    
    # Demo 1: PayrollService dengan CSV Repository
    print("\n" + "="*70)
    print("DEMO 1: PayrollService with CSV Repository")
    print("="*70)
    
    csv_repo = EmployeeCSVRepository("employees_service_demo.csv")
    csv_repo.save(sample_data)
    
    payroll_service = PayrollService(csv_repo)
    payroll_service.calculate_payroll()
    
    summary = payroll_service.get_payroll_summary()
    print(f"\nPAYROLL SUMMARY:")
    print(f"Total Employees: {summary['total_employees']}")
    print(f"Total Gross: Rp {summary['total_gross']:,.0f}")
    print(f"Total Deductions: Rp {summary['total_deductions']:,.0f}")
    print(f"Total Net: Rp {summary['total_net']:,.0f}")
    
    # Demo 2: Same Service with SQLite Repository
    print("\n" + "="*70)
    print("DEMO 2: SAME PayrollService with SQLite Repository")
    print("="*70)
    
    sqlite_repo = EmployeeSQLiteRepository("employees_service_demo.db")
    sqlite_repo.save(sample_data)
    
    # MAGIC: Same service code, different repository!
    payroll_service = PayrollService(sqlite_repo)
    payroll_service.calculate_payroll()
    
    # Demo 3: EmployeeService
    print("\n" + "="*70)
    print("DEMO 3: EmployeeService")
    print("="*70)
    
    employee_service = EmployeeService(csv_repo)
    
    # Add new employee
    new_emp = {
        "id": "EMP004",
        "nama": "Alice Johnson",
        "email": "alice@company.com",
        "departemen": "HR",
        "gaji": 12000000,
        "join_date": "2024-01-01"
    }
    employee_service.add_employee(new_emp)
    
    # Search
    it_employees = employee_service.search_employees(departemen="IT")
    print(f"IT Employees: {[emp['nama'] for emp in it_employees]}")
    
    # Statistics
    stats = employee_service.get_statistics()
    print(f"\nSTATISTICS:")
    print(f"Total Employees: {stats['total_employees']}")
    print(f"Departments: {stats['departments']}")
    print(f"Average Salary: Rp {stats['average_salary']:,.0f}")
    
    # Demo 4: ReportService
    print("\n" + "="*70)
    print("DEMO 4: ReportService")
    print("="*70)
    
    report_service = ReportService(csv_repo)
    
    payroll_report = report_service.generate_payroll_report()
    print(payroll_report)
    
    dept_report = report_service.generate_department_report()
    print("\n" + dept_report)
    
    print("\n" + "="*70)
    print("✓ KEY TAKEAWAY")
    print("="*70)
    print("Business Logic (Services) TIDAK BERGANTUNG pada storage!")
    print("Kita bisa switch dari CSV → SQLite → API tanpa ubah service!")
    print("This is the power of Repository Pattern! 🚀")
    print("="*70)
