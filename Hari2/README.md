# HRMS - Human Resource Management System
## Modular Version - Separated by Classes and Features

Sistem manajemen sumber daya manusia yang komprehensif dengan struktur modular.

---

## 📁 Struktur Project

```
Hari2/
├── models/                     # Model classes
│   ├── __init__.py            # Package initializer
│   ├── person.py              # Base Person class
│   ├── employee.py            # Base Employee class (abstract)
│   ├── full_time_employee.py  # Full-time employee dengan benefits
│   ├── contract_employee.py   # Contract employee dengan durasi kontrak
│   ├── intern.py              # Intern dengan program magang
│   └── department.py          # Department management
│
├── systems/                    # System classes
│   ├── __init__.py            # Package initializer
│   ├── payroll_system.py      # Payroll processing system
│   └── hr_system.py           # Main HR management system
│
├── main.py                     # Demo program
└── README.md                   # Dokumentasi (file ini)
```

---

## 🎯 Fitur Utama

### 1. **Employee Management**
- Tiga tipe karyawan: Full-time, Contract, Intern
- Employee information tracking
- Tenure calculation
- Search by department/position

### 2. **Performance Management**
- Performance rating system (1-5 scale)
- Average rating calculation
- Performance bonus based on rating

### 3. **Leave Management**
- Annual leave & sick leave
- Leave request workflow
- Leave approval system
- Balance tracking

### 4. **Attendance System**
- Clock in/out functionality
- Hours worked calculation
- Monthly attendance summary
- Attendance bonus

### 5. **Payroll System**
- Automated salary calculation
- Grade-based bonuses
- Performance bonuses
- Tenure bonuses
- Tax & pension deductions
- Payslip generation

### 6. **Department Management**
- Department creation & management
- Employee assignment
- Budget allocation
- Department payroll calculation

---

## 🔧 Cara Menggunakan

### Menjalankan Demo Program

Dari direktori `PythonFundamental`:

```bash
python Hari2/main.py
```

### Import Modules dalam Project Sendiri

```python
# Import models
from models import (
    Person,
    Employee,
    FullTimeEmployee,
    ContractEmployee,
    Intern,
    Department
)

# Import systems
from systems import (
    PayrollSystem,
    HRManagementSystem
)
```

---

## 💡 Contoh Penggunaan

### 1. Membuat HR System

```python
from systems import HRManagementSystem

hrms = HRManagementSystem("TechCorp Solutions")
```

### 2. Membuat Department

```python
from models import Department

dept_it = Department("DEPT001", "Information Technology")
dept_it.budget = 500000000
hrms.add_department(dept_it)
```

### 3. Membuat Full-Time Employee

```python
from models import FullTimeEmployee

emp = FullTimeEmployee(
    emp_id="EMP001",
    name="John Doe",
    email="john@company.com",
    phone="081234567890",
    date_of_birth="1990-05-15",
    join_date="2020-01-15",
    department="Information Technology",
    base_salary=15000000,
    position="Senior Software Engineer",
    grade="Senior"
)

hrms.add_employee(emp)
dept_it.add_employee(emp)
```

### 4. Menambah Performance Rating

```python
emp.add_performance_rating(
    rating=4.5,
    review_date="2024-12-31",
    reviewer="Manager Name",
    comments="Excellent performance"
)
```

### 5. Request & Approve Leave

```python
# Request leave
emp.request_leave(
    leave_type="annual",
    start_date="2024-03-15",
    end_date="2024-03-20",
    reason="Family vacation"
)

# Approve leave (index 0 = first leave request)
emp.approve_leave(0)
```

### 6. Clock In/Out

```python
from datetime import datetime

# Clock in
emp.clock_in()

# Clock out (beberapa jam kemudian)
emp.clock_out()

# Atau dengan waktu spesifik
emp.clock_in(datetime(2024, 2, 15, 9, 0, 0))
emp.clock_out(datetime(2024, 2, 15, 18, 0, 0))
```

### 7. Generate Payslip

