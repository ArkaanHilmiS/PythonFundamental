"""
========================================================================
PAYROLL API - Main Application
FastAPI Application dengan Clean Architecture
========================================================================
"""

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import time

from app.routers import employee_router, payroll_router


# ========================================================================
# CREATE FASTAPI APP
# ========================================================================

app = FastAPI(
    title="Payroll Management API",
    description="""
    ## Payroll Management System API
    
    Modern REST API untuk Employee dan Payroll Management.
    
    ### Features:
    * **Employee Management**: CRUD operations untuk employees
    * **Payroll Calculation**: Automatic payroll calculation dengan deductions
    * **Department Reports**: Payroll reports per department
    * **Statistics**: Employee dan salary statistics
    
    ### Architecture:
    * **Clean Architecture**: Separation of concerns
    * **Repository Pattern**: Abstracted data access
    * **Dependency Injection**: Testable dan maintainable
    * **Automatic Validation**: Pydantic schemas
    * **Auto Documentation**: Swagger UI dan ReDoc
    
    ### Tech Stack:
    * FastAPI (Modern Python web framework)
    * Pydantic (Data validation)
    * CSV/SQLite (Data storage)
    
    Built with ❤️ using FastAPI
    """,
    version="1.0.0",
    contact={
        "name": "Tech Corp",
        "email": "api@techcorp.com"
    },
    license_info={
        "name": "MIT License",
        "url": "https://opensource.org/licenses/MIT"
    }
)


# ========================================================================
# MIDDLEWARE
# ========================================================================

# CORS Middleware (untuk frontend integration)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, specify allowed origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Request timing middleware
@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    """Add X-Process-Time header untuk monitoring."""
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response


# ========================================================================
# EXCEPTION HANDLERS
# ========================================================================

@app.exception_handler(ValueError)
async def value_error_handler(request: Request, exc: ValueError):
    """Handle ValueError exceptions."""
    return JSONResponse(
        status_code=400,
        content={
            "error": "Validation Error",
            "detail": str(exc)
        }
    )


@app.exception_handler(Exception)
async def general_exception_handler(request: Request, exc: Exception):
    """Handle general exceptions."""
    return JSONResponse(
        status_code=500,
        content={
            "error": "Internal Server Error",
            "detail": "An unexpected error occurred"
        }
    )


# ========================================================================
# INCLUDE ROUTERS
# ========================================================================

app.include_router(employee_router)
app.include_router(payroll_router)


# ========================================================================
# ROOT ENDPOINTS
# ========================================================================

@app.get(
    "/",
    tags=["Root"],
    summary="API Root",
    description="Welcome endpoint"
)
async def root():
    """
    API Root endpoint.
    
    Returns welcome message dan available endpoints.
    """
    return {
        "message": "Welcome to Payroll Management API",
        "version": "1.0.0",
        "docs": "/docs",
        "redoc": "/redoc",
        "endpoints": {
            "employees": {
                "list": "GET /employees",
                "get": "GET /employees/{emp_id}",
                "create": "POST /employees",
                "update": "PUT /employees/{emp_id}",
                "delete": "DELETE /employees/{emp_id}",
                "statistics": "GET /employees/statistics/summary"
            },
            "payroll": {
                "calculate": "POST /payroll/calculate",
                "department": "GET /payroll/department/{departemen}"
            }
        },
        "architecture": {
            "pattern": "Repository Pattern",
            "layers": ["Routers", "Services", "Repositories"],
            "principles": ["Clean Architecture", "Dependency Injection", "SOLID"]
        }
    }


@app.get(
    "/health",
    tags=["Root"],
    summary="Health Check",
    description="Check API health status"
)
async def health_check():
    """
    Health check endpoint.
    
    Use this untuk monitoring dan load balancer health checks.
    """
    return {
        "status": "healthy",
        "timestamp": time.time()
    }


# ========================================================================
# STARTUP & SHUTDOWN EVENTS
# ========================================================================

@app.on_event("startup")
async def startup_event():
    """Runs on application startup."""
    print("="*70)
    print("PAYROLL API - STARTING UP")
    print("="*70)
    print(f"Title: {app.title}")
    print(f"Version: {app.version}")
    print(f"Docs: http://localhost:8000/docs")
    print(f"ReDoc: http://localhost:8000/redoc")
    print("="*70)


@app.on_event("shutdown")
async def shutdown_event():
    """Runs on application shutdown."""
    print("="*70)
    print("PAYROLL API - SHUTTING DOWN")
    print("="*70)


# ========================================================================
# MAIN (For development)
# ========================================================================

if __name__ == "__main__":
    import uvicorn
    
    print("""
    ╔══════════════════════════════════════════════════════════════════╗
    ║         PAYROLL MANAGEMENT API - DEVELOPMENT SERVER             ║
    ╚══════════════════════════════════════════════════════════════════╝
    """)
    
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,  # Auto-reload on code changes
        log_level="info"
    )
