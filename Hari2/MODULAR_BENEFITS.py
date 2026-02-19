"""
MODULAR STRUCTURE BENEFITS - Keuntungan Struktur Modular
==========================================================

File ini menjelaskan mengapa memisahkan code menjadi modul-modul terpisah 
adalah best practice dalam software development.
"""

# ============================================================================
# 1. SEPARATION OF CONCERNS (Pemisahan Tanggung Jawab)
# ============================================================================

"""
Setiap file memiliki tanggung jawab spesifik:

SEBELUM (Single File):
- hari2_oop_implementation.py (1000+ lines)
  └── Semua class, system, dan demo dalam 1 file

SESUDAH (Modular):
- models/person.py (30 lines) - Hanya Person class
- models/employee.py (200 lines) - Hanya Employee base class
- models/full_time_employee.py (60 lines) - Hanya FullTimeEmployee
- models/contract_employee.py (50 lines) - Hanya ContractEmployee
- models/intern.py (50 lines) - Hanya Intern
- models/department.py (60 lines) - Hanya Department
- systems/payroll_system.py (80 lines) - Hanya Payroll logic
- systems/hr_system.py (100 lines) - Hanya HR management logic
- main.py (150 lines) - Hanya demo/application

KEUNTUNGAN:
✓ Mudah menemukan code yang dicari
✓ Fokus pada satu masalah saat edit
✓ Tidak overwhelmed dengan code yang terlalu banyak
"""


# ============================================================================
# 2. MAINTAINABILITY (Kemudahan Maintenance)
# ============================================================================

"""
Misal ada bug di payroll calculation:

SEBELUM:
1. Buka file 1000 lines
2. Scroll mencari PayrollSystem class
3. Find method calculate_salary
4. Fix bug
5. Risk: Accidentally modify code lain

SESUDAH:
1. Langsung buka systems/payroll_system.py (80 lines)
2. Method langsung terlihat
3. Fix bug
4. Save
✓ Tidak ada risk modify code lain

Real Case:
"Bug: Performance bonus tidak dihitung dengan benar"
- Langsung tau: full_time_employee.py, method calculate_salary()
- Edit 1 file, 60 lines total
- Done in 2 minutes
"""


# ============================================================================
# 3. REUSABILITY (Kemampuan Menggunakan Ulang)
# ============================================================================

"""
Misal ingin membuat project baru: Sales Management System

TANPA MODULAR:
- Copy-paste 1000 lines
- Hapus yang tidak perlu
- Modify yang perlu
- High risk error

DENGAN MODULAR:
from models.person import Person  # Reuse Person class
from models.employee import Employee  # Reuse Employee base

class SalesPerson(Employee):
    def calculate_commission(self):
        # New functionality
        pass

✓ Import only what you need
✓ No copy-paste
✓ Consistent base classes
"""


# ============================================================================
# 4. TEAM COLLABORATION (Kolaborasi Tim)
# ============================================================================

"""
Scenario: Tim dengan 3 developer

SINGLE FILE (hari2_oop_implementation.py):
Developer A: Edit line 100-200 (Person class)
Developer B: Edit line 500-600 (Payroll)
Developer C: Edit line 800-900 (Department)

Problem:
- Semua edit file yang sama
- Git merge conflicts
- Saling tunggu untuk commit
- Risk overwrite code orang lain

MODULAR FILES:
Developer A: Edit models/person.py
Developer B: Edit systems/payroll_system.py
Developer C: Edit models/department.py

Benefit:
✓ Edit file berbeda
✓ No merge conflicts
✓ Parallel work
✓ Independent commits
✓ Faster development

Git Log akan terlihat seperti:
commit abc123 "Add person validation" - models/person.py
commit def456 "Fix payroll tax" - systems/payroll_system.py
commit ghi789 "Add department budget" - models/department.py
"""


# ============================================================================
# 5. TESTING (Pengujian yang Lebih Mudah)
# ============================================================================

