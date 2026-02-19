# ================================================================
# 📘 HARI 3: REPOSITORY PATTERN & FASTAPI
# ================================================================

Materi advanced backend development dengan Python: Repository Pattern dan FastAPI

## 🎯 Tujuan Pembelajaran

Setelah menyelesaikan Hari 3, Anda akan memahami:

1. **Repository Pattern**
   - ✅ Apa itu Data Layer dan mengapa penting
   - ✅ Anti-pattern yang sering dilakukan pemula
   - ✅ Cara implementasi Repository Pattern
   - ✅ Manfaat: Testability, Replaceability, Maintainability
   - ✅ Kapan menggunakan dan tidak menggunakan pattern ini

2. **FastAPI Framework**
   - ✅ Modern Python web framework dengan performa tinggi
   - ✅ Automatic validation via Pydantic
   - ✅ Automatic API documentation (Swagger UI + ReDoc)
   - ✅ Dependency Injection pattern
   - ✅ Clean Architecture implementation

3. **Production-Ready Practices**
   - ✅ Clean Architecture (separation of concerns)
   - ✅ SOLID Principles (especially Dependency Inversion)
   - ✅ Error handling strategies
   - ✅ API versioning
   - ✅ Middleware (CORS, timing)
   - ✅ Code yang testable dan maintainable

## 📁 Struktur Materi

```
Hari3/
│
├── 01_repository_pattern/          # Repository Pattern Deep Dive
│   ├── theory.py                   # ⭐ Teori + anti-patterns + design principles
│   ├── repositories.py             # 4 implementasi (CSV, SQLite, JSON, Mock)
│   ├── services.py                 # Business logic dengan Repository
│   └── demo.py                     # 5 demo scenarios lengkap
│
├── 02_fastapi_basics/              # FastAPI Comprehensive Guide
│   └── fastapi_theory.py           # ⭐ Semua tentang FastAPI (600+ baris)
│
├── 03_mini_project_payroll_api/    # 🚀 Complete REST API Project
│   ├── app/
│   │   ├── main.py                 # FastAPI application
│   │   ├── schemas.py              # Pydantic validation schemas
│   │   ├── repositories.py         # Data access layer
│   │   ├── services.py             # Business logic layer
│   │   └── routers.py              # API endpoints
│   ├── requirements.txt            # Dependencies
│   ├── RUN_API.py                  # Quick start script
│   └── README.md                   # Project documentation
│
└── README.md                       # 📖 Anda di sini!
```

## 🚀 Quick Start

### Part A: Repository Pattern

```bash
# 1. Baca teori Repository Pattern
python Hari3/01_repository_pattern/theory.py

# 2. Lihat implementasi 4 repositories
python Hari3/01_repository_pattern/repositories.py

# 3. Jalankan demo lengkap (5 scenarios)
python Hari3/01_repository_pattern/demo.py
```

### Part B: FastAPI Theory

```bash
# Baca comprehensive FastAPI guide
python Hari3/02_fastapi_basics/fastapi_theory.py
```

### Part C: Mini Project (Payroll API)

```bash
# Navigate ke project folder
cd Hari3/03_mini_project_payroll_api/

# Install dependencies
pip install -r requirements.txt

# Start API server
python RUN_API.py

# Buka browser: http://localhost:8000/docs
```

## 📚 Learning Path (Recommended Order)

### Step 1: Understand Repository Pattern (~2 hours)
1. Baca [theory.py](01_repository_pattern/theory.py) - Teori lengkap
2. Pelajari [repositories.py](01_repository_pattern/repositories.py) - 4 implementasi
3. Lihat [services.py](01_repository_pattern/services.py) - Business logic
4. Run [demo.py](01_repository_pattern/demo.py) - 5 demo scenarios

**Key Takeaways:**
- Repository abstraksi data access
- Business logic tidak tahu storage implementation
- Gampang testing dengan Mock repository
- Gampang migration (CSV → Database)

