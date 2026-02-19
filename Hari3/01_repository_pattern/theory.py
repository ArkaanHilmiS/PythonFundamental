"""
========================================================================
HARI 3 - BAGIAN A: FILE / DATA LAYER YANG "REAL"
REPOSITORY PATTERN - THE PROFESSIONAL WAY
========================================================================

Materi ini mengajarkan cara profesional mengelola data layer yang:
✅ Production-ready
✅ Testable
✅ Maintainable
✅ Scalable
"""

# ========================================================================
# 1. APA ITU DATA LAYER?
# ========================================================================

"""
DATA LAYER adalah lapisan yang bertanggung jawab untuk:
1. Menyimpan data (CRUD operations)
2. Mengambil data dari storage
3. Mengubah format data
4. Mengisolasi sumber data dari business logic

ANALOGY (Real World):
===================

Bayangkan sebuah Restaurant:

┌─────────────────────────────────────────────────────┐
│  CUSTOMER (User Interface)                           │
│  "Saya mau Nasi Goreng"                             │
└──────────────────┬──────────────────────────────────┘
                   │
                   ▼
┌─────────────────────────────────────────────────────┐
│  WAITER (Business Logic / Service)                   │
│  - Terima order                                      │
│  - Validasi menu ada atau tidak                     │
│  - Hitung harga total                               │
│  - Kirim ke kitchen                                 │
└──────────────────┬──────────────────────────────────┘
                   │
                   ▼
┌─────────────────────────────────────────────────────┐
│  CHEF (Repository / Data Layer)                      │
│  - Ambil bahan dari storage                         │
│  - Masak                                            │
│  - Return makanan                                   │
└──────────────────┬──────────────────────────────────┘
                   │
                   ▼
┌─────────────────────────────────────────────────────┐
│  WAREHOUSE (Storage: CSV / Database / Cloud)         │
│  - Tempat nyimpan bahan makanan                     │
└─────────────────────────────────────────────────────┘

KEY POINT:
• Customer TIDAK PERLU TAHU bahan dari mana
• Waiter TIDAK PERLU TAHU cara masak
• Chef fokus ke data, bukan business rule

Ini adalah SEPARATION OF CONCERNS!
"""


# ========================================================================
# 2. MASALAH UMUM PEMULA (ANTI-PATTERN ❌)
# ========================================================================

"""
❌ ANTI-PATTERN #1: Business Logic Urus Data Langsung
=====================================================
"""

# ❌ BAD: Service langsung akses file
class PayrollServiceBad:
    def process_payroll(self):
        # Business logic TERCAMPUR dengan file handling
        with open("employees.csv") as f:
            employees = []
            for line in f:
                # Parse CSV manual
                id, nama, gaji = line.strip().split(",")
                
                # Business logic
                gaji_bersih = float(gaji) * 0.95  # Tax 5%
                
                employees.append({
                    "id": id,
                    "nama": nama,
                    "gaji_bersih": gaji_bersih
                })
        
        # Save hasil
        with open("payroll_result.csv", "w") as f:
            for emp in employees:
                f.write(f"{emp['id']},{emp['nama']},{emp['gaji_bersih']}\n")
        
        return employees

"""
MASALAH dari code di atas:

1. ❌ TIGHT COUPLING
   - Service terikat ke CSV file
   - Mau ganti ke database? Harus ubah semua

2. ❌ NOT TESTABLE
   - Harus buat file CSV nyata untuk test
   - Tidak bisa mock data

3. ❌ HARD TO MAINTAIN
   - File handling logic campur aduk
   - Susah debug

4. ❌ NOT SCALABLE
   - Mau tambah source data lain? Refactor besar
   - Tidak bisa parallel development

5. ❌ VIOLATES SOLID PRINCIPLES
   - Single Responsibility: Service urus terlalu banyak
   - Open/Closed: Tidak bisa extend tanpa modify
   - Dependency Inversion: Depend on concrete, bukan abstraction
"""


# ========================================================================
# 3. PRINSIP DESAIN DATA LAYER (WAJIB!) ✅
# ========================================================================

"""
🔑 PRINSIP #1: SEPARATION OF CONCERNS
====================================

Setiap layer punya tanggung jawab spesifik:

┌────────────────────────────────────────┐
│  PRESENTATION LAYER (API/UI)           │  ← Handle HTTP, JSON, user input
├────────────────────────────────────────┤
│  BUSINESS LOGIC LAYER (Service)        │  ← Business rules, calculations
├────────────────────────────────────────┤
│  DATA ACCESS LAYER (Repository)        │  ← CRUD operations only
├────────────────────────────────────────┤
│  DATA STORAGE (DB/File/Cloud)          │  ← Actual storage
└────────────────────────────────────────┘

RULES:
• Presentation NEVER access Repository directly
• Business Logic NEVER know about storage details
• Repository NEVER have business rules


🔑 PRINSIP #2: ABSTRACTION
=========================

Business logic hanya tahu INTERFACE, bukan IMPLEMENTATION:

Business Logic says:
"Give me all employees" ← Interface

Repository implements:
- From CSV file
- From SQLite
- From PostgreSQL
- From REST API
- From Cloud Storage

Business Logic TIDAK PEDULI implementation mana yang dipakai!


🔑 PRINSIP #3: REPLACEABLE (Dependency Inversion)
=================================================

Kamu harus bisa ganti repository tanpa ubah business logic:

# Today: CSV
service = PayrollService(EmployeeCSVRepository("data.csv"))

# Tomorrow: Database (NO CODE CHANGE!)
service = PayrollService(EmployeeSQLiteRepository("data.db"))

# Next week: Cloud (NO CODE CHANGE!)
service = PayrollService(EmployeeFirestoreRepository("project-id"))


🔑 PRINSIP #4: TESTABLE
=======================

Dengan repository pattern, testing jadi mudah:

# Production: Real database
real_repo = EmployeeSQLiteRepository("prod.db")
service = PayrollService(real_repo)

# Testing: Mock data (NO DATABASE NEEDED!)
mock_repo = MockEmployeeRepository([
    {"id": "EMP001", "nama": "Test", "gaji": 5000000}
])
service = PayrollService(mock_repo)
"""