"""
TESTING SINGLE FILE:
tests/test_oop_implementation.py
- Import all classes
- Test all features
- 1 file, 500+ lines tests
- Slow to run

TESTING MODULAR:
tests/
├── test_person.py          # Test Person only
├── test_employee.py        # Test Employee only
├── test_full_time.py       # Test FullTimeEmployee only
├── test_payroll.py         # Test PayrollSystem only
└── test_hr_system.py       # Test HRSystem only

Benefits:
✓ Run only failed tests
✓ Fast feedback
✓ Isolated testing
✓ Clear test organization

Example:
$ pytest tests/test_payroll.py  # Only test payroll
$ pytest tests/test_person.py   # Only test person
$ pytest                         # Run all tests
"""


# ============================================================================
# 6. DEPENDENCY MANAGEMENT (Manajemen Ketergantungan)
# ============================================================================

"""
Dependency Tree:

main.py
├── models/
│   ├── person.py (no dependencies)
│   ├── employee.py (depends on: person.py)
│   ├── full_time_employee.py (depends on: employee.py)
│   ├── contract_employee.py (depends on: employee.py)
│   ├── intern.py (depends on: employee.py)
│   └── department.py (no dependencies)
└── systems/
    ├── payroll_system.py (no dependencies)
    └── hr_system.py (depends on: payroll_system.py, models/*)

KEUNTUNGAN:
✓ Clear dependency chain
✓ Avoid circular dependencies
✓ Easy to refactor
✓ Understand code flow

CONTOH REFACTOR:
Jika ingin ganti Person class dengan library lain:
1. Edit models/person.py only
2. Ensure same interface
3. All subclasses still work
   (karena depend on interface, not implementation)
"""


# ============================================================================
# 7. SCALABILITY (Skalabilitas)
# ============================================================================

"""
Menambah Fitur Baru:

SCENARIO: Add Training Management System

SINGLE FILE:
- Edit hari2_oop_implementation.py
- Add 200 lines
- Now 1200 lines
- Harder to navigate
- More risk of conflicts

MODULAR:
1. Create new file: systems/training_system.py

from models.employee import Employee

class TrainingSystem:
    def __init__(self):
        self.courses = []
        self.enrollments = []
    
    def add_course(self, course):
        self.courses.append(course)
    
    def enroll_employee(self, employee, course):
        # Logic here
        pass

2. Update systems/__init__.py:
from .training_system import TrainingSystem
__all__.append('TrainingSystem')

3. Use in main.py:
from systems import TrainingSystem
training = TrainingSystem()

RESULT:
✓ Zero modification to existing files
✓ New feature in new file
✓ Easy to remove if not needed
✓ Clear separation
"""


# ============================================================================
# 8. CODE NAVIGATION (Navigasi Code)
# ============================================================================

"""
IDE Features Work Better:

1. AUTOCOMPLETE:
   from models.emp|   <- IDE suggests: employee, full_time_employee, etc.
   
2. GO TO DEFINITION:
   Click on FullTimeEmployee -> Jump to full_time_employee.py
   
3. FIND USAGES:
   Where is Person used? -> Shows all files importing Person
   
4. REFACTOR:
   Rename Person to BasePerson -> IDE updates all imports automatically
   
5. SEARCH:
   "Find calculate_salary" -> Shows in specific file only

VS SINGLE FILE:
- Find in 1000 lines
- Hard to see structure
- Slow autocomplete
- Confusing go-to-definition
"""


# ============================================================================
# 9. DOCUMENTATION (Dokumentasi)
# ============================================================================

"""
SINGLE FILE:
- 1 docstring at top
- Hard to document each section
- Comments mixed with code
- No clear API documentation

MODULAR:
Each file has:
- Module docstring
- Clear purpose
- Import examples
- Usage examples

Example:

# models/person.py
'''
Person Model - Base class untuk semua person di sistem.

Usage:
    from models.person import Person
    
    person = Person(
        person_id="P001",
        name="John Doe",
        email="john@example.com",
        phone="081234567890",
        date_of_birth="1990-05-15"
    )
    
    age = person.get_age()
'''

✓ Self-documenting code
✓ Easy to generate API docs
✓ Clear usage examples
"""