### Step 2: Learn FastAPI (~2 hours)
1. Baca [fastapi_theory.py](02_fastapi_basics/fastapi_theory.py) - Comprehensive guide
   - FastAPI vs Flask comparison
   - Pydantic validation
   - Dependency Injection
   - Automatic documentation
   - Routing & error handling

**Key Takeaways:**
- FastAPI = modern, fast, auto-documentation
- Pydantic = automatic validation (no manual checks!)
- Type hints = better IDE support + validation
- Dependency Injection = testable code

### Step 3: Build Real API (~3 hours)
1. Navigate ke [03_mini_project_payroll_api/](03_mini_project_payroll_api/)
2. Baca README.md untuk setup
3. Install dependencies: `pip install -r requirements.txt`
4. Explore code structure:
   - `schemas.py` - Data validation
   - `repositories.py` - Data access
   - `services.py` - Business logic
   - `routers.py` - API endpoints
   - `main.py` - Application config
5. Run API: `python RUN_API.py`
6. Test via Swagger UI: http://localhost:8000/docs

**Key Takeaways:**
- Clean Architecture in action
- Dependency Injection throughout
- Automatic validation & documentation
- Production-ready code structure

## 🎓 Key Concepts Mastery

### 1. Repository Pattern

**Problem:**
```python
# ❌ BAD: Business logic tahu storage details
def calculate_payroll():
    with open("employees.csv") as f:  # Tightly coupled!
        reader = csv.DictReader(f)
        for row in reader:
            # calculate...
```

**Solution:**
```python
# ✅ GOOD: Business logic uses abstraction
class PayrollService:
    def __init__(self, repository: IEmployeeRepository):
        self.repo = repository  # Depends on interface!
    
    def calculate_payroll(self):
        employees = self.repo.load()  # Don't care if CSV/SQLite/API
        # calculate...
```

**Benefits:**
- ✅ Testable (mock repository)
- ✅ Replaceable (swap CSV → Database)
- ✅ Maintainable (changes isolated)

### 2. Dependency Injection

**Problem:**
```python
# ❌ BAD: Service creates own dependencies
class PayrollService:
    def __init__(self):
        self.repo = EmployeeCSVRepository()  # Hard-coded!
```

**Solution:**
```python
# ✅ GOOD: Dependencies injected
def get_repository():
    return EmployeeCSVRepository("data.csv")

@app.post("/payroll/calculate")
async def calculate(
    service: PayrollService = Depends(get_payroll_service)
):
    # Service with injected repository!
    return service.calculate_payroll()
```

**Benefits:**
- ✅ Testable (inject mock in tests)
- ✅ Flexible (change implementation easily)
- ✅ Clear dependencies

### 3. Clean Architecture Layers

```
📱 Presentation Layer (Routers)
    ↓ Request
📋 Validation Layer (Schemas)
    ↓ Validated data
💼 Business Layer (Services)
    ↓ Commands
🗄️  Data Layer (Repositories)
    ↓ Queries
💾 Storage (Files/Database)
```

**Principles:**
- Each layer has ONE responsibility
- Inner layers don't know outer layers
- Dependencies point INWARD
- Business logic is independent of frameworks

### 4. Automatic Validation (Pydantic)

**Before Pydantic:**
```python
# ❌ Manual validation (100+ lines)
def create_employee(data: dict):
    if "email" not in data:
        raise ValueError("Email required")
    if "@" not in data["email"]:
        raise ValueError("Invalid email")
    if data["gaji"] < 3000000:
        raise ValueError("Salary too low")
    # ... more validation
```

**With Pydantic:**
```python
# ✅ Automatic validation (5 lines!)
class EmployeeCreate(BaseModel):
    email: EmailStr  # Auto email validation
    gaji: float = Field(..., gt=3000000)  # Auto range check
```

## 🔥 Mini Project Highlights

### API Features
- ✅ 9 REST endpoints (CRUD + payroll)
- ✅ Automatic request/response validation
- ✅ Interactive API documentation
- ✅ Error handling (400, 404, 422, 500)
- ✅ CORS enabled for frontend
- ✅ Request timing monitoring
- ✅ Health check endpoint