# ========================================================================
# 4. REPOSITORY PATTERN - THE SOLUTION! ✅
# ========================================================================

"""
REPOSITORY PATTERN adalah design pattern untuk:
• Encapsulate data access logic
• Provide clean API untuk business logic
• Enable testing dengan mock data
• Allow multiple implementations

STRUCTURE:
==========

┌─────────────────────────────────────────────────────────┐
│  IEmployeeRepository (Interface/Abstract)                │
│  ├── load() -> List[Employee]                           │
│  ├── save(employees) -> None                            │
│  ├── get_by_id(id) -> Employee                          │
│  └── delete(id) -> None                                 │
└──────────────┬──────────────────────────────────────────┘
               │
               │ Implements
               ├──────────────────────────────────────┐
               │                                      │
┌──────────────▼────────────┐      ┌─────────────────▼────────────┐
│  CSVRepository             │      │  SQLiteRepository             │
│  - load_from_csv()         │      │  - load_from_db()            │
│  - save_to_csv()           │      │  - save_to_db()              │
└────────────────────────────┘      └──────────────────────────────┘


BENEFITS:
=========

✅ 1. CLEAN BUSINESS LOGIC
--------------------------
# Business logic fokus ke business rules
class PayrollService:
    def __init__(self, repo):
        self.repo = repo  # Any repository!
    
    def calculate_payroll(self):
        employees = self.repo.load()  # Abstraction!
        
        # Pure business logic
        for emp in employees:
            emp.net_salary = emp.gross_salary * 0.95
        
        self.repo.save(employees)  # Abstraction!


✅ 2. EASY TO TEST
------------------
# Test dengan mock data, tidak butuh file/database
mock_repo = MockRepository([{"id": "EMP001", "gaji": 5000000}])
service = PayrollService(mock_repo)

result = service.calculate_payroll()
assert result[0]["net_salary"] == 4750000  # ✓ Pass!


✅ 3. EASY TO MIGRATE
---------------------
# Switch dari CSV ke Database:
# BEFORE
repo = EmployeeCSVRepository("data.csv")

# AFTER (Business logic code TIDAK BERUBAH!)
repo = EmployeeSQLiteRepository("data.db")

service = PayrollService(repo)  # Same code!


✅ 4. PARALLEL DEVELOPMENT
--------------------------
Team A: Develop business logic dengan mock repository
Team B: Develop real database repository
Team C: Develop API layer

Semua bisa jalan parallel tanpa blocking!


✅ 5. MULTIPLE DATA SOURCES
---------------------------
# Employee dari database
emp_repo = EmployeeSQLiteRepository("hr.db")

# Attendance dari API
attendance_repo = AttendanceAPIRepository("https://api.company.com")

# Payroll calculation combine both
service = PayrollService(emp_repo, attendance_repo)
"""


# ========================================================================
# 5. KAPAN PAKAI REPOSITORY PATTERN?
# ========================================================================

"""
✅ PAKAI REPOSITORY PATTERN WHEN:
=================================

1. ✅ Project akan berkembang besar
2. ✅ Perlu testing yang solid
3. ✅ Data source mungkin berubah (CSV → DB → Cloud)
4. ✅ Multiple data sources
5. ✅ Team collaboration
6. ✅ Production-grade application

❌ TIDAK PERLU REPOSITORY PATTERN WHEN:
========================================

1. ❌ Script sederhana one-time use
2. ❌ Prototype quick & dirty
3. ❌ Data source 100% tidak akan berubah
4. ❌ Solo project yang sangat kecil

RULE OF THUMB:
=============
"Jika code ini akan dipakai production atau dikembangkan team,
 ALWAYS gunakan Repository Pattern!"
"""


# ========================================================================
# 6. KESIMPULAN
# ========================================================================

"""
DATA LAYER / REPOSITORY PATTERN adalah:
✅ WAJIB untuk production code
✅ BEST PRACTICE yang dipakai di industry
✅ FUNDAMENTAL untuk clean architecture
✅ KEY SKILL yang dicari employer

REMEMBER:
• Separate data access from business logic
• Code to interface, not implementation
• Make it testable
• Make it replaceable

NEXT:
Kita akan implement Repository Pattern dengan:
1. CSV Repository (File-based)
2. SQLite Repository (Database)
3. Mock Repository (Testing)
4. Integrate dengan FastAPI

Let's build production-grade code! 🚀
"""

if __name__ == "__main__":
    print("Repository Pattern Theory - Hari 3")
    print("Baca code ini dengan teliti untuk memahami konsep!")
    print("\nNext: Lihat repositories.py untuk implementasi nyata")