# ============================================================================
# 10. PERFORMANCE (Performa Import)
# ============================================================================

"""
SINGLE FILE:
import hari2_oop_implementation
- Load 1000+ lines
- Parse all classes
- Memory overhead
- Slow startup

MODULAR - SELECTIVE IMPORT:
from models.person import Person
- Load only person.py (30 lines)
- Parse only Person class
- Minimal memory
- Fast startup

EXAMPLE:
# Script hanya butuh Person untuk validation
from models.person import Person  # Fast, light

# vs

import hari2_oop_implementation  # Loads everything, slow

BENEFIT:
✓ Faster import time
✓ Lower memory usage
✓ Better performance
"""


# ============================================================================
# 11. VERSION CONTROL (Git Best Practices)
# ============================================================================

"""
GIT HISTORY:

SINGLE FILE:
git log hari2_oop_implementation.py

commit 1: "Add Person class"
commit 2: "Add Employee class"
commit 3: "Add Payroll"
commit 4: "Fix Person bug"
commit 5: "Update Payroll"
...

Problem: All changes in 1 file history

MODULAR:
git log models/person.py
commit 1: "Add Person class"
commit 4: "Fix Person bug"

git log systems/payroll_system.py
commit 3: "Add Payroll"
commit 5: "Update Payroll"

BENEFIT:
✓ Clear history per component
✓ Easy to track changes
✓ Better blame/annotate
✓ Easier to revert specific features

EXAMPLE SCENARIO:
"Rollback payroll changes, keep everything else"

SINGLE FILE: Difficult, need to cherry-pick code
MODULAR: git checkout HEAD~1 systems/payroll_system.py
"""


# ============================================================================
# 12. REAL-WORLD COMPARISON
# ============================================================================

"""
POPULAR FRAMEWORKS STRUCTURE:

DJANGO (Python Web Framework):
myproject/
├── models/
│   ├── __init__.py
│   ├── user.py
│   └── product.py
├── views/
│   ├── __init__.py
│   └── main.py
└── urls.py

FLASK (Python Web Framework):
myapp/
├── models/
├── views/
└── services/

REACT (JavaScript):
src/
├── components/
├── services/
└── utils/

ANGULAR (JavaScript):
src/
├── app/
│   ├── models/
│   ├── services/
│   └── components/

✓ Industry standard
✓ Proven approach
✓ Scalable architecture
"""


# ============================================================================
# KESIMPULAN
# ============================================================================

"""
MODULAR STRUCTURE IS ESSENTIAL FOR:

1. ✓ Professional Development
2. ✓ Team Collaboration
3. ✓ Easy Maintenance
4. ✓ Code Reusability
5. ✓ Testing
6. ✓ Scalability
7. ✓ Performance
8. ✓ Documentation
9. ✓ Version Control
10. ✓ Career Preparation (Real-world coding)

REMEMBER:
"A good programmer writes code that humans can understand, not just machines."
- Martin Fowler

Modular structure membuat code:
- Readable (mudah dibaca)
- Maintainable (mudah di-maintain)
- Testable (mudah di-test)
- Scalable (mudah dikembangkan)
- Professional (standar industri)

NEXT STEPS:
1. Practice dengan modular structure
2. Always separate concerns
3. Keep files focused and small
4. Use clear naming conventions
5. Document your modules

Happy Coding! 🚀
"""

# ============================================================================
# PRACTICE EXERCISE
# ============================================================================

"""
TRY THIS:
1. Add new employee type: PartTimeEmployee
   - Create: models/part_time_employee.py
   - Inherit from Employee
   - Implement calculate_salary() with hourly rate
   
2. Add new system: TrainingSystem
   - Create: systems/training_system.py
   - Manage courses and enrollments
   - Track employee training progress
   
3. Add new feature: Performance Review System
   - Create: systems/performance_system.py
   - Schedule reviews
   - Generate review reports

Notice how easy it is to add features without touching existing code!
"""
