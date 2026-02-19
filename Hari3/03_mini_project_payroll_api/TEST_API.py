"""
========================================================================
PAYROLL API - Testing Script
Demonstrasi Complete API Endpoints
========================================================================
"""

import requests
import json
from datetime import date

# API Configuration
BASE_URL = "http://127.0.0.1:8000"
HEADERS = {"Content-Type": "application/json"}


def print_response(title: str, response: requests.Response):
    """Helper untuk print response dengan format rapi."""
    print("\n" + "=" * 70)
    print(f"📋 {title}")
    print("=" * 70)
    print(f"Status Code: {response.status_code}")
    print(f"Response:")
    print(json.dumps(response.json(), indent=2, default=str))


def test_health_check():
    """Test health check endpoint."""
    print("\n" + "🏥 TESTING HEALTH CHECK" + "\n")
    response = requests.get(f"{BASE_URL}/health")
    print_response("Health Check", response)
    return response.status_code == 200


def test_create_employees():
    """Test create multiple employees."""
    print("\n" + "👤 TESTING CREATE EMPLOYEES" + "\n")
    
    employees = [
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
            "gaji": 12000000,
            "join_date": "2021-03-20"
        },
        {
            "id": "EMP003",
            "nama": "John McClane",
            "email": "john@techcorp.com",
            "departemen": "Sales",
            "gaji": 10000000,
            "join_date": "2019-06-10"
        },
        {
            "id": "EMP004",
            "nama": "Ellen Ripley",
            "email": "ellen@techcorp.com",
            "departemen": "HR",
            "gaji": 9000000,
            "join_date": "2022-01-05"
        }
    ]
    
    created_count = 0
    for emp in employees:
        response = requests.post(
            f"{BASE_URL}/employees",
            headers=HEADERS,
            json=emp
        )
        if response.status_code == 201:
            print(f"✅ Created: {emp['nama']}")
            created_count += 1
        else:
            print(f"❌ Failed: {emp['nama']} - {response.text}")
    
    print(f"\n📊 Total created: {created_count}/{len(employees)}")
    return created_count > 0


def test_get_all_employees():
    """Test get all employees."""
    print("\n" + "📋 TESTING GET ALL EMPLOYEES" + "\n")
    response = requests.get(f"{BASE_URL}/employees")
    print_response("All Employees", response)
    return response.status_code == 200


def test_filter_by_department():
    """Test filter employees by department."""
    print("\n" + "🔍 TESTING FILTER BY DEPARTMENT" + "\n")
    response = requests.get(f"{BASE_URL}/employees?departemen=Engineering")
    print_response("Engineering Department", response)
    return response.status_code == 200


def test_get_employee_by_id():
    """Test get specific employee."""
    print("\n" + "🔍 TESTING GET EMPLOYEE BY ID" + "\n")
    response = requests.get(f"{BASE_URL}/employees/EMP001")
    print_response("Employee EMP001", response)
    return response.status_code == 200


def test_update_employee():
    """Test update employee."""
    print("\n" + "✏️  TESTING UPDATE EMPLOYEE" + "\n")
    update_data = {
        "gaji": 16000000,
        "departemen": "Engineering - Senior"
    }
    response = requests.put(
        f"{BASE_URL}/employees/EMP001",
        headers=HEADERS,
        json=update_data
    )
    print_response("Updated Employee", response)
    return response.status_code == 200


def test_calculate_payroll():
    """Test payroll calculation."""
    print("\n" + "💰 TESTING PAYROLL CALCULATION" + "\n")
    response = requests.post(f"{BASE_URL}/payroll/calculate")
    print_response("Payroll Calculation", response)
    return response.status_code == 200


def test_department_payroll():
    """Test department payroll report."""
    print("\n" + "📊 TESTING DEPARTMENT PAYROLL" + "\n")
    response = requests.get(f"{BASE_URL}/payroll/department/Engineering")
    print_response("Engineering Payroll", response)
    return response.status_code == 200