```python
payslip = hrms.payroll_system.generate_payslip(
    employee=emp,
    period_month=2,
    period_year=2024
)

print(hrms.payroll_system.print_payslip(payslip))
```

### 8. Company Reports

```python
# Department summary
print(dept_it.get_department_summary())

# Company-wide report
print(hrms.generate_company_report())

# Employee information
print(emp.get_info())
```

---

## 📊 Salary Calculation

### Full-Time Employee
- **Base Salary**: Gaji pokok
- **Grade Bonus**:
  - Junior: Rp 0
  - Mid: Rp 2,000,000
  - Senior: Rp 5,000,000
  - Lead: Rp 8,000,000
- **Performance Bonus**:
  - Rating ≥ 4.5: 20% of base
  - Rating ≥ 4.0: 15% of base
  - Rating ≥ 3.5: 10% of base
- **Tenure Bonus**: 1% per year (max 10%)
- **Deductions**:
  - Pension: 5% of gross
  - Tax: 5% of gross

### Contract Employee
- Fixed monthly atau hourly rate
- No benefits
- No bonus
- No deductions

### Intern
- Fixed stipend
- No benefits
- No bonus
- No deductions

---

## 🎓 Konsep OOP yang Diimplementasikan

### 1. **Class & Objects**
Setiap entitas (Person, Employee, Department) adalah class dengan attributes dan methods.

### 2. **Inheritance**
```
Person (base class)
└── Employee (inherits from Person)
    ├── FullTimeEmployee (inherits from Employee)
    ├── ContractEmployee (inherits from Employee)
    └── Intern (inherits from Employee)
```

### 3. **Encapsulation**
- Data dan methods dikemas dalam class
- Information hiding dengan private/protected attributes

### 4. **Polymorphism**
- Method `calculate_salary()` diimplementasikan berbeda untuk setiap tipe employee
- Method overriding dalam subclasses

### 5. **Abstraction**
- `Employee.calculate_salary()` adalah abstract method
- Harus diimplementasikan oleh semua subclasses

### 6. **Composition**
- `HRManagementSystem` menggunakan `PayrollSystem`
- `Department` memiliki collection of `Employee` objects

---

## 🚀 Extensibility

System ini mudah dikembangkan dengan menambahkan:

1. **New Employee Types**
   ```python
   class PartTimeEmployee(Employee):
       def calculate_salary(self):
           # Implementation
           pass
   ```

2. **New Systems**
   ```python
   class TrainingSystem:
       def schedule_training(self, employee, course):
           # Implementation
           pass
   ```

3. **New Features**
   - Database integration (SQLAlchemy)
   - REST API (FastAPI/Flask)
   - Web interface (Django/React)
   - Email notifications
   - Report generation (PDF)
   - Analytics dashboard

---

## 📝 Requirements

- Python 3.7+
- Standard library only (no external dependencies)

---

## 👨‍💻 Code Style

- PEP 8 compliant
- Docstrings untuk semua classes dan methods
- Type hints (optional, bisa ditambahkan)
- Bilingual comments (Indonesian + English)

---

## 🔒 Best Practices

1. **Separation of Concerns**: Models, systems, dan business logic terpisah
2. **Single Responsibility**: Setiap class memiliki satu tanggung jawab utama
3. **DRY (Don't Repeat Yourself)**: Base classes untuk shared functionality
4. **Clear Naming**: Variable dan method names yang descriptive
5. **Modular Design**: Easy to extend dan maintain

---

## 📚 Learning Path

File ini adalah bagian dari **Day 2: OOP** dalam Python learning series:

- **Day 1**: Python Fundamentals (`hari1_fundamental.py`)
- **Day 2**: OOP Concepts (`hari2_oop.py`)
- **Day 2**: OOP Implementation - HRMS (this project)

---

## 📄 License

Educational project - Free to use and modify

---

## 👤 Author

Part of Python Fundamental Learning Series
Created for comprehensive OOP understanding with real-world implementation

---

## 📮 Contact & Support

Untuk pertanyaan atau feedback, silakan buat issue atau hubungi instructor.

---

**Happy Coding! 🚀**
