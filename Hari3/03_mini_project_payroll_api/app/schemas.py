"""
========================================================================
PAYROLL API - Pydantic Schemas
API Contract untuk Employee dan Payroll
========================================================================
"""

from pydantic import BaseModel, Field, EmailStr, validator
from typing import Optional, List
from datetime import date


# ========================================================================
# EMPLOYEE SCHEMAS
# ========================================================================

class EmployeeBase(BaseModel):
    """Base schema untuk Employee dengan common fields."""
    nama: str = Field(..., min_length=1, max_length=100, description="Employee name")
    email: EmailStr = Field(..., description="Valid email address")
    departemen: str = Field(..., min_length=1, description="Department name")
    gaji: float = Field(..., gt=0, description="Base salary (must be positive)")
    
    @validator('gaji')
    def validate_minimum_wage(cls, v):
        """Validate salary meets minimum wage."""
        if v < 3000000:
            raise ValueError('Salary below minimum wage (Rp 3,000,000)')
        return v


class EmployeeCreate(EmployeeBase):
    """Schema untuk create employee request."""
    id: str = Field(..., pattern="^EMP[0-9]{3}$", description="Employee ID (format: EMP001)")
    join_date: date = Field(..., description="Join date (YYYY-MM-DD)")
    
    class Config:
        schema_extra = {
            "example": {
                "id": "EMP001",
                "nama": "Tomas Anderson",
                "email": "tomas@techcorp.com",
                "departemen": "Engineering",
                "gaji": 15000000,
                "join_date": "2020-01-15"
            }
        }


class EmployeeUpdate(BaseModel):
    """Schema untuk update employee (partial update)."""
    nama: Optional[str] = Field(None, min_length=1, max_length=100)
    email: Optional[EmailStr] = None
    departemen: Optional[str] = None
    gaji: Optional[float] = Field(None, gt=0)
    
    @validator('gaji')
    def validate_minimum_wage(cls, v):
        if v is not None and v < 3000000:
            raise ValueError('Salary below minimum wage (Rp 3,000,000)')
        return v
    
    class Config:
        schema_extra = {
            "example": {
                "nama": "Updated Name",
                "gaji": 16000000
            }
        }


class EmployeeResponse(EmployeeBase):
    """Schema untuk employee response."""
    id: str
    join_date: date
    
    class Config:
        schema_extra = {
            "example": {
                "id": "EMP001",
                "nama": "Tomas Anderson",
                "email": "tomas@techcorp.com",
                "departemen": "Engineering",
                "gaji": 15000000,
                "join_date": "2020-01-15"
            }
        }


class EmployeeList(BaseModel):
    """Schema untuk list of employees."""
    employees: List[EmployeeResponse]
    total: int
    
    class Config:
        schema_extra = {
            "example": {
                "employees": [
                    {
                        "id": "EMP001",
                        "nama": "Tomas Anderson",
                        "email": "tomas@techcorp.com",
                        "departemen": "Engineering",
                        "gaji": 15000000,
                        "join_date": "2020-01-15"
                    }
                ],
                "total": 1
            }
        }


# ========================================================================
# PAYROLL SCHEMAS
# ========================================================================

class PayrollDetail(BaseModel):
    """Schema untuk payroll detail satu employee."""
    id: str
    nama: str
    departemen: str
    gross_salary: float = Field(..., description="Gross salary (gaji pokok)")
    tax: float = Field(..., description="Tax deduction (PPh 21)")
    pension: float = Field(..., description="Pension deduction")
    health_insurance: float = Field(..., description="Health insurance")
    total_deductions: float = Field(..., description="Total deductions")
    net_salary: float = Field(..., description="Net salary (take home pay)")
    processed_at: str = Field(..., description="Processing timestamp")
    
    class Config:
        schema_extra = {
            "example": {
                "id": "EMP001",
                "nama": "Tomas Anderson",
                "departemen": "Engineering",
                "gross_salary": 15000000,
                "tax": 750000,
                "pension": 300000,
                "health_insurance": 500000,
                "total_deductions": 1550000,
                "net_salary": 13450000,
                "processed_at": "2024-02-19 10:30:00"
            }
        }


class PayrollResponse(BaseModel):
    """Schema untuk payroll calculation response."""
    employees: List[PayrollDetail]
    summary: dict
    
    class Config:
        schema_extra = {
            "example": {
                "employees": [
                    {
                        "id": "EMP001",
                        "nama": "Tomas Anderson",
                        "departemen": "Engineering",
                        "gross_salary": 15000000,
                        "tax": 750000,
                        "pension": 300000,
                        "health_insurance": 500000,
                        "total_deductions": 1550000,
                        "net_salary": 13450000,
                        "processed_at": "2024-02-19 10:30:00"
                    }
                ],
                "summary": {
                    "total_employees": 1,
                    "total_gross": 15000000,
                    "total_deductions": 1550000,
                    "total_net": 13450000,
                    "average_net": 13450000
                }
            }
        }


class DepartmentPayroll(BaseModel):
    """Schema untuk department payroll summary."""
    departemen: str
    total_employees: int
    total_payroll: float
    employees: List[str]
    
    class Config:
        schema_extra = {
            "example": {
                "departemen": "Engineering",
                "total_employees": 2,
                "total_payroll": 28900000,
                "employees": ["Tomas Anderson", "Sarah Connor"]
            }
        }


# ========================================================================
# STATISTICS SCHEMAS
# ========================================================================

class EmployeeStatistics(BaseModel):
    """Schema untuk employee statistics."""
    total_employees: int
    departments: List[str]
    average_salary: float
    min_salary: float
    max_salary: float
    salary_range: float
    
    class Config:
        schema_extra = {
            "example": {
                "total_employees": 5,
                "departments": ["Engineering", "Finance", "HR"],
                "average_salary": 16000000,
                "min_salary": 12000000,
                "max_salary": 22000000,
                "salary_range": 10000000
            }
        }


# ========================================================================
# ERROR RESPONSE SCHEMAS
# ========================================================================

class ErrorResponse(BaseModel):
    """Schema untuk error response."""
    error: str
    detail: Optional[str] = None
    
    class Config:
        schema_extra = {
            "example": {
                "error": "Employee not found",
                "detail": "Employee ID EMP999 does not exist"
            }
        }


class ValidationErrorDetail(BaseModel):
    """Schema untuk validation error detail."""
    loc: List[str]
    msg: str
    type: str


class ValidationErrorResponse(BaseModel):
    """Schema untuk validation error response."""
    detail: List[ValidationErrorDetail]
    
    class Config:
        schema_extra = {
            "example": {
                "detail": [
                    {
                        "loc": ["body", "gaji"],
                        "msg": "Salary below minimum wage (Rp 3,000,000)",
                        "type": "value_error"
                    }
                ]
            }
        }


# ========================================================================
# SUCCESS RESPONSE SCHEMAS
# ========================================================================

class MessageResponse(BaseModel):
    """Schema untuk simple message response."""
    message: str
    data: Optional[dict] = None
    
    class Config:
        schema_extra = {
            "example": {
                "message": "Operation successful",
                "data": {"id": "EMP001"}
            }
        }
