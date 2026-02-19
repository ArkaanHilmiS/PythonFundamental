"""
========================================================================
HARI 3 - BAGIAN B: FASTAPI THEORY
Modern Backend Framework untuk Python
========================================================================

Materi ini mengajarkan FastAPI dari dasar sampai production-ready.
"""

# ========================================================================
# 1. APA ITU FASTAPI?
# ========================================================================

"""
FASTAPI adalah modern web framework untuk building APIs dengan Python 3.7+

KEY FEATURES:
=============

✅ 1. FAST (Performance)
   - Setara dengan NodeJS dan Go
   - Berbasis Starlette (async framework)
   - Salah satu framework Python tercepat

✅ 2. FAST (Development)
   - Easy to learn
   - Less code
   - Fewer bugs
   - Intuitive

✅ 3. AUTOMATIC VALIDATION
   - Based on Python type hints
   - Pydantic validation
   - No manual validation code

✅ 4. AUTOMATIC DOCUMENTATION
   - Swagger UI (Interactive docs)
   - ReDoc (Alternative docs)
   - Both auto-generated!

✅ 5. MODERN PYTHON
   - Async/await support
   - Type hints as core feature
   - Python 3.7+ syntax

✅ 6. PRODUCTION READY
   - ASGI compliant
   - OAuth2 with JWT
   - Database integration
   - Testing support


REAL WORLD COMPARISON:
=====================

┌─────────────────┬──────────┬──────────┬──────────┐
│     Feature     │  Flask   │  Django  │ FastAPI  │
├─────────────────┼──────────┼──────────┼──────────┤
│ Performance     │    ⭐⭐   │   ⭐⭐⭐  │  ⭐⭐⭐⭐⭐ │
│ Learning Curve  │   Easy   │  Medium  │   Easy   │
│ Auto Validation │    ❌    │   Partial│    ✅    │
│ Auto Docs       │    ❌    │    ❌    │    ✅    │
│ Async Support   │  Partial │  Partial │   Native │
│ Type Hints      │ Optional │ Optional │   Core   │
│ API Focus       │  Partial │   No     │    ✅    │
│ Microservices   │    ⭐⭐   │    ⭐    │  ⭐⭐⭐⭐⭐ │
└─────────────────┴──────────┴──────────┴──────────┘


WHEN TO USE FASTAPI?
===================

✅ PAKAI FastAPI untuk:
- REST API backends
- Microservices
- ML model deployment
- Real-time applications
- High-performance APIs
- Modern async applications

❌ JANGAN pakai FastAPI untuk:
- Server-side rendered websites (use Django)
- Simple static sites (use Flask)
- Legacy projects (stick with existing framework)
"""


# ========================================================================
# 2. FASTAPI vs FLASK (Detailed Comparison)
# ========================================================================

"""
EXAMPLE: Same endpoint in Flask vs FastAPI

═══════════════════════════════════════════════════════
FLASK (Traditional Way)
═══════════════════════════════════════════════════════
"""

# Flask example
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/users', methods=['POST'])
def create_user():
    # Manual validation
    data = request.get_json()
    
    # Check if data exists
    if not data:
        return jsonify({"error": "No data provided"}), 400
    
    # Check required fields
    if 'name' not in data:
        return jsonify({"error": "name is required"}), 400
    if 'email' not in data:
        return jsonify({"error": "email is required"}), 400
    if 'age' not in data:
        return jsonify({"error": "age is required"}), 400
    
    # Type validation
    if not isinstance(data['name'], str):
        return jsonify({"error": "name must be string"}), 400
    if not isinstance(data['email'], str):
        return jsonify({"error": "email must be string"}), 400
    if not isinstance(data['age'], int):
        return jsonify({"error": "age must be integer"}), 400
    
    # Business validation
    if data['age'] < 0:
        return jsonify({"error": "age must be positive"}), 400
    if '@' not in data['email']:
        return jsonify({"error": "invalid email"}), 400
    
    # Process...
    return jsonify(data), 201

"""
Problems with Flask approach:
❌ Banyak manual validation (prone to bugs)
❌ Lots of boilerplate code
❌ No automatic documentation
❌ No type checking
❌ Hard to maintain


═══════════════════════════════════════════════════════
FASTAPI (Modern Way)
═══════════════════════════════════════════════════════
"""

