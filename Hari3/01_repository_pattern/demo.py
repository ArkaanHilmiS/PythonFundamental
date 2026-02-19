"""
========================================================================
HARI 3 - COMPLETE REPOSITORY PATTERN DEMO
Demo lengkap Repository Pattern dengan berbagai scenarios
========================================================================

Run this file to see Repository Pattern in action!
"""

import sys
import os

# Make sure we can import from current directory
sys.path.insert(0, os.path.dirname(__file__))

from repositories import (
    EmployeeCSVRepository,
    EmployeeSQLiteRepository,
    MockEmployeeRepository,
    EmployeeJSONRepository
)
from services import PayrollService, EmployeeService, ReportService


def setup_sample_data():
    """Create sample employee data."""
    return [
        {
            "id": "EMP001",
            "nama": "Tomas Anderson",
            "email": "tomas@techcorp.com",
            "departemen": "Engineering",
            "gaji": 15000000,
            "join_date": "2020-01-15"
        },
        {
            "id": "EMP002",
            "nama": "Sarah Connor",
            "email": "sarah@techcorp.com",
            "departemen": "Engineering",
            "gaji": 20000000,
            "join_date": "2019-03-01"
        },
        {
            "id": "EMP003",
            "nama": "John Wick",
            "email": "john@techcorp.com",
            "departemen": "Finance",
            "gaji": 18000000,
            "join_date": "2021-06-15"
        },
        {
            "id": "EMP004",
            "nama": "Diana Prince",
            "email": "diana@techcorp.com",
            "departemen": "HR",
            "gaji": 16000000,
            "join_date": "2020-08-20"
        },
        {
            "id": "EMP005",
            "nama": "Bruce Wayne",
            "email": "bruce@techcorp.com",
            "departemen": "Finance",
            "gaji": 22000000,
            "join_date": "2018-05-10"
        }
    ]


def demo_repository_basics():
    """Demo 1: Basic Repository Operations."""
    print("\n" + "="*80)
    print("DEMO 1: BASIC REPOSITORY OPERATIONS")
    print("="*80)
    
    sample_data = setup_sample_data()
    
    print("\n--- CSV Repository ---")
    csv_repo = EmployeeCSVRepository("demo_employees.csv")
    csv_repo.save(sample_data)
    
    # Read
    employees = csv_repo.load()
    print(f"Loaded {len(employees)} employees")
    
    # Get by ID
    emp = csv_repo.get_by_id("EMP001")
    print(f"Found: {emp['nama']}")
    
    # Add new
    new_emp = {
        "id": "EMP006",
        "nama": "Clark Kent",
        "email": "clark@techcorp.com",
        "departemen": "Engineering",
        "gaji": 17000000,
        "join_date": "2024-01-01"
    }
    csv_repo.add(new_emp)
    
    # Delete
    csv_repo.delete("EMP006")
    
    print("\n--- SQLite Repository ---")
    sqlite_repo = EmployeeSQLiteRepository("demo_employees.db")
    sqlite_repo.save(sample_data)
    
    # SQL-specific features
    it_employees = sqlite_repo.get_by_department("Engineering")
    print(f"Engineering Department: {[emp['nama'] for emp in it_employees]}")
    
    high_earners = sqlite_repo.get_salary_range(18000000, 25000000)
    print(f"High Earners (>18M): {[emp['nama'] for emp in high_earners]}")
    
    print("\n--- JSON Repository ---")
    json_repo = EmployeeJSONRepository("demo_employees.json")
    json_repo.save(sample_data)
    print("JSON file is human-readable, check demo_employees.json!")
    
    print("\n✓ All repositories work with same interface!")


def demo_replaceable_repositories():
    """Demo 2: Replaceable Repositories (Key Benefit!)."""
    print("\n" + "="*80)
    print("DEMO 2: REPLACEABLE REPOSITORIES")
    print("="*80)
    
    sample_data = setup_sample_data()
    
    # Setup different repositories
    csv_repo = EmployeeCSVRepository("demo_employees.csv")
    csv_repo.save(sample_data)
    
    sqlite_repo = EmployeeSQLiteRepository("demo_employees.db")
    sqlite_repo.save(sample_data)
    
    mock_repo = MockEmployeeRepository(sample_data)
    
    # MAGIC: Same service, different repositories!
    print("\n--- PayrollService with CSV Repository ---")
    payroll_service = PayrollService(csv_repo)
    payroll_service.calculate_payroll()
    
    print("\n--- SAME PayrollService with SQLite Repository ---")
    payroll_service = PayrollService(sqlite_repo)  # Just change this line!
    payroll_service.calculate_payroll()
    
    print("\n--- SAME PayrollService with Mock Repository ---")
    payroll_service = PayrollService(mock_repo)  # Just change this line!
    payroll_service.calculate_payroll()
    
    print("\n✓ Business logic TIDAK BERUBAH!")
    print("✓ Hanya ganti repository implementation!")
    print("✓ This is DEPENDENCY INVERSION PRINCIPLE!")