def test_employee_statistics():
    """Test employee statistics."""
    print("\n" + "📈 TESTING EMPLOYEE STATISTICS" + "\n")
    response = requests.get(f"{BASE_URL}/employees/statistics/summary")
    print_response("Statistics", response)
    return response.status_code == 200


def test_delete_employee():
    """Test delete employee."""
    print("\n" + "🗑️  TESTING DELETE EMPLOYEE" + "\n")
    response = requests.delete(f"{BASE_URL}/employees/EMP004")
    print_response("Deleted Employee", response)
    return response.status_code == 200


def test_validation_error():
    """Test validation error handling."""
    print("\n" + "❌ TESTING VALIDATION ERROR" + "\n")
    invalid_employee = {
        "id": "INVALID",  # Wrong format
        "nama": "Invalid Employee",
        "email": "not-an-email",  # Invalid email
        "departemen": "Test",
        "gaji": 1000000,  # Below minimum wage
        "join_date": "2024-01-01"
    }
    response = requests.post(
        f"{BASE_URL}/employees",
        headers=HEADERS,
        json=invalid_employee
    )
    print_response("Validation Error (Expected)", response)
    return response.status_code == 422


def test_not_found_error():
    """Test 404 error handling."""
    print("\n" + "🔍 TESTING 404 NOT FOUND" + "\n")
    response = requests.get(f"{BASE_URL}/employees/EMP999")
    print_response("Not Found Error (Expected)", response)
    return response.status_code == 404


def run_all_tests():
    """Run all API tests."""
    print("\n")
    print("=" * 70)
    print("🚀 PAYROLL API - COMPREHENSIVE TESTING")
    print("=" * 70)
    print(f"\nAPI Base URL: {BASE_URL}")
    print("Testing all endpoints...\n")
    
    tests = [
        ("Health Check", test_health_check),
        ("Create Employees", test_create_employees),
        ("Get All Employees", test_get_all_employees),
        ("Filter by Department", test_filter_by_department),
        ("Get Employee by ID", test_get_employee_by_id),
        ("Update Employee", test_update_employee),
        ("Calculate Payroll", test_calculate_payroll),
        ("Department Payroll", test_department_payroll),
        ("Employee Statistics", test_employee_statistics),
        ("Delete Employee", test_delete_employee),
        ("Validation Error", test_validation_error),
        ("404 Not Found", test_not_found_error),
    ]
    
    results = []
    for test_name, test_func in tests:
        try:
            result = test_func()
            results.append((test_name, result))
        except Exception as e:
            print(f"\n❌ ERROR in {test_name}: {str(e)}")
            results.append((test_name, False))
    
    # Print summary
    print("\n" + "=" * 70)
    print("📊 TEST SUMMARY")
    print("=" * 70)
    passed = sum(1 for _, result in results if result)
    total = len(results)
    
    for test_name, result in results:
        status = "✅ PASSED" if result else "❌ FAILED"
        print(f"{status:12} - {test_name}")
    
    print("\n" + "-" * 70)
    print(f"Total: {passed}/{total} tests passed ({passed/total*100:.1f}%)")
    print("=" * 70)
    
    # Important URLs
    print("\n" + "🌐 Important URLs:")
    print(f"   - API Documentation (Swagger): {BASE_URL}/docs")
    print(f"   - API Documentation (ReDoc):   {BASE_URL}/redoc")
    print(f"   - Health Check:                {BASE_URL}/health")
    print("\n")


if __name__ == "__main__":
    try:
        run_all_tests()
    except requests.exceptions.ConnectionError:
        print("\n" + "=" * 70)
        print("❌ ERROR: Cannot connect to API server!")
        print("=" * 70)
        print("\nPlease make sure the API server is running:")
        print("  python RUN_API.py")
        print(f"\nOr manually:")
        print(f"  python -m uvicorn app.main:app --reload")
        print("\n")
