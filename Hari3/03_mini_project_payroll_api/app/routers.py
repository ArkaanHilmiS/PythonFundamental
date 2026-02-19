"""
========================================================================
PAYROLL API - Routers
API Endpoints untuk Employee dan Payroll Management
========================================================================
"""

from fastapi import APIRouter, Depends, HTTPException, status, Query
from typing import List, Optional

from app.schemas import (
    EmployeeCreate,
    EmployeeUpdate,
    EmployeeResponse,
    EmployeeList,
    PayrollResponse,
    DepartmentPayroll,
    EmployeeStatistics,
    MessageResponse
)
from app.services import EmployeeService, PayrollService
from app.repositories import IEmployeeRepository


# ========================================================================
# DEPENDENCY INJECTION
# ========================================================================

def get_repository() -> IEmployeeRepository:
    """
    Get repository instance.
    Ini adalah Dependency yang akan di-inject ke services.
    """
    from app.repositories import EmployeeCSVRepository
    return EmployeeCSVRepository("employees_data.csv")


def get_employee_service(
    repository: IEmployeeRepository = Depends(get_repository)
) -> EmployeeService:
    """Get EmployeeService dengan injected repository."""
    return EmployeeService(repository)


def get_payroll_service(
    repository: IEmployeeRepository = Depends(get_repository)
) -> PayrollService:
    """Get PayrollService dengan injected repository."""
    return PayrollService(repository)


# ========================================================================
# EMPLOYEE ROUTER
# ========================================================================

employee_router = APIRouter(
    prefix="/employees",
    tags=["Employees"],
    responses={404: {"description": "Employee not found"}}
)


@employee_router.get(
    "",
    response_model=EmployeeList,
    summary="Get all employees",
    description="Retrieve list of all employees"
)
async def get_employees(
    departemen: Optional[str] = Query(None, description="Filter by department"),
    service: EmployeeService = Depends(get_employee_service)
):
    """
    Get all employees, optionally filtered by department.
    
    - **departemen**: Optional department filter
    """
    if departemen:
        employees = service.search_employees(departemen=departemen)
    else:
        employees = service.get_all_employees()
    
    return {
        "employees": employees,
        "total": len(employees)
    }


@employee_router.get(
    "/{emp_id}",
    response_model=EmployeeResponse,
    summary="Get employee by ID",
    description="Retrieve specific employee by ID"
)
async def get_employee(
    emp_id: str,
    service: EmployeeService = Depends(get_employee_service)
):
    """
    Get employee by ID.
    
    - **emp_id**: Employee ID (format: EMP001)
    """
    employee = service.get_employee_by_id(emp_id)
    
    if not employee:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Employee {emp_id} not found"
        )
    
    return employee


@employee_router.post(
    "",
    response_model=EmployeeResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Create new employee",
    description="Create new employee with validation"
)
async def create_employee(
    employee: EmployeeCreate,
    service: EmployeeService = Depends(get_employee_service)
):
    """
    Create new employee with following validations:
    
    - **id**: Required, format EMP001-EMP999
    - **nama**: Required, 1-100 characters
    - **email**: Required, valid email format
    - **departemen**: Required
    - **gaji**: Required, minimum Rp 3,000,000
    - **join_date**: Required, date format YYYY-MM-DD
    """
    try:
        employee_data = employee.dict()
        
        # Convert date to string
        if 'join_date' in employee_data:
            employee_data['join_date'] = str(employee_data['join_date'])
        
        created = service.create_employee(employee_data)
        return created
        
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )


@employee_router.put(
    "/{emp_id}",
    response_model=EmployeeResponse,
    summary="Update employee",
    description="Update employee data (partial update supported)"
)
async def update_employee(
    emp_id: str,
    employee: EmployeeUpdate,
    service: EmployeeService = Depends(get_employee_service)
):
    """
    Update employee data.
    
    - **emp_id**: Employee ID to update
    - Provide only fields you want to update
    """
    # Get only provided fields (non-None values)
    update_data = {k: v for k, v in employee.dict().items() if v is not None}
    
    if not update_data:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="No fields to update"
        )
    
    updated = service.update_employee(emp_id, update_data)
    
    if not updated:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Employee {emp_id} not found"
        )
    
    return updated


@employee_router.delete(
    "/{emp_id}",
    response_model=MessageResponse,
    summary="Delete employee",
    description="Delete employee by ID"
)
async def delete_employee(
    emp_id: str,
    service: EmployeeService = Depends(get_employee_service)
):
    """
    Delete employee.
    
    - **emp_id**: Employee ID to delete
    """
    deleted = service.delete_employee(emp_id)
    
    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Employee {emp_id} not found"
        )
    
    return {
        "message": f"Employee {emp_id} deleted successfully",
        "data": {"emp_id": emp_id}
    }


@employee_router.get(
    "/statistics/summary",
    response_model=EmployeeStatistics,
    summary="Get employee statistics",
    description="Get statistical summary of employees"
)
async def get_statistics(
    service: EmployeeService = Depends(get_employee_service)
):
    """
    Get employee statistics including:
    
    - Total employees
    - Departments list
    - Average, min, max salary
    - Salary range
    """
    return service.get_statistics()


# ========================================================================
# PAYROLL ROUTER
# ========================================================================

payroll_router = APIRouter(
    prefix="/payroll",
    tags=["Payroll"],
    responses={404: {"description": "No employees found"}}
)


@payroll_router.post(
    "/calculate",
    response_model=PayrollResponse,
    summary="Calculate payroll",
    description="Calculate payroll for all employees"
)
async def calculate_payroll(
    service: PayrollService = Depends(get_payroll_service)
):
    """
    Calculate payroll untuk semua karyawan.
    
    Calculation includes:
    - Gross salary (gaji pokok)
    - Tax (PPh 21): 5%
    - Pension: 2%
    - Health insurance: Rp 500,000
    - Net salary (take home pay)
    
    Returns:
    - List of employees dengan payroll details
    - Summary dengan total gross, deductions, net salary
    """
    result = service.calculate_payroll()
    
    if not result['employees']:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No employees found to process payroll"
        )
    
    return result


@payroll_router.get(
    "/department/{departemen}",
    response_model=DepartmentPayroll,
    summary="Get department payroll",
    description="Get payroll summary for specific department"
)
async def get_department_payroll(
    departemen: str,
    service: PayrollService = Depends(get_payroll_service)
):
    """
    Get payroll summary untuk specific department.
    
    - **departemen**: Department name (e.g., Engineering, Finance, HR)
    
    Returns:
    - Total employees in department
    - Total payroll for department
    - List of employee names
    """
    result = service.get_department_payroll(departemen)
    
    if result['total_employees'] == 0:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"No employees found in department: {departemen}"
        )
    
    return result