# FastAPI example
from fastapi import FastAPI
from pydantic import BaseModel, EmailStr, Field

app = FastAPI()

class User(BaseModel):
    name: str = Field(..., min_length=1)
    email: EmailStr
    age: int = Field(..., ge=0)  # ge = greater than or equal

@app.post("/users", status_code=201)
async def create_user(user: User):
    # Validation AUTOMATIC!
    # FastAPI validates:
    # - name is string
    # - email is valid email format
    # - age is integer >= 0
    
    return user

"""
Benefits of FastAPI approach:
✅ Automatic validation (based on type hints)
✅ Minimal code
✅ Automatic documentation
✅ Type safety
✅ Easy to maintain

LESS CODE = FEWER BUGS = FASTER DEVELOPMENT
"""


# ========================================================================
# 3. FASTAPI ARCHITECTURE
# ========================================================================

"""
PROFESSIONAL FASTAPI PROJECT STRUCTURE:
=======================================

my_api/
├── app/
│   ├── __init__.py
│   ├── main.py              # FastAPI app instance
│   ├── config.py            # Configuration
│   ├── models/              # Data models (SQLAlchemy/etc)
│   │   ├── __init__.py
│   │   └── employee.py
│   ├── schemas/             # Pydantic schemas (API contract)
│   │   ├── __init__.py
│   │   └── employee.py
│   ├── repositories/        # Data access layer
│   │   ├── __init__.py
│   │   └── employee.py
│   ├── services/            # Business logic
│   │   ├── __init__.py
│   │   └── payroll.py
│   └── routers/             # API endpoints
│       ├── __init__.py
│       ├── employees.py
│       └── payroll.py
├── tests/                   # Unit tests
├── requirements.txt         # Dependencies
└── README.md


LAYER RESPONSIBILITIES:
======================

┌────────────────────────────────────────────────┐
│  ROUTERS (API Endpoints)                       │
│  - Handle HTTP requests                        │
│  - Path parameters                             │
│  - Query parameters                            │
│  - Return responses                            │
└──────────────────┬─────────────────────────────┘
                   │
                   ↓
┌────────────────────────────────────────────────┐
│  SCHEMAS (Data Validation & Serialization)     │
│  - Input validation                            │
│  - Output serialization                        │
│  - API contract definition                     │
└──────────────────┬─────────────────────────────┘
                   │
                   ↓
┌────────────────────────────────────────────────┐
│  SERVICES (Business Logic)                     │
│  - Business rules                              │
│  - Calculations                                │
│  - Orchestration                               │
└──────────────────┬─────────────────────────────┘
                   │
                   ↓
┌────────────────────────────────────────────────┐
│  REPOSITORIES (Data Access)                    │
│  - CRUD operations                             │
│  - Database queries                            │
│  - File operations                             │
└──────────────────┬─────────────────────────────┘
                   │
                   ↓
┌────────────────────────────────────────────────┐
│  DATABASE / STORAGE                            │
└────────────────────────────────────────────────┘

This is CLEAN ARCHITECTURE!
"""


# ========================================================================
# 4. PYDANTIC SCHEMAS (API CONTRACT)
# ========================================================================

"""
PYDANTIC adalah library untuk data validation menggunakan type hints.

WHY PYDANTIC?
=============

✅ Automatic validation
✅ Type conversion
✅ Error messages
✅ JSON serialization
✅ Schema generation

SCHEMAS vs MODELS:
==================

- SCHEMA = API contract (Request/Response format)
- MODEL = Database/Business entity

Example:
"""

from pydantic import BaseModel, Field, validator
from typing import Optional
from datetime import date

class EmployeeBase(BaseModel):
    """Base schema untuk Employee."""
    nama: str = Field(..., min_length=1, max_length=100)
    email: str
    departemen: str
    gaji: float = Field(..., gt=0)  # gt = greater than

class EmployeeCreate(EmployeeBase):
    """Schema untuk create employee (Input)."""
    id: str
    join_date: date
    
    @validator('email')
    def validate_email(cls, v):
        """Custom validator untuk email."""
        if '@' not in v:
            raise ValueError('Invalid email format')
        return v
    
    @validator('gaji')
    def validate_minimum_wage(cls, v):
        """Validate minimum wage (UMR Jakarta 2024)."""
        if v < 3000000:
            raise ValueError('Salary below minimum wage')
        return v