def demo_testing_with_mock():
    """Demo 3: Testing dengan Mock Repository."""
    print("\n" + "="*80)
    print("DEMO 3: TESTING WITH MOCK REPOSITORY")
    print("="*80)
    
    print("\nScenario: Unit testing PayrollService")
    print("Problem: Kita tidak mau test bergantung pada file atau database nyata")
    print("Solution: Use Mock Repository!")
    
    # Test data
    test_data = [
        {
            "id": "TEST001",
            "nama": "Test Employee",
            "email": "test@company.com",
            "departemen": "IT",
            "gaji": 10000000,
            "join_date": "2024-01-01"
        }
    ]
    
    # Create mock repository (no file, no database!)
    mock_repo = MockEmployeeRepository(test_data)
    
    # Test payroll calculation
    payroll_service = PayrollService(mock_repo)
    result = payroll_service.calculate_payroll()
    
    # Assertions (like in unit tests)
    emp = result[0]
    expected_tax = 10000000 * 0.05  # 500,000
    expected_pension = 10000000 * 0.02  # 200,000
    expected_health = 500000
    expected_net = 10000000 - expected_tax - expected_pension - expected_health
    
    print(f"\n--- TEST RESULTS ---")
    print(f"Gross Salary: Rp {emp['gross_salary']:,.0f}")
    print(f"Tax: Rp {emp['tax']:,.0f} (Expected: Rp {expected_tax:,.0f})")
    print(f"Pension: Rp {emp['pension']:,.0f} (Expected: Rp {expected_pension:,.0f})")
    print(f"Health: Rp {emp['health_insurance']:,.0f} (Expected: Rp {expected_health:,.0f})")
    print(f"Net Salary: Rp {emp['net_salary']:,.0f} (Expected: Rp {expected_net:,.0f})")
    
    assert emp['net_salary'] == expected_net, "❌ Test Failed!"
    print("\n✓ TEST PASSED!")
    print("✓ No file created, no database needed!")
    print("✓ Fast, isolated, repeatable!")


def demo_business_logic_services():
    """Demo 4: Complete Business Logic dengan Services."""
    print("\n" + "="*80)
    print("DEMO 4: COMPLETE BUSINESS LOGIC WITH SERVICES")
    print("="*80)
    
    sample_data = setup_sample_data()
    
    # Setup repository
    repo = EmployeeCSVRepository("demo_employees_full.csv")
    repo.save(sample_data)
    
    # === PayrollService ===
    print("\n--- PayrollService ---")
    payroll_service = PayrollService(repo)
    payroll_service.calculate_payroll()
    
    summary = payroll_service.get_payroll_summary()
    print(f"\nPayroll Summary:")
    print(f"  Total Employees: {summary['total_employees']}")
    print(f"  Total Gross: Rp {summary['total_gross']:,.0f}")
    print(f"  Total Deductions: Rp {summary['total_deductions']:,.0f}")
    print(f"  Total Net: Rp {summary['total_net']:,.0f}")
    print(f"  Average Net: Rp {summary['average_net']:,.0f}")
    
    dept_summary = payroll_service.get_department_payroll("Engineering")
    print(f"\nEngineering Department Payroll:")
    print(f"  Employees: {dept_summary['total_employees']}")
    print(f"  Total: Rp {dept_summary['total_payroll']:,.0f}")
    print(f"  Staff: {dept_summary['employees']}")
    
    # === EmployeeService ===
    print("\n--- EmployeeService ---")
    employee_service = EmployeeService(repo)
    
    # Add new employee
    new_emp = {
        "id": "EMP006",
        "nama": "Peter Parker",
        "email": "peter@techcorp.com",
        "departemen": "Engineering",
        "gaji": 14000000,
        "join_date": "2024-02-01"
    }
    
    try:
        employee_service.add_employee(new_emp)
    except ValueError as e:
        print(f"Validation Error: {e}")
    
    # Search employees
    finance_employees = employee_service.search_employees(departemen="Finance")
    print(f"\nFinance Employees: {[emp['nama'] for emp in finance_employees]}")
    
    # Get statistics
    stats = employee_service.get_statistics()
    print(f"\nEmployee Statistics:")
    print(f"  Total: {stats['total_employees']}")
    print(f"  Departments: {stats['departments']}")
    print(f"  Avg Salary: Rp {stats['average_salary']:,.0f}")
    print(f"  Min Salary: Rp {stats['min_salary']:,.0f}")
    print(f"  Max Salary: Rp {stats['max_salary']:,.0f}")
    
    # === ReportService ===
    print("\n--- ReportService ---")
    report_service = ReportService(repo)
    
    # Generate reports
    payroll_report = report_service.generate_payroll_report()
    print("\n" + payroll_report)
    
    # Export to file
    report_service.export_to_file("payroll", "payroll_report.txt")
    report_service.export_to_file("department", "department_report.txt")