### Architecture Layers
1. **Routers** (routers.py): HTTP endpoints, request handling
2. **Schemas** (schemas.py): Data validation, API contracts
3. **Services** (services.py): Business logic, calculations
4. **Repositories** (repositories.py): Data access, storage abstraction
5. **Main** (main.py): App config, middleware, exception handlers

### Payroll Logic
- **Tax (PPh 21)**: 5% dari gaji kotor
- **Pension**: 2% dari gaji kotor
- **Health Insurance**: Rp 500,000 tetap
- **Net Salary**: Gross - (Tax + Pension + Health)

## 📊 API Endpoints

### Employee Management
```
GET    /employees                    # Get all employees
GET    /employees?departemen=IT      # Filter by department
GET    /employees/{emp_id}           # Get by ID
POST   /employees                    # Create employee
PUT    /employees/{emp_id}           # Update employee
DELETE /employees/{emp_id}           # Delete employee
GET    /employees/statistics/summary # Get statistics
```

### Payroll Processing
```
POST   /payroll/calculate                  # Calculate all payrolls
GET    /payroll/department/{departemen}    # Department payroll
```

### Utility
```
GET    /              # API info
GET    /health        # Health check
```

## 🧪 Testing Examples

### Using curl
```bash
# Create employee
curl -X POST "http://localhost:8000/employees" \
  -H "Content-Type: application/json" \
  -d '{"id":"EMP001","nama":"Tomas","email":"t@ex.com","departemen":"IT","gaji":10000000,"join_date":"2020-01-01"}'

# Calculate payroll
curl -X POST "http://localhost:8000/payroll/calculate"
```

### Using Python
```python
import requests

# Create employee
data = {
    "id": "EMP001",
    "nama": "Tomas Anderson",
    "email": "tomas@techcorp.com",
    "departemen": "Engineering",
    "gaji": 15000000,
    "join_date": "2020-01-15"
}
response = requests.post("http://localhost:8000/employees", json=data)
print(response.json())
```

## 🎯 What Makes This Production-Ready?

### 1. Proper Error Handling
```python
@app.exception_handler(ValueError)
async def value_error_handler(request, exc):
    return JSONResponse(
        status_code=400,
        content={"detail": str(exc)}
    )
```

### 2. Request Validation
```python
class EmployeeCreate(BaseModel):
    gaji: float = Field(..., gt=3000000)
    
    @validator('gaji')
    def validate_minimum_wage(cls, v):
        if v < 3000000:
            raise ValueError("Salary below minimum")
        return v
```

### 3. Response Models
```python
@router.post("/employees", response_model=EmployeeResponse, status_code=201)
async def create_employee(employee: EmployeeCreate):
    # Automatic response validation!
    return service.create_employee(employee.dict())
```

### 4. Dependency Injection
```python
def get_employee_service(repo = Depends(get_repository)):
    return EmployeeService(repo)

# Easy to test with mock!
```

### 5. Middleware
```python
# CORS for frontend
app.add_middleware(CORSMiddleware, allow_origins=["*"])

# Request timing
@app.middleware("http")
async def add_process_time_header(request, call_next):
    # Add X-Process-Time header
```

### 6. Documentation
```python
app = FastAPI(
    title="Payroll Management API",
    description="""
    Complete payroll API with:
    - Employee CRUD
    - Payroll calculation
    - Department reports
    """,
    version="1.0.0"
)
```

## 🚀 Next Steps & Advanced Topics

### Immediate Enhancements
1. **Database**: Add SQLite/PostgreSQL support
2. **Authentication**: JWT tokens, OAuth2
3. **Testing**: Unit tests with pytest + TestClient
4. **Logging**: Structured logging
5. **Docker**: Containerization

### Production Deployment
1. **Environment Config**: Use .env files
2. **Database Migrations**: Alembic
3. **Rate Limiting**: Prevent abuse
4. **Caching**: Redis for performance
5. **Monitoring**: Prometheus + Grafana
6. **CI/CD**: GitHub Actions