class EmployeeResponse(EmployeeBase):
    """Schema untuk response employee (Output)."""
    id: str
    join_date: date
    created_at: str
    
    class Config:
        # Allow reading from ORM models
        orm_mode = True

class EmployeeUpdate(BaseModel):
    """Schema untuk update employee (Partial)."""
    nama: Optional[str] = None
    email: Optional[str] = None
    departemen: Optional[str] = None
    gaji: Optional[float] = None

"""
BENEFITS:
=========

1. ❌ Manual validation:
   if 'nama' not in data:
       return error
   if not isinstance(data['gaji'], float):
       return error
   if data['gaji'] < 0:
       return error

2. ✅ Pydantic validation:
   gaji: float = Field(..., gt=0)
   
   ONE LINE!


TYPE HINTS BENEFITS:
====================

✅ Auto-completion in IDE
✅ Type checking (mypy, pyright)
✅ Self-documenting code
✅ Fewer runtime errors
"""


# ========================================================================
# 5. FASTAPI ROUTING
# ========================================================================

"""
ROUTING adalah mapping URL ke function yang handle request.

BASIC ROUTING:
=============
"""

from fastapi import FastAPI, Query, Path, Body

app = FastAPI()

# GET request
@app.get("/")
async def root():
    return {"message": "Hello World"}

# Path parameter
@app.get("/users/{user_id}")
async def get_user(user_id: int):
    return {"user_id": user_id}

# Query parameter
@app.get("/items")
async def get_items(skip: int = 0, limit: int = 10):
    return {"skip": skip, "limit": limit}

# Request body
@app.post("/users")
async def create_user(user: User):
    return user

"""
ADVANCED ROUTING:
=================
"""

# Validation dengan Query
@app.get("/search")
async def search(
    q: str = Query(..., min_length=3, max_length=50),
    page: int = Query(1, ge=1),
    limit: int = Query(10, ge=1, le=100)
):
    return {"query": q, "page": page, "limit": limit}

# Path validation
@app.get("/employees/{emp_id}")
async def get_employee(
    emp_id: str = Path(..., regex="^EMP[0-9]{3}$")
):
    # emp_id must be like "EMP001"
    return {"emp_id": emp_id}

# Multiple body parameters
@app.put("/employees/{emp_id}")
async def update_employee(
    emp_id: str,
    employee: EmployeeUpdate,
    note: str = Body(...)
):
    return {"emp_id": emp_id, "employee": employee, "note": note}


# ========================================================================
# 6. DEPENDENCY INJECTION
# ========================================================================

"""
DEPENDENCY INJECTION adalah pattern untuk inject dependencies ke endpoint.

Benefits:
✅ Reusable code
✅ Testable
✅ Clean separation
✅ Easy to mock

Example:
"""

from fastapi import Depends

# Dependency function
def get_repository():
    """Provide repository instance."""
    from repositories import EmployeeCSVRepository
    return EmployeeCSVRepository("employees.csv")

def get_payroll_service(repo = Depends(get_repository)):
    """Provide payroll service with injected repository."""
    from services import PayrollService
    return PayrollService(repo)

# Use dalam endpoint
@app.post("/payroll/calculate")
async def calculate_payroll(
    service: PayrollService = Depends(get_payroll_service)
):
    result = service.calculate_payroll()
    return result

"""
BENEFITS:
=========

❌ Without DI:
@app.post("/payroll/calculate")
async def calculate_payroll():
    repo = EmployeeCSVRepository("employees.csv")  # Hardcoded!
    service = PayrollService(repo)
    result = service.calculate_payroll()
    return result

Problems:
- Hardcoded dependency
- Hard to test
- Hard to change implementation

✅ With DI:
@app.post("/payroll/calculate")
async def calculate_payroll(
    service: PayrollService = Depends(get_payroll_service)
):
    result = service.calculate_payroll()
    return result

Benefits:
- Injected dependency
- Easy to test (inject mock)
- Easy to change (change get_payroll_service only)
"""


# ========================================================================
# 7. ERROR HANDLING
# ========================================================================

"""
FastAPI memiliki error handling yang powerful.
"""