def demo_migration_scenario():
    """Demo 5: Real-World Migration Scenario."""
    print("\n" + "="*80)
    print("DEMO 5: REAL-WORLD MIGRATION SCENARIO")
    print("="*80)
    
    print("\nScenario: Company starts with CSV, grows to need Database")
    
    # Phase 1: Small company, CSV is enough
    print("\n--- PHASE 1: Small Company (CSV) ---")
    sample_data = setup_sample_data()
    
    csv_repo = EmployeeCSVRepository("company_data.csv")
    csv_repo.save(sample_data)
    
    payroll_service = PayrollService(csv_repo)
    employee_service = EmployeeService(csv_repo)
    
    payroll_service.calculate_payroll()
    stats = employee_service.get_statistics()
    print(f"Company Stats: {stats['total_employees']} employees")
    
    # Phase 2: Company grows, needs database
    print("\n--- PHASE 2: Growing Company (Migrate to SQLite) ---")
    print("Decision: Move to database for better performance")
    
    # Migration: Load from CSV, save to SQLite
    employees = csv_repo.load()
    
    sqlite_repo = EmployeeSQLiteRepository("company_data.db")
    sqlite_repo.save(employees)
    
    print("✓ Data migrated from CSV to SQLite!")
    
    # Use services with new repository
    # BUSINESS LOGIC CODE DOES NOT CHANGE!
    payroll_service = PayrollService(sqlite_repo)
    employee_service = EmployeeService(sqlite_repo)
    
    payroll_service.calculate_payroll()
    stats = employee_service.get_statistics()
    print(f"Company Stats: {stats['total_employees']} employees")
    
    print("\n✓ Migration Complete!")
    print("✓ Business logic code TIDAK BERUBAH!")
    print("✓ Just changed repository instantiation!")
    print("✓ This is why Repository Pattern is POWERFUL!")


def main():
    """Run all demos."""
    print("="*80)
    print("REPOSITORY PATTERN - COMPLETE DEMO")
    print("Hari 3: Data Layer yang Professional")
    print("="*80)
    
    demos = [
        ("Repository Basics", demo_repository_basics),
        ("Replaceable Repositories", demo_replaceable_repositories),
        ("Testing with Mock", demo_testing_with_mock),
        ("Business Logic Services", demo_business_logic_services),
        ("Migration Scenario", demo_migration_scenario)
    ]
    
    for i, (name, demo_func) in enumerate(demos, 1):
        try:
            demo_func()
            input(f"\n--- Press Enter to continue to Demo {i+1 if i < len(demos) else 'Summary'} ---")
        except Exception as e:
            print(f"\n❌ Error in {name}: {e}")
            import traceback
            traceback.print_exc()
            continue
    
    # Final Summary
    print("\n" + "="*80)
    print("SUMMARY - KEY TAKEAWAYS")
    print("="*80)
    print("""
✅ 1. SEPARATION OF CONCERNS
   - Data access (Repository) terpisah dari business logic (Service)

✅ 2. REPLACEABLE IMPLEMENTATIONS
   - Ganti CSV → SQLite → API tanpa ubah business logic

✅ 3. TESTABLE
   - Mock repository untuk unit testing tanpa file/database

✅ 4. MAINTAINABLE
   - Clear structure, easy to understand and modify

✅ 5. SCALABLE
   - Easy to add new data sources or services

✅ 6. PROFESSIONAL
   - Industry-standard pattern used in production systems

REMEMBER:
"Program to an interface, not an implementation"
- Gang of Four (Design Patterns)

Repository Pattern adalah FUNDAMENTAL untuk:
- Clean Architecture
- Microservices
- Domain-Driven Design
- Test-Driven Development

NEXT:
Bagian B - FastAPI: Build REST API dengan Repository Pattern! 🚀
    """)
    
    print("="*80)
    print("Files generated:")
    print("- demo_employees.csv")
    print("- demo_employees.db")
    print("- demo_employees.json")
    print("- company_data.csv")
    print("- company_data.db")
    print("- payroll_report.txt")
    print("- department_report.txt")
    print("="*80)


if __name__ == "__main__":
    main()