### Architecture Extensions
1. **CQRS**: Separate read/write models
2. **Event Sourcing**: Track all changes
3. **Message Queue**: Async processing (Celery)
4. **Microservices**: Split into services
5. **API Gateway**: Kong/Nginx

## 📖 Additional Resources

### Official Documentation
- [FastAPI Docs](https://fastapi.tiangolo.com/)
- [Pydantic Docs](https://docs.pydantic.dev/)
- [SQLAlchemy](https://www.sqlalchemy.org/)

### Design Patterns
- Repository Pattern
- Dependency Injection
- Clean Architecture (Uncle Bob)
- SOLID Principles

### Best Practices
- [12-Factor Apps](https://12factor.net/)
- [REST API Design](https://restfulapi.net/)
- [Python Type Hints](https://docs.python.org/3/library/typing.html)

## ✅ Learning Checklist

Copy checklist ini untuk tracking progress Anda:

### Repository Pattern
- [ ] Memahami konsep Data Layer
- [ ] Memahami anti-patterns yang sering terjadi
- [ ] Implementasi abstract interface
- [ ] Implementasi concrete repositories (CSV, SQLite)
- [ ] Implementasi Mock repository untuk testing
- [ ] Memahami manfaat: Testability, Replaceability
- [ ] Run semua demo scenarios

### FastAPI
- [ ] Memahami FastAPI vs Flask
- [ ] Install dan setup FastAPI + Uvicorn
- [ ] Membuat Pydantic schemas
- [ ] Implementasi routing (GET, POST, PUT, DELETE)
- [ ] Dependency Injection pattern
- [ ] Error handling dan validation
- [ ] Automatic documentation (Swagger UI)
- [ ] Middleware (CORS, timing)

### Mini Project
- [ ] Clone dan setup project
- [ ] Memahami struktur Clean Architecture
- [ ] Read & understand semua layer (schemas, repos, services, routers)
- [ ] Run API server
- [ ] Test via Swagger UI
- [ ] Test via curl/Python requests
- [ ] Modify dan extend API (add endpoint)
- [ ] Switch repository (CSV → Mock)

### Production Skills
- [ ] Error handling strategies
- [ ] Request/Response validation
- [ ] API documentation best practices
- [ ] Testing strategies (unit, integration)
- [ ] Deployment considerations

## 🎓 Summary

**Apa yang Anda pelajari:**

1. **Repository Pattern**: Abstraksi data access untuk code yang testable dan maintainable
2. **FastAPI**: Modern web framework dengan auto-validation dan documentation
3. **Clean Architecture**: Separation of concerns dengan layer yang jelas
4. **Dependency Injection**: Pattern untuk code yang flexible dan testable
5. **Production Practices**: Error handling, validation, documentation, middleware

**Skills yang Anda kuasai:**

- ✅ Advanced OOP (Abstract Base Classes, interfaces)
- ✅ Design Patterns (Repository, Dependency Injection)
- ✅ Clean Architecture implementation
- ✅ REST API development dengan FastAPI
- ✅ Automatic validation dengan Pydantic
- ✅ Type hints dan modern Python
- ✅ Production-ready code structure

**Project yang bisa Anda tunjukkan:**

Payroll Management API - Complete REST API dengan:
- 9 endpoints (CRUD + business logic)
- Clean Architecture (4 layers)
- Automatic documentation
- Production-ready patterns
- Testable & maintainable code

---

## 💬 Questions?

Explore code dengan membaca comments di setiap file. Setiap file punya penjelasan detail tentang:
- Why: Mengapa pattern ini digunakan
- How: Bagaimana implementasinya
- When: Kapan sebaiknya digunakan
- Alternatives: Pilihan lain dan trade-offs

**Happy Learning! 🚀**

Dari Beginner → Professional Python Backend Developer dalam 3 hari!

---

*Materi ini dibuat dengan fokus pada production-ready code, bukan just working code.*