from fastapi import HTTPException, status

@app.get("/employees/{emp_id}")
async def get_employee(emp_id: str):
    # Example: Employee not found
    employee = None  # from repository
    
    if not employee:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Employee {emp_id} not found"
        )
    
    return employee

# Custom exception handler
from fastapi import Request
from fastapi.responses import JSONResponse

class EmployeeNotFoundException(Exception):
    def __init__(self, emp_id: str):
        self.emp_id = emp_id

@app.exception_handler(EmployeeNotFoundException)
async def employee_not_found_handler(
    request: Request, 
    exc: EmployeeNotFoundException
):
    return JSONResponse(
        status_code=404,
        content={
            "error": "Employee not found",
            "emp_id": exc.emp_id
        }
    )


# ========================================================================
# 8. AUTOMATIC DOCUMENTATION
# ========================================================================

"""
FastAPI automatically generates interactive API documentation!

SWAGGER UI (OpenAPI):
====================
http://localhost:8000/docs

Features:
- Interactive API testing
- Request/response examples
- Schema documentation
- Try it out functionality

REDOC:
======
http://localhost:8000/redoc

Features:
- Clean documentation
- Easy to read
- Great for sharing with team

Example dengan metadata:
"""

app = FastAPI(
    title="Employee Management API",
    description="API for managing employee and payroll",
    version="1.0.0",
    contact={
        "name": "Tech Corp",
        "email": "api@techcorp.com"
    }
)

@app.post(
    "/employees",
    response_model=EmployeeResponse,
    status_code=status.HTTP_201_CREATED,
    tags=["Employees"],
    summary="Create new employee",
    description="Create a new employee with validation"
)
async def create_employee(employee: EmployeeCreate):
    """
    Create new employee with following validations:
    
    - **name**: required, 1-100 characters
    - **email**: required, valid email format
    - **salary**: required, must be >= Rp 3,000,000 (UMR)
    - **join_date**: required, date format
    """
    return employee

"""
This generates BEAUTIFUL documentation automatically!
"""


# ========================================================================
# 9. TESTING FASTAPI
# ========================================================================

"""
FastAPI memiliki excellent testing support.
"""

from fastapi.testclient import TestClient

# test_main.py
def test_root():
    client = TestClient(app)
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}

def test_create_employee():
    client = TestClient(app)
    
    employee_data = {
        "id": "EMP001",
        "nama": "Test Employee",
        "email": "test@company.com",
        "departemen": "IT",
        "gaji": 5000000,
        "join_date": "2024-01-01"
    }
    
    response = client.post("/employees", json=employee_data)
    assert response.status_code == 201
    assert response.json()["nama"] == "Test Employee"


# ========================================================================
# 10. DEPLOYMENT
# ========================================================================

"""
DEVELOPMENT:
===========
uvicorn main:app --reload

PRODUCTION:
===========
uvicorn main:app --host 0.0.0.0 --port 8000 --workers 4

DOCKER:
=======
FROM python:3.11
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]

CLOUD:
======
- AWS Lambda dengan Mangum
- Google Cloud Run
- Azure App Service
- Heroku
- Railway
"""


# ========================================================================
# SUMMARY
# ========================================================================

"""
FASTAPI KEY TAKEAWAYS:
=====================

✅ 1. MODERN & FAST
   - High performance
   - Async support
   - Type hints as core

✅ 2. DEVELOPER FRIENDLY
   - Less code
   - Auto validation
   - Auto documentation

✅ 3. PRODUCTION READY
   - Error handling
   - Testing support
   - Deployment ready

✅ 4. BEST PRACTICES
   - Dependency injection
   - Clean architecture
   - Repository pattern

✅ 5. PERFECT FOR:
   - REST APIs
   - Microservices
   - ML deployment
   - Real-time apps


NEXT STEPS:
===========
1. Build complete Payroll API
2. Integrate dengan Repository Pattern
3. Add authentication
4. Add database
5. Deploy to cloud

Let's build production-ready API! 🚀
"""

if __name__ == "__main__":
    print("FastAPI Theory - Hari 3 Bagian B")
    print("Baca code ini untuk memahami FastAPI concepts!")
    print("\nNext: Lihat implementasi actual di folder 02_fastapi_basics/")
