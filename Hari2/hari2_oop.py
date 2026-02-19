"""
PYTHON OOP (OBJECT-ORIENTED PROGRAMMING) - COMPREHENSIVE GUIDE
================================================================
File ini berisi materi lengkap OOP Python dengan penjelasan mendalam dan 
contoh studi kasus implementatif di dunia kerja.

Author: Python Learning Series
Day: 2 - Object-Oriented Programming
"""

# ============================================================================
# 1. INTRODUCTION TO OOP
# ============================================================================
"""
PENJELASAN:
OOP adalah paradigma programming yang mengorganisir code dalam bentuk objects.
Object adalah instance dari class yang memiliki attributes (data) dan methods (behavior).

4 PILAR OOP:
1. Encapsulation: Bundling data dan methods dalam satu unit (class)
2. Inheritance: Class bisa mewarisi properties dan methods dari class lain
3. Polymorphism: Kemampuan object untuk mengambil bentuk berbeda
4. Abstraction: Menyembunyikan kompleksitas internal

KEUNTUNGAN OOP:
- Code reusability
- Modularity dan organization
- Easier maintenance dan scaling
- Real-world modeling
- Data security dengan encapsulation

STUDI KASUS DI DUNIA KERJA:
OOP digunakan di hampir semua aplikasi enterprise:
- Web frameworks (Django, Flask)
- Desktop applications
- Mobile apps
- Game development
- Database ORM (SQLAlchemy)
- API development
"""

print("=" * 70)
print("BAGIAN 1: CLASS DAN OBJECT BASICS")
print("=" * 70)


# ============================================================================
# 2. CLASS DAN OBJECT BASICS
# ============================================================================
"""
PENJELASAN:
- Class: Blueprint/template untuk membuat objects
- Object: Instance dari class
- Attributes: Variables yang belong to class/object
- Methods: Functions yang belong to class

SYNTAX:
class ClassName:
    # class body
    pass
"""

# Class sederhana
class Employee:
    """Class untuk merepresentasikan karyawan."""
    
    # Constructor/Initializer
    def __init__(self, emp_id, name, position):
        """
        Initialize employee object.
        
        Args:
            emp_id (str): Employee ID
            name (str): Employee name
            position (str): Job position
        """
        self.emp_id = emp_id  # Instance attribute
        self.name = name
        self.position = position
    
    # Instance method
    def introduce(self):
        """Print employee introduction."""
        return f"Hi, saya {self.name}, bekerja sebagai {self.position}"
    
    def get_info(self):
        """Get employee information."""
        return f"ID: {self.emp_id} | Nama: {self.name} | Posisi: {self.position}"


# Membuat objects (instances)
emp1 = Employee("EMP001", "Tomas Anderson", "Software Engineer")
emp2 = Employee("EMP002", "Sarah Connor", "Product Manager")
emp3 = Employee("EMP003", "John Wick", "DevOps Engineer")

print("\n--- Employee Objects ---")
print(emp1.introduce())
print(emp2.introduce())
print(emp3.introduce())

print("\n--- Employee Details ---")
print(emp1.get_info())
print(emp2.get_info())

# Mengakses dan memodifikasi attributes
print(f"\nNama emp1 sebelum: {emp1.name}")
emp1.name = "Neo"  # Modify attribute
print(f"Nama emp1 setelah: {emp1.name}")


# ============================================================================
# 3. CLASS ATTRIBUTES VS INSTANCE ATTRIBUTES
# ============================================================================
"""
PENJELASAN:
- Instance Attributes: Unique untuk setiap object, didefinisikan dalam __init__
- Class Attributes: Shared oleh semua instances, didefinisikan di class level

KAPAN MENGGUNAKAN:
- Instance Attributes: Data yang berbeda untuk setiap object (nama, gaji, dll)
- Class Attributes: Data yang sama untuk semua objects (company name, tax rate, dll)

STUDI KASUS - COMPANY SETTINGS:
"""

print("\n" + "=" * 70)
print("BAGIAN 2: CLASS ATTRIBUTES VS INSTANCE ATTRIBUTES")
print("=" * 70)


class Employee_v2:
    """Enhanced Employee class dengan class attributes."""
    
    # Class attributes (shared by all instances)
    company_name = "Tech Solutions Inc."
    total_employees = 0
    annual_bonus_rate = 0.10
    
    def __init__(self, emp_id, name, position, salary):
        # Instance attributes (unique to each instance)
        self.emp_id = emp_id
        self.name = name
        self.position = position
        self.salary = salary
        
        # Increment total employees setiap kali object dibuat
        Employee_v2.total_employees += 1
    
    def calculate_bonus(self):
        """Calculate annual bonus menggunakan class attribute."""
        return self.salary * Employee_v2.annual_bonus_rate
    
    def get_full_info(self):
        """Get complete employee information."""
        bonus = self.calculate_bonus()
        return f"""
        Company: {Employee_v2.company_name}
        ID: {self.emp_id}
        Name: {self.name}
        Position: {self.position}
        Monthly Salary: Rp {self.salary:,}
        Annual Bonus: Rp {bonus:,.0f}
        """


# Creating multiple employees
print(f"Total employees awal: {Employee_v2.total_employees}")

emp_a = Employee_v2("EMP001", "Tomas", "Senior Developer", 15000000)
emp_b = Employee_v2("EMP002", "Sarah", "Tech Lead", 20000000)
emp_c = Employee_v2("EMP003", "Mike", "Junior Developer", 8000000)

print(f"Total employees sekarang: {Employee_v2.total_employees}")

print(f"\n--- Company Info ---")
print(f"Company: {Employee_v2.company_name}")
print(f"Bonus Rate: {Employee_v2.annual_bonus_rate * 100}%")

print("\n--- Employee A Details ---")
print(emp_a.get_full_info())

# Mengubah class attribute (affects all instances)
print("--- Updating Company Bonus Rate ---")
Employee_v2.annual_bonus_rate = 0.15  # Increase to 15%
print(f"New bonus rate: {Employee_v2.annual_bonus_rate * 100}%")
print(f"Tomas's new bonus: Rp {emp_a.calculate_bonus():,.0f}")
print(f"Sarah's new bonus: Rp {emp_b.calculate_bonus():,.0f}")


# ============================================================================
# 4. METHODS: INSTANCE, CLASS, DAN STATIC METHODS
# ============================================================================
"""
PENJELASAN:

INSTANCE METHOD:
- Default method type
- Memiliki akses ke instance (self)
- Bisa memodifikasi instance state dan class state

CLASS METHOD (@classmethod):
- Memiliki akses ke class (cls)
- Tidak bisa mengakses instance attributes
- Digunakan untuk factory methods atau modify class state

STATIC METHOD (@staticmethod):
- Tidak memiliki akses ke instance maupun class
- Seperti regular function tapi belong to class
- Digunakan untuk utility functions yang related to class

STUDI KASUS - EMPLOYEE MANAGEMENT SYSTEM:
"""

print("\n" + "=" * 70)
print("BAGIAN 3: INSTANCE, CLASS, DAN STATIC METHODS")
print("=" * 70)


class Employee_v3:
    """Employee class dengan berbagai jenis methods."""
    
    company_name = "Tech Solutions Inc."
    total_employees = 0
    min_salary = 5000000
    max_salary = 50000000
    
    def __init__(self, emp_id, name, position, salary):
        self.emp_id = emp_id
        self.name = name
        self.position = position
        self.salary = salary
        Employee_v3.total_employees += 1
    
    # INSTANCE METHOD
    def give_raise(self, amount):
        """
        Give raise to employee (instance method).
        Mengakses dan memodifikasi instance data.
        """
        old_salary = self.salary
        self.salary += amount
        return f"{self.name} mendapat raise Rp {amount:,}. Gaji: {old_salary:,} → {self.salary:,}"
    
    # CLASS METHOD sebagai alternative constructor (factory method)
    @classmethod
    def from_string(cls, emp_string):
        """
        Create Employee dari string format 'ID-Name-Position-Salary'.
        
        Class method berguna untuk alternative constructors.
        """
        emp_id, name, position, salary = emp_string.split('-')
        return cls(emp_id, name, position, int(salary))
    
    @classmethod
    def set_min_salary(cls, new_min_salary):
        """
        Update minimum salary (class method).
        Memodifikasi class attribute.
        """
        old_min = cls.min_salary
        cls.min_salary = new_min_salary
        return f"Minimum salary updated: Rp {old_min:,} → Rp {new_min_salary:,}"
    
    @classmethod
    def get_company_stats(cls):
        """Get company statistics (class method)."""
        return f"""
        Company: {cls.company_name}
        Total Employees: {cls.total_employees}
        Salary Range: Rp {cls.min_salary:,} - Rp {cls.max_salary:,}
        """
    
    # STATIC METHOD
    @staticmethod
    def is_valid_salary(salary):
        """
        Validasi salary range (static method).
        Tidak membutuhkan akses ke instance atau class.
        """
        return Employee_v3.min_salary <= salary <= Employee_v3.max_salary
    
    @staticmethod
    def calculate_annual_from_monthly(monthly_salary):
        """Calculate annual salary from monthly (static method)."""
        return monthly_salary * 12
    
    @staticmethod
    def format_currency(amount):
        """Format currency (static method - utility function)."""
        return f"Rp {amount:,.0f}"


print("\n--- Instance Method Example ---")
emp = Employee_v3("EMP001", "Tomas", "Developer", 10000000)
print(emp.give_raise(2000000))

print("\n--- Class Method: Alternative Constructor ---")
# Factory method - membuat object dari string
emp_from_string = Employee_v3.from_string("EMP002-Sarah-Designer-12000000")
print(f"Created: {emp_from_string.name} - {emp_from_string.position} - {Employee_v3.format_currency(emp_from_string.salary)}")

print("\n--- Class Method: Modify Class State ---")
print(Employee_v3.set_min_salary(6000000))

print("\n--- Class Method: Company Stats ---")
print(Employee_v3.get_company_stats())

print("\n--- Static Method: Utility Functions ---")
test_salaries = [4000000, 8000000, 60000000]
for salary in test_salaries:
    valid = Employee_v3.is_valid_salary(salary)
    status = "✓ Valid" if valid else "✗ Invalid"
    print(f"Salary {Employee_v3.format_currency(salary)}: {status}")

annual = Employee_v3.calculate_annual_from_monthly(10000000)
print(f"\nMonthly 10jt → Annual: {Employee_v3.format_currency(annual)}")


# ============================================================================
# 5. ENCAPSULATION: PUBLIC, PROTECTED, PRIVATE
# ============================================================================
"""
PENJELASAN:
Encapsulation adalah prinsip menyembunyikan internal details dan hanya expose interface.

PYTHON CONVENTION:
- Public: variable (normal access)
- Protected: _variable (should not be accessed outside, but technically can)
- Private: __variable (name mangling, harder to access)

Note: Python tidak enforce access control seperti Java/C++, ini hanya convention.

NAME MANGLING:
Private attributes (__variable) di-mangle menjadi _ClassName__variable

STUDI KASUS - BANKING SYSTEM:
Bank perlu protect sensitive data seperti balance, transaction history.
"""

print("\n" + "=" * 70)
print("BAGIAN 4: ENCAPSULATION - PUBLIC, PROTECTED, PRIVATE")
print("=" * 70)


class BankAccount:
    """
    Bank Account class dengan encapsulation.
    Demonstrasi public, protected, dan private attributes.
    """
    
    # Class attribute
    bank_name = "National Bank"
    interest_rate = 0.05  # 5% per tahun
    
    def __init__(self, account_number, account_holder, initial_balance=0):
        # Public attributes
        self.account_number = account_number
        self.account_holder = account_holder
        
        # Protected attribute (convention: don't access directly outside class)
        self._balance = initial_balance
        
        # Private attribute (name mangling)
        self.__pin = "1234"  # Default PIN
        self.__transaction_history = []
        
        # Log initial deposit
        if initial_balance > 0:
            self.__add_transaction("Initial Deposit", initial_balance)
    
    # Public method
    def deposit(self, amount):
        """Deposit money (public method)."""
        if amount <= 0:
            return "❌ Jumlah deposit harus lebih dari 0"
        
        self._balance += amount
        self.__add_transaction("Deposit", amount)
        return f"✓ Deposit berhasil: Rp {amount:,}. Saldo: Rp {self._balance:,}"
    
    def withdraw(self, amount, pin):
        """Withdraw money dengan PIN verification."""
        if not self.__verify_pin(pin):
            return "❌ PIN salah!"
        
        if amount <= 0:
            return "❌ Jumlah withdraw harus lebih dari 0"
        
        if amount > self._balance:
            return f"❌ Saldo tidak cukup. Saldo: Rp {self._balance:,}"
        
        self._balance -= amount
        self.__add_transaction("Withdrawal", -amount)
        return f"✓ Withdraw berhasil: Rp {amount:,}. Saldo: Rp {self._balance:,}"
    
    def get_balance(self, pin):
        """Get balance dengan PIN verification."""
        if not self.__verify_pin(pin):
            return "❌ PIN salah!"
        return f"Saldo: Rp {self._balance:,}"
    
    def change_pin(self, old_pin, new_pin):
        """Change PIN."""
        if not self.__verify_pin(old_pin):
            return "❌ PIN lama salah!"
        
        if len(new_pin) != 4 or not new_pin.isdigit():
            return "❌ PIN harus 4 digit angka"
        
        self.__pin = new_pin
        return "✓ PIN berhasil diubah"
    
    def get_transaction_history(self, pin):
        """Get transaction history dengan PIN verification."""
        if not self.__verify_pin(pin):
            return "❌ PIN salah!"
        
        if not self.__transaction_history:
            return "Tidak ada transaksi"
        
        history = "\n--- Transaction History ---\n"
        for i, transaction in enumerate(self.__transaction_history, 1):
            history += f"{i}. {transaction}\n"
        return history
    
    # Private method (internal use only)
    def __verify_pin(self, pin):
        """Verify PIN (private method)."""
        return pin == self.__pin
    
    def __add_transaction(self, transaction_type, amount):
        """Add transaction to history (private method)."""
        from datetime import datetime
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        sign = "+" if amount >= 0 else ""
        transaction = f"{timestamp} | {transaction_type}: {sign}Rp {abs(amount):,}"
        self.__transaction_history.append(transaction)
    
    # Protected method (internal/subclass use)
    def _calculate_interest(self):
        """Calculate interest (protected method)."""
        return self._balance * self.interest_rate
    
    def apply_annual_interest(self):
        """Apply annual interest (uses protected method)."""
        interest = self._calculate_interest()
        self._balance += interest
        self.__add_transaction("Interest", interest)
        return f"✓ Bunga tahunan diterapkan: Rp {interest:,.0f}. Saldo baru: Rp {self._balance:,}"
    
    # Public method untuk display info
    def get_account_info(self):
        """Get account information (tidak include sensitive data)."""
        return f"""
        Bank: {self.bank_name}
        Account Number: {self.account_number}
        Account Holder: {self.account_holder}
        (Gunakan get_balance() dengan PIN untuk melihat saldo)
        """


# Demonstrasi Encapsulation
print("\n--- Creating Bank Account ---")
account = BankAccount("1234567890", "Tomas Anderson", 5000000)
print(account.get_account_info())

# Public access
print("\n--- Public Access ---")
print(f"Account Number (public): {account.account_number}")
print(f"Account Holder (public): {account.account_holder}")

# Trying to access protected (will work but not recommended)
print("\n--- Protected Access (not recommended) ---")
print(f"Balance (protected _balance): Rp {account._balance:,}")

# Trying to access private (will cause AttributeError)
print("\n--- Private Access (will fail) ---")
try:
    print(account.__pin)  # This will fail
except AttributeError:
    print("❌ Cannot access __pin directly (private attribute)")

# But can access via name mangling (not recommended!)
print(f"PIN via name mangling: {account._BankAccount__pin} (don't do this!)")

# Proper way: using public methods
print("\n--- Using Public Methods (Proper Way) ---")
print(account.deposit(2000000))
print(account.withdraw(1000000, "1234"))
print(account.get_balance("1234"))

print("\n--- Change PIN ---")
print(account.change_pin("1234", "5678"))
print(account.withdraw(500000, "1234"))  # Old PIN - fail
print(account.withdraw(500000, "5678"))  # New PIN - success

print("\n--- Transaction History ---")
print(account.get_transaction_history("5678"))

print("\n--- Annual Interest ---")
print(account.apply_annual_interest())


# ============================================================================
# 6. INHERITANCE (PEWARISAN)
# ============================================================================
"""
PENJELASAN:
Inheritance memungkinkan class (child/subclass) untuk mewarisi attributes dan 
methods dari class lain (parent/superclass).

KEUNTUNGAN:
- Code reusability
- Hierarchical classification
- Method overriding
- Extensibility

TYPES:
- Single Inheritance: One parent
- Multiple Inheritance: Multiple parents
- Multilevel Inheritance: Chain of inheritance

STUDI KASUS - EMPLOYEE HIERARCHY:
Company memiliki berbagai tipe karyawan dengan characteristics berbeda.
"""

print("\n" + "=" * 70)
print("BAGIAN 5: INHERITANCE (PEWARISAN)")
print("=" * 70)


# Parent Class (Base Class)
class Employee_Base:
    """Base Employee class."""
    
    company_name = "Tech Solutions Inc."
    
    def __init__(self, emp_id, name, email, base_salary):
        self.emp_id = emp_id
        self.name = name
        self.email = email
        self.base_salary = base_salary
    
    def get_info(self):
        """Get basic employee info."""
        return f"[{self.emp_id}] {self.name} - {self.email}"
    
    def calculate_salary(self):
        """Calculate total salary (will be overridden by subclasses)."""
        return self.base_salary
    
    def work(self):
        """Generic work method."""
        return f"{self.name} is working..."


# Child Class 1: Developer
class Developer(Employee_Base):
    """Developer class - inherits from Employee_Base."""
    
    def __init__(self, emp_id, name, email, base_salary, programming_languages, level):
        # Call parent constructor
        super().__init__(emp_id, name, email, base_salary)
        
        # Add specific attributes
        self.programming_languages = programming_languages
        self.level = level  # Junior, Mid, Senior
        self.projects_completed = 0
    
    # Override calculate_salary
    def calculate_salary(self):
        """Calculate developer salary with level bonus."""
        level_bonus = {
            "Junior": 0,
            "Mid": 2000000,
            "Senior": 5000000
        }
        bonus = level_bonus.get(self.level, 0)
        project_bonus = self.projects_completed * 500000
        return self.base_salary + bonus + project_bonus
    
    # Override work method
    def work(self):
        """Developer specific work."""
        return f"{self.name} is coding in {', '.join(self.programming_languages)}..."
    
    # New method specific to Developer
    def complete_project(self):
        """Complete a project."""
        self.projects_completed += 1
        return f"✓ {self.name} completed project #{self.projects_completed}"
    
    def code_review(self, code):
        """Review code."""
        return f"{self.name} is reviewing code: '{code}'"


# Child Class 2: Manager
class Manager(Employee_Base):
    """Manager class - inherits from Employee_Base."""
    
    def __init__(self, emp_id, name, email, base_salary, department, team_size):
        super().__init__(emp_id, name, email, base_salary)
        self.department = department
        self.team_size = team_size
        self.team_members = []
    
    # Override calculate_salary
    def calculate_salary(self):
        """Calculate manager salary with team bonus."""
        team_bonus = self.team_size * 500000  # 500k per team member
        return self.base_salary + team_bonus
    
    # Override work method
    def work(self):
        """Manager specific work."""
        return f"{self.name} is managing {self.department} department with {self.team_size} people..."
    
    # New methods specific to Manager
    def add_team_member(self, employee):
        """Add team member."""
        self.team_members.append(employee)
        self.team_size += 1
        return f"✓ {employee.name} added to {self.name}'s team"
    
    def conduct_meeting(self, topic):
        """Conduct team meeting."""
        return f"{self.name} is conducting meeting about '{topic}' with {self.team_size} people"
    
    def approve_leave(self, employee_name, days):
        """Approve employee leave."""
        return f"✓ {self.name} approved {days} days leave for {employee_name}"


# Child Class 3: Intern
class Intern(Employee_Base):
    """Intern class - inherits from Employee_Base."""
    
    def __init__(self, emp_id, name, email, base_salary, university, mentor_id):
        super().__init__(emp_id, name, email, base_salary)
        self.university = university
        self.mentor_id = mentor_id
        self.duration_months = 0
    
    # Override calculate_salary
    def calculate_salary(self):
        """Intern gets base salary only."""
        return self.base_salary
    
    # Override work method
    def work(self):
        """Intern specific work."""
        return f"{self.name} is learning and working (intern from {self.university})..."
    
    def extend_internship(self, months):
        """Extend internship duration."""
        self.duration_months += months
        return f"✓ {self.name}'s internship extended by {months} months (total: {self.duration_months})"


# Demonstrasi Inheritance
print("\n--- Creating Different Employee Types ---")

dev = Developer(
    "DEV001", 
    "Tomas Anderson", 
    "tomas@tech.com", 
    10000000,
    ["Python", "JavaScript", "Go"],
    "Senior"
)

manager = Manager(
    "MGR001",
    "Sarah Connor",
    "sarah@tech.com",
    15000000,
    "Engineering",
    0  # Will add team members later
)

intern = Intern(
    "INT001",
    "Mike Ross",
    "mike@tech.com",
    3000000,
    "MIT",
    "DEV001"
)

print("\n--- Employee Information (Inherited Method) ---")
print(dev.get_info())
print(manager.get_info())
print(intern.get_info())

print("\n--- Work Methods (Overridden) ---")
print(dev.work())
print(manager.work())
print(intern.work())

print("\n--- Salary Calculation (Overridden) ---")
print(f"{dev.name} salary: Rp {dev.calculate_salary():,}")
print(f"{manager.name} salary: Rp {manager.calculate_salary():,}")
print(f"{intern.name} salary: Rp {intern.calculate_salary():,}")

print("\n--- Developer Specific Methods ---")
print(dev.complete_project())
print(dev.complete_project())
print(dev.code_review("def hello(): return 'world'"))
print(f"Updated salary with project bonus: Rp {dev.calculate_salary():,}")

print("\n--- Manager Specific Methods ---")
print(manager.add_team_member(dev))
print(manager.add_team_member(intern))
print(manager.conduct_meeting("Q1 Planning"))
print(manager.approve_leave("Tomas Anderson", 3))
print(f"Updated salary with team bonus: Rp {manager.calculate_salary():,}")

print("\n--- Intern Specific Methods ---")
print(intern.extend_internship(3))

# Check inheritance using isinstance()
print("\n--- Checking Inheritance (isinstance) ---")
print(f"dev is Developer: {isinstance(dev, Developer)}")
print(f"dev is Employee_Base: {isinstance(dev, Employee_Base)}")
print(f"manager is Developer: {isinstance(manager, Developer)}")
print(f"manager is Employee_Base: {isinstance(manager, Employee_Base)}")


# ============================================================================
# 7. MULTIPLE INHERITANCE DAN METHOD RESOLUTION ORDER (MRO)
# ============================================================================
"""
PENJELASAN:
Multiple Inheritance: Class bisa inherit dari multiple parent classes.

METHOD RESOLUTION ORDER (MRO):
Python menggunakan C3 Linearization algorithm untuk menentukan urutan method lookup.
Gunakan ClassName.mro() atau ClassName.__mro__ untuk melihat MRO.

DIAMOND PROBLEM:
Terjadi ketika class inherit dari 2 parents yang punya common ancestor.
Python resolve ini dengan MRO.

STUDI KASUS - EMPLOYEE DENGAN MULTIPLE ROLES:
"""

print("\n" + "=" * 70)
print("BAGIAN 6: MULTIPLE INHERITANCE & MRO")
print("=" * 70)


class Developer_Mixin:
    """Mixin class untuk developer capabilities."""
    
    def code(self, language):
        return f"Writing code in {language}"
    
    def debug(self, bug):
        return f"Debugging: {bug}"
    
    def deploy(self, environment):
        return f"Deploying to {environment}"


class Manager_Mixin:
    """Mixin class untuk manager capabilities."""
    
    def manage_team(self, team_size):
        return f"Managing team of {team_size} people"
    
    def conduct_review(self, employee):
        return f"Conducting performance review for {employee}"
    
    def allocate_budget(self, amount):
        return f"Allocating budget: Rp {amount:,}"


class Presenter_Mixin:
    """Mixin class untuk presentation capabilities."""
    
    def create_presentation(self, topic):
        return f"Creating presentation about '{topic}'"
    
    def present(self, audience):
        return f"Presenting to {audience}"


# Multiple Inheritance: Tech Lead has both Developer and Manager capabilities
class TechLead(Developer_Mixin, Manager_Mixin, Presenter_Mixin, Employee_Base):
    """
    Tech Lead class - inherits from multiple classes.
    Combines Developer, Manager, dan Presenter capabilities.
    """
    
    def __init__(self, emp_id, name, email, base_salary, tech_stack, team_size):
        Employee_Base.__init__(self, emp_id, name, email, base_salary)
        self.tech_stack = tech_stack
        self.team_size = team_size
    
    def calculate_salary(self):
        """Tech Lead gets both coding and management bonus."""
        tech_bonus = 5000000
        management_bonus = self.team_size * 800000
        return self.base_salary + tech_bonus + management_bonus
    
    def work(self):
        """Tech Lead work."""
        return f"{self.name} is leading team and coding..."
    
    def sprint_planning(self):
        """Conduct sprint planning."""
        return f"{self.name} is conducting sprint planning with {self.team_size} developers"


# Create Tech Lead
print("\n--- Creating Tech Lead (Multiple Inheritance) ---")
tech_lead = TechLead(
    "TL001",
    "Neo Anderson",
    "neo@tech.com",
    18000000,
    ["Python", "AWS", "Docker"],
    5
)

print(tech_lead.get_info())
print(f"Salary: Rp {tech_lead.calculate_salary():,}")

print("\n--- Using Developer Capabilities ---")
print(tech_lead.code("Python"))
print(tech_lead.debug("Memory leak in user service"))
print(tech_lead.deploy("Production"))

print("\n--- Using Manager Capabilities ---")
print(tech_lead.manage_team(5))
print(tech_lead.conduct_review("Junior Developer"))
print(tech_lead.allocate_budget(100000000))

print("\n--- Using Presenter Capabilities ---")
print(tech_lead.create_presentation("Microservices Architecture"))
print(tech_lead.present("Engineering Team"))

print("\n--- Tech Lead Specific Methods ---")
print(tech_lead.sprint_planning())

print("\n--- Method Resolution Order (MRO) ---")
print("Tech Lead MRO:")
for i, cls in enumerate(TechLead.mro(), 1):
    print(f"  {i}. {cls.__name__}")


# ============================================================================
# 8. POLYMORPHISM
# ============================================================================
"""
PENJELASAN:
Polymorphism = "many forms". Object bisa take different forms.
Same interface, different implementations.

TYPES:
1. Method Overriding: Subclass provides different implementation
2. Duck Typing: "If it walks like a duck and quacks like a duck, it's a duck"

STUDI KASUS - PAYMENT PROCESSING SYSTEM:
Berbagai payment methods dengan interface sama tapi implementation berbeda.
"""

print("\n" + "=" * 70)
print("BAGIAN 7: POLYMORPHISM")
print("=" * 70)


# Base Payment class
class Payment:
    """Base Payment class."""
    
    def __init__(self, amount, customer_name):
        self.amount = amount
        self.customer_name = customer_name
        self.status = "pending"
    
    def process_payment(self):
        """Process payment - to be overridden by subclasses."""
        raise NotImplementedError("Subclass must implement process_payment()")
    
    def get_receipt(self):
        """Get payment receipt."""
        return f"""
        Receipt
        -------
        Customer: {self.customer_name}
        Amount: Rp {self.amount:,}
        Status: {self.status}
        """


class CreditCardPayment(Payment):
    """Credit Card Payment."""
    
    def __init__(self, amount, customer_name, card_number, cvv):
        super().__init__(amount, customer_name)
        self.card_number = card_number
        self.cvv = cvv
        self.payment_method = "Credit Card"
    
    def process_payment(self):
        """Process credit card payment."""
        # Simulate credit card processing
        print(f"Processing credit card payment...")
        print(f"Card: **** **** **** {self.card_number[-4:]}")
        print(f"Amount: Rp {self.amount:,}")
        self.status = "completed"
        return f"✓ Credit Card payment processed successfully"


class BankTransferPayment(Payment):
    """Bank Transfer Payment."""
    
    def __init__(self, amount, customer_name, bank_name, account_number):
        super().__init__(amount, customer_name)
        self.bank_name = bank_name
        self.account_number = account_number
        self.payment_method = "Bank Transfer"
    
    def process_payment(self):
        """Process bank transfer payment."""
        # Simulate bank transfer
        print(f"Processing bank transfer...")
        print(f"Bank: {self.bank_name}")
        print(f"Account: {self.account_number}")
        print(f"Amount: Rp {self.amount:,}")
        self.status = "completed"
        return f"✓ Bank Transfer payment processed successfully"


class EWalletPayment(Payment):
    """E-Wallet Payment."""
    
    def __init__(self, amount, customer_name, wallet_type, phone_number):
        super().__init__(amount, customer_name)
        self.wallet_type = wallet_type  # GoPay, OVO, Dana, etc.
        self.phone_number = phone_number
        self.payment_method = "E-Wallet"
    
    def process_payment(self):
        """Process e-wallet payment."""
        # Simulate e-wallet processing
        print(f"Processing {self.wallet_type} payment...")
        print(f"Phone: {self.phone_number}")
        print(f"Amount: Rp {self.amount:,}")
        self.status = "completed"
        return f"✓ {self.wallet_type} payment processed successfully"


# Polymorphism in action
def process_customer_payment(payment):
    """
    Process any type of payment (polymorphism).
    Same function works with different payment types.
    """
    print("\n" + "-" * 50)
    print(f"Customer: {payment.customer_name}")
    result = payment.process_payment()
    print(result)
    return payment.get_receipt()


# Create different payment types
print("\n--- Creating Different Payment Methods ---")

payment1 = CreditCardPayment(
    amount=5000000,
    customer_name="Tomas Anderson",
    card_number="1234567890123456",
    cvv="123"
)

payment2 = BankTransferPayment(
    amount=10000000,
    customer_name="Sarah Connor",
    bank_name="BCA",
    account_number="1234567890"
)

payment3 = EWalletPayment(
    amount=250000,
    customer_name="Mike Ross",
    wallet_type="GoPay",
    phone_number="081234567890"
)

# Process all payments using same function (polymorphism)
print("\n--- Processing Payments (Polymorphism) ---")
payments = [payment1, payment2, payment3]

for payment in payments:
    receipt = process_customer_payment(payment)
    print(receipt)


# Duck Typing Example
class CashPayment:
    """Cash Payment - tidak inherit dari Payment, tapi punya interface sama."""
    
    def __init__(self, amount, customer_name):
        self.amount = amount
        self.customer_name = customer_name
        self.status = "pending"
        self.payment_method = "Cash"
    
    def process_payment(self):
        """Process cash payment."""
        print(f"Processing cash payment...")
        print(f"Amount: Rp {self.amount:,}")
        self.status = "completed"
        return f"✓ Cash payment received"
    
    def get_receipt(self):
        """Get receipt."""
        return f"""
        Receipt
        -------
        Customer: {self.customer_name}
        Amount: Rp {self.amount:,}
        Method: {self.payment_method}
        Status: {self.status}
        """


print("\n--- Duck Typing Example ---")
cash_payment = CashPayment(150000, "John Wick")
# Meskipun tidak inherit dari Payment, bisa diproses sama
receipt = process_customer_payment(cash_payment)
print(receipt)


# ============================================================================
# 9. ABSTRACT CLASSES DAN INTERFACES
# ============================================================================
"""
PENJELASAN:
Abstract Class: Class yang tidak bisa diinstantiasi, hanya sebagai blueprint.
Memaksa subclass untuk implement certain methods.

Python menggunakan module `abc` (Abstract Base Classes).

KAPAN MENGGUNAKAN:
- Enforce interface contract
- Ensure subclasses implement specific methods
- Create a common API

STUDI KASUS - NOTIFICATION SYSTEM:
"""

print("\n" + "=" * 70)
print("BAGIAN 8: ABSTRACT CLASSES")
print("=" * 70)

from abc import ABC, abstractmethod


class NotificationService(ABC):
    """Abstract base class for notification services."""
    
    def __init__(self, recipient):
        self.recipient = recipient
        self.sent = False
    
    @abstractmethod
    def send(self, message):
        """Send notification - must be implemented by subclasses."""
        pass
    
    @abstractmethod
    def validate_recipient(self):
        """Validate recipient - must be implemented by subclasses."""
        pass
    
    # Concrete method (implemented in base class)
    def mark_as_sent(self):
        """Mark notification as sent."""
        self.sent = True
        return "Notification marked as sent"


class EmailNotification(NotificationService):
    """Email notification implementation."""
    
    def __init__(self, recipient, subject):
        super().__init__(recipient)
        self.subject = subject
    
    def validate_recipient(self):
        """Validate email address."""
        return "@" in self.recipient and "." in self.recipient
    
    def send(self, message):
        """Send email notification."""
        if not self.validate_recipient():
            return f"❌ Invalid email: {self.recipient}"
        
        print(f"\n📧 Sending Email...")
        print(f"To: {self.recipient}")
        print(f"Subject: {self.subject}")
        print(f"Message: {message}")
        self.mark_as_sent()
        return "✓ Email sent successfully"


class SMSNotification(NotificationService):
    """SMS notification implementation."""
    
    def validate_recipient(self):
        """Validate phone number."""
        # Simple validation: starts with 08 and has 10-13 digits
        return self.recipient.startswith("08") and len(self.recipient) >= 10
    
    def send(self, message):
        """Send SMS notification."""
        if not self.validate_recipient():
            return f"❌ Invalid phone number: {self.recipient}"
        
        print(f"\n📱 Sending SMS...")
        print(f"To: {self.recipient}")
        print(f"Message: {message}")
        self.mark_as_sent()
        return "✓ SMS sent successfully"


class PushNotification(NotificationService):
    """Push notification implementation."""
    
    def __init__(self, recipient, app_name):
        super().__init__(recipient)
        self.app_name = app_name
    
    def validate_recipient(self):
        """Validate device token."""
        # Simple validation: token should be non-empty
        return len(self.recipient) > 0
    
    def send(self, message):
        """Send push notification."""
        if not self.validate_recipient():
            return f"❌ Invalid device token"
        
        print(f"\n🔔 Sending Push Notification...")
        print(f"App: {self.app_name}")
        print(f"Device Token: {self.recipient[:20]}...")
        print(f"Message: {message}")
        self.mark_as_sent()
        return "✓ Push notification sent successfully"


# Function that works with any NotificationService
def send_notification(notification_service, message):
    """Send notification using any notification service."""
    print("\n" + "=" * 50)
    result = notification_service.send(message)
    print(result)
    print(f"Sent status: {notification_service.sent}")


# Demonstrasi Abstract Classes
print("\n--- Creating Notification Services ---")

email = EmailNotification("tomas@tech.com", "Welcome to Our Platform")
sms = SMSNotification("081234567890")
push = PushNotification("device_token_xyz123abc456", "TechApp")

print("\n--- Sending Notifications ---")
send_notification(email, "Hello Tomas, welcome to our platform!")
send_notification(sms, "Your OTP code is: 123456")
send_notification(push, "You have a new message!")

# Try with invalid recipients
print("\n--- Invalid Recipients ---")
invalid_email = EmailNotification("invalid-email", "Test")
send_notification(invalid_email, "This should fail")

invalid_sms = SMSNotification("123")  # Too short
send_notification(invalid_sms, "This should fail")


# Attempting to instantiate abstract class (will fail)
print("\n--- Cannot Instantiate Abstract Class ---")
try:
    notification = NotificationService("test@test.com")
except TypeError as e:
    print(f"❌ Error: {e}")


# ============================================================================
# 10. PROPERTY DECORATORS (@property, @setter, @deleter)
# ============================================================================
"""
PENJELASAN:
@property decorator mengubah method menjadi attribute (getter).
Memungkinkan controlled access ke attributes dengan validation.

KEUNTUNGAN:
- Data validation
- Computed attributes
- Backward compatibility
- Encapsulation

STUDI KASUS - PRODUCT CATALOG SYSTEM:
"""

print("\n" + "=" * 70)
print("BAGIAN 9: PROPERTY DECORATORS")
print("=" * 70)


class Product:
    """Product class dengan property decorators."""
    
    def __init__(self, product_id, name, base_price, discount_percent=0):
        self.product_id = product_id
        self._name = name
        self._base_price = base_price
        self._discount_percent = discount_percent
        self._stock = 0
    
    # Property: name (with validation)
    @property
    def name(self):
        """Get product name."""
        return self._name
    
    @name.setter
    def name(self, value):
        """Set product name with validation."""
        if not value or len(value) < 3:
            raise ValueError("Product name must be at least 3 characters")
        self._name = value.title()
    
    # Property: base_price (with validation)
    @property
    def base_price(self):
        """Get base price."""
        return self._base_price
    
    @base_price.setter
    def base_price(self, value):
        """Set base price with validation."""
        if value < 0:
            raise ValueError("Price cannot be negative")
        self._base_price = value
    
    # Property: discount_percent (with validation)
    @property
    def discount_percent(self):
        """Get discount percentage."""
        return self._discount_percent
    
    @discount_percent.setter
    def discount_percent(self, value):
        """Set discount with validation."""
        if not 0 <= value <= 100:
            raise ValueError("Discount must be between 0 and 100")
        self._discount_percent = value
    
    # Computed property: final_price (read-only)
    @property
    def final_price(self):
        """Calculate final price after discount (computed property)."""
        discount_amount = self._base_price * (self._discount_percent / 100)
        return self._base_price - discount_amount
    
    # Property: stock
    @property
    def stock(self):
        """Get stock quantity."""
        return self._stock
    
    @stock.setter
    def stock(self, value):
        """Set stock with validation."""
        if value < 0:
            raise ValueError("Stock cannot be negative")
        self._stock = value
    
    # Computed property: is_available
    @property
    def is_available(self):
        """Check if product is available (computed property)."""
        return self._stock > 0
    
    # Computed property: total_value
    @property
    def total_value(self):
        """Calculate total inventory value (computed property)."""
        return self.final_price * self._stock
    
    def add_stock(self, quantity):
        """Add stock."""
        if quantity <= 0:
            raise ValueError("Quantity must be positive")
        self._stock += quantity
        return f"✓ Added {quantity} units. New stock: {self._stock}"
    
    def remove_stock(self, quantity):
        """Remove stock."""
        if quantity <= 0:
            raise ValueError("Quantity must be positive")
        if quantity > self._stock:
            raise ValueError(f"Not enough stock. Available: {self._stock}")
        self._stock -= quantity
        return f"✓ Removed {quantity} units. Remaining stock: {self._stock}"
    
    def __str__(self):
        """String representation."""
        return f"""
Product: {self.name}
ID: {self.product_id}
Base Price: Rp {self.base_price:,}
Discount: {self.discount_percent}%
Final Price: Rp {self.final_price:,.0f}
Stock: {self.stock} units
Available: {'Yes' if self.is_available else 'No'}
Total Value: Rp {self.total_value:,.0f}
        """


# Demonstrasi Property Decorators
print("\n--- Creating Product ---")
laptop = Product("PRD001", "gaming laptop", 15000000, 10)
laptop.stock = 50

print(laptop)

print("\n--- Using Properties (like attributes) ---")
print(f"Product name: {laptop.name}")  # Calls getter
print(f"Base price: Rp {laptop.base_price:,}")
print(f"Final price: Rp {laptop.final_price:,.0f}")  # Computed property
print(f"Is available: {laptop.is_available}")  # Computed property

print("\n--- Modifying via Setters (with validation) ---")
laptop.discount_percent = 15  # Calls setter with validation
print(f"New discount: {laptop.discount_percent}%")
print(f"New final price: Rp {laptop.final_price:,.0f}")

print("\n--- Stock Management ---")
print(laptop.add_stock(20))
print(laptop.remove_stock(10))
print(f"Total inventory value: Rp {laptop.total_value:,.0f}")

print("\n--- Validation Examples ---")
try:
    laptop.name = "ab"  # Too short
except ValueError as e:
    print(f"❌ Name validation: {e}")

try:
    laptop.base_price = -1000  # Negative
except ValueError as e:
    print(f"❌ Price validation: {e}")

try:
    laptop.discount_percent = 150  # > 100
except ValueError as e:
    print(f"❌ Discount validation: {e}")

try:
    laptop.remove_stock(100)  # Not enough stock
except ValueError as e:
    print(f"❌ Stock validation: {e}")


# ============================================================================
# 11. MAGIC/DUNDER METHODS
# ============================================================================
"""
PENJELASAN:
Magic methods (dunder methods) adalah special methods dengan double underscore.
Memungkinkan custom behavior untuk built-in operations.

COMMON MAGIC METHODS:
- __init__: Constructor
- __str__: String representation (user-friendly)
- __repr__: String representation (developer-friendly)
- __len__: Define behavior for len()
- __getitem__: Define behavior for indexing []
- __setitem__: Define behavior for item assignment
- __iter__: Make object iterable
- __eq__, __lt__, __gt__: Comparison operators
- __add__, __sub__, __mul__: Arithmetic operators
- __call__: Make object callable like function

STUDI KASUS - SHOPPING CART SYSTEM:
"""

print("\n" + "=" * 70)
print("BAGIAN 10: MAGIC/DUNDER METHODS")
print("=" * 70)


class ShoppingCart:
    """Shopping Cart dengan magic methods."""
    
    def __init__(self, customer_name):
        """Initialize cart."""
        self.customer_name = customer_name
        self.items = []
        self.created_at = __import__('datetime').datetime.now()
    
    def add_item(self, product_name, price, quantity=1):
        """Add item to cart."""
        self.items.append({
            "product": product_name,
            "price": price,
            "quantity": quantity
        })
    
    # __str__: User-friendly string representation
    def __str__(self):
        """String representation for users."""
        return f"Shopping Cart for {self.customer_name} ({len(self.items)} items)"
    
    # __repr__: Developer-friendly representation
    def __repr__(self):
        """String representation for developers."""
        return f"ShoppingCart(customer='{self.customer_name}', items={len(self.items)})"
    
    # __len__: Define behavior for len()
    def __len__(self):
        """Return number of items in cart."""
        return len(self.items)
    
    # __getitem__: Enable indexing cart[0]
    def __getitem__(self, index):
        """Get item by index."""
        return self.items[index]
    
    # __setitem__: Enable item assignment cart[0] = value
    def __setitem__(self, index, value):
        """Set item by index."""
        self.items[index] = value
    
    # __iter__: Make cart iterable
    def __iter__(self):
        """Make cart iterable."""
        return iter(self.items)
    
    # __contains__: Enable 'in' operator
    def __contains__(self, product_name):
        """Check if product in cart."""
        return any(item["product"] == product_name for item in self.items)
    
    # __add__: Enable cart1 + cart2
    def __add__(self, other):
        """Merge two carts."""
        new_cart = ShoppingCart(f"{self.customer_name} & {other.customer_name}")
        new_cart.items = self.items + other.items
        return new_cart
    
    # __eq__: Enable cart1 == cart2
    def __eq__(self, other):
        """Check if two carts are equal."""
        return (self.customer_name == other.customer_name and 
                self.items == other.items)
    
    # __bool__: Enable if cart (True if has items)
    def __bool__(self):
        """Return True if cart has items."""
        return len(self.items) > 0
    
    # __call__: Make cart callable
    def __call__(self):
        """Calculate total when cart is called."""
        return self.get_total()
    
    # Custom method
    def get_total(self):
        """Calculate total cart value."""
        return sum(item["price"] * item["quantity"] for item in self.items)
    
    def get_summary(self):
        """Get cart summary."""
        summary = f"\n{'='*60}\n"
        summary += f"SHOPPING CART - {self.customer_name}\n"
        summary += f"{'='*60}\n"
        
        for i, item in enumerate(self.items, 1):
            subtotal = item["price"] * item["quantity"]
            summary += f"{i}. {item['product']:<30} x{item['quantity']:<3} = Rp {subtotal:>12,}\n"
        
        summary += f"{'-'*60}\n"
        summary += f"{'TOTAL:':<35} Rp {self.get_total():>12,}\n"
        summary += f"{'='*60}\n"
        return summary


# Demonstrasi Magic Methods
print("\n--- Creating Shopping Carts ---")
cart1 = ShoppingCart("Tomas Anderson")
cart1.add_item("Laptop", 15000000, 1)
cart1.add_item("Mouse", 250000, 2)
cart1.add_item("Keyboard", 800000, 1)

cart2 = ShoppingCart("Sarah Connor")
cart2.add_item("Monitor", 3000000, 2)
cart2.add_item("Webcam", 1500000, 1)

print("\n--- __str__ and __repr__ ---")
print(f"str(cart1): {str(cart1)}")  # Calls __str__
print(f"repr(cart1): {repr(cart1)}")  # Calls __repr__

print("\n--- __len__ (len function) ---")
print(f"Number of items in cart1: {len(cart1)}")  # Calls __len__
print(f"Number of items in cart2: {len(cart2)}")

print("\n--- __getitem__ (indexing) ---")
print(f"First item in cart1: {cart1[0]}")  # Calls __getitem__
print(f"Second item in cart1: {cart1[1]}")

print("\n--- __iter__ (iteration) ---")
print("Items in cart1:")
for item in cart1:  # Calls __iter__
    print(f"  - {item['product']}: Rp {item['price']:,}")

print("\n--- __contains__ ('in' operator) ---")
print(f"'Laptop' in cart1: {'Laptop' in cart1}")  # Calls __contains__
print(f"'Phone' in cart1: {'Phone' in cart1}")

print("\n--- __add__ (+ operator) ---")
merged_cart = cart1 + cart2  # Calls __add__
print(f"Merged cart: {merged_cart}")
print(f"Items in merged cart: {len(merged_cart)}")

print("\n--- __bool__ (boolean context) ---")
empty_cart = ShoppingCart("Empty User")
print(f"cart1 is truthy: {bool(cart1)}")  # Calls __bool__
print(f"empty_cart is truthy: {bool(empty_cart)}")

if cart1:  # Uses __bool__
    print("Cart1 has items!")

print("\n--- __call__ (callable object) ---")
total1 = cart1()  # Calls __call__ which calls get_total()
print(f"Total cart1 (using call): Rp {total1:,}")

print("\n--- Cart Summary ---")
print(cart1.get_summary())
print(cart2.get_summary())


# ============================================================================
# 12. COMPOSITION VS INHERITANCE
# ============================================================================
"""
PENJELASAN:
COMPOSITION: "Has-a" relationship
- Object contains other objects
- More flexible than inheritance
- Easier to modify and test

INHERITANCE: "Is-a" relationship
- Object is a type of another object
- Can lead to deep hierarchies
- Tightly coupled

PRINCIPLE: "Favor composition over inheritance"

STUDI KASUS - CAR MANUFACTURING SYSTEM:
"""

print("\n" + "=" * 70)
print("BAGIAN 11: COMPOSITION VS INHERITANCE")
print("=" * 70)


# Components (to be composed)
class Engine:
    """Engine component."""
    
    def __init__(self, engine_type, horsepower):
        self.engine_type = engine_type
        self.horsepower = horsepower
        self.running = False
    
    def start(self):
        """Start engine."""
        self.running = True
        return f"🔧 {self.engine_type} engine started ({self.horsepower} HP)"
    
    def stop(self):
        """Stop engine."""
        self.running = False
        return f"🔧 Engine stopped"
    
    def get_info(self):
        """Get engine info."""
        status = "Running" if self.running else "Stopped"
        return f"{self.engine_type} - {self.horsepower} HP - {status}"


class Transmission:
    """Transmission component."""
    
    def __init__(self, transmission_type):
        self.transmission_type = transmission_type
        self.current_gear = "P"  # Park
    
    def shift_gear(self, gear):
        """Shift gear."""
        self.current_gear = gear
        return f"⚙️ Shifted to gear: {gear}"
    
    def get_info(self):
        """Get transmission info."""
        return f"{self.transmission_type} - Current gear: {self.current_gear}"


class FuelTank:
    """Fuel tank component."""
    
    def __init__(self, capacity):
        self.capacity = capacity
        self.current_fuel = capacity
    
    def refuel(self, amount):
        """Refuel."""
        if self.current_fuel + amount > self.capacity:
            amount = self.capacity - self.current_fuel
        self.current_fuel += amount
        return f"⛽ Refueled {amount}L. Current: {self.current_fuel}L/{self.capacity}L"
    
    def consume_fuel(self, amount):
        """Consume fuel."""
        if amount > self.current_fuel:
            return "❌ Not enough fuel!"
        self.current_fuel -= amount
        return f"⛽ Used {amount}L fuel. Remaining: {self.current_fuel}L"
    
    def get_info(self):
        """Get fuel info."""
        percentage = (self.current_fuel / self.capacity) * 100
        return f"Fuel: {self.current_fuel}L / {self.capacity}L ({percentage:.1f}%)"


class GPS:
    """GPS component."""
    
    def __init__(self):
        self.current_location = "Unknown"
        self.destination = None
    
    def set_destination(self, location):
        """Set destination."""
        self.destination = location
        return f"🗺️ Destination set to: {location}"
    
    def navigate(self):
        """Navigate."""
        if not self.destination:
            return "❌ No destination set"
        return f"🗺️ Navigating to {self.destination}..."
    
    def get_info(self):
        """Get GPS info."""
        return f"GPS - Location: {self.current_location}, Destination: {self.destination or 'None'}"


# Car using COMPOSITION (has-a relationship)
class Car:
    """Car class using composition (has Engine, Transmission, etc.)."""
    
    def __init__(self, make, model, year, engine, transmission, fuel_tank):
        self.make = make
        self.model = model
        self.year = year
        
        # Composition: Car HAS-A engine, transmission, fuel_tank
        self.engine = engine
        self.transmission = transmission
        self.fuel_tank = fuel_tank
        self.gps = GPS()  # Optional GPS
        
        self.mileage = 0
    
    def start_car(self):
        """Start car."""
        print(f"\n🚗 Starting {self.year} {self.make} {self.model}...")
        print(self.engine.start())
        print(self.transmission.shift_gear("D"))
        return "✓ Car started and ready to drive"
    
    def drive(self, distance_km):
        """Drive car."""
        if not self.engine.running:
            return "❌ Start the engine first!"
        
        fuel_needed = distance_km * 0.1  # 0.1L per km
        result = self.fuel_tank.consume_fuel(fuel_needed)
        
        if "Not enough" in result:
            return result
        
        self.mileage += distance_km
        return f"🚗 Drove {distance_km} km. Total mileage: {self.mileage} km"
    
    def stop_car(self):
        """Stop car."""
        print(f"\n🚗 Stopping {self.make} {self.model}...")
        print(self.transmission.shift_gear("P"))
        print(self.engine.stop())
        return "✓ Car stopped"
    
    def get_full_info(self):
        """Get complete car information."""
        return f"""
{'='*60}
CAR INFORMATION
{'='*60}
Car: {self.year} {self.make} {self.model}
Mileage: {self.mileage} km

{self.engine.get_info()}
{self.transmission.get_info()}
{self.fuel_tank.get_info()}
{self.gps.get_info()}
{'='*60}
        """


# Demonstrasi Composition
print("\n--- Creating Car with Composition ---")

# Create components
engine = Engine("V6 Turbocharged", 300)
transmission = Transmission("Automatic 8-Speed")
fuel_tank = FuelTank(60)  # 60 liter capacity

# Create car with components
car = Car("Toyota", "Camry", 2024, engine, transmission, fuel_tank)

print(car.get_full_info())

print("\n--- Using Car ---")
print(car.start_car())

print("\n--- Driving ---")
print(car.drive(50))
print(car.drive(100))

print("\n--- Using GPS (through car) ---")
print(car.gps.set_destination("Jakarta Convention Center"))
print(car.gps.navigate())

print("\n--- Refueling ---")
print(car.fuel_tank.refuel(30))

print("\n--- Final Status ---")
print(car.get_full_info())

print("\n--- Stopping Car ---")
print(car.stop_car())


# Comparison: Inheritance approach (less flexible)
print("\n--- Comparison with Inheritance Approach ---")
print("""
INHERITANCE APPROACH (less flexible):
class Vehicle:
    def start_engine():
        pass

class ElectricVehicle(Vehicle):
    # Problem: Inherit engine but don't need it
    pass

COMPOSITION APPROACH (more flexible):
class Car:
    def __init__(self, engine):  # Can swap engine types
        self.engine = engine

ADVANTAGES OF COMPOSITION:
✓ More flexible - can swap components easily
✓ Easier to test - test components independently
✓ No deep inheritance hierarchy
✓ Loosely coupled
✓ Easier to change behavior at runtime
""")


# ============================================================================
# 13. REAL-WORLD PROJECT: E-COMMERCE SYSTEM
# ============================================================================
"""
COMPREHENSIVE STUDI KASUS:
E-Commerce System dengan semua konsep OOP yang telah dipelajari.
"""

print("\n" + "=" * 70)
print("BAGIAN 12: REAL-WORLD PROJECT - E-COMMERCE SYSTEM")
print("=" * 70)


class User:
    """Base User class."""
    
    user_count = 0
    
    def __init__(self, user_id, name, email, phone):
        self.user_id = user_id
        self.name = name
        self.email = email
        self.phone = phone
        self.created_at = __import__('datetime').datetime.now()
        User.user_count += 1
    
    def __str__(self):
        return f"User({self.user_id}): {self.name} - {self.email}"
    
    def __repr__(self):
        return f"User(id='{self.user_id}', name='{self.name}')"


class Customer(User):
    """Customer class - inherits from User."""
    
    def __init__(self, user_id, name, email, phone, address):
        super().__init__(user_id, name, email, phone)
        self.address = address
        self.cart = ShoppingCart(name)
        self.orders = []
        self.loyalty_points = 0
    
    def add_to_cart(self, product, quantity=1):
        """Add product to cart."""
        self.cart.add_item(product.name, product.final_price, quantity)
        return f"✓ Added {product.name} to cart"
    
    def checkout(self):
        """Checkout cart."""
        if not self.cart:
            return "❌ Cart is empty!"
        
        order = Order(f"ORD{len(self.orders)+1:04d}", self, list(self.cart.items))
        self.orders.append(order)
        
        # Add loyalty points (1 point per 10,000)
        points_earned = int(order.total_amount / 10000)
        self.loyalty_points += points_earned
        
        # Clear cart
        self.cart = ShoppingCart(self.name)
        
        return f"✓ Order placed! Order ID: {order.order_id}. Points earned: {points_earned}"
    
    def get_order_history(self):
        """Get order history."""
        if not self.orders:
            return "No orders yet"
        
        history = f"\n{'='*60}\n"
        history += f"ORDER HISTORY - {self.name}\n"
        history += f"{'='*60}\n"
        for order in self.orders:
            history += f"\n{order.get_summary()}"
        history += f"\nTotal Orders: {len(self.orders)}\n"
        history += f"Loyalty Points: {self.loyalty_points}\n"
        history += f"{'='*60}\n"
        return history


class Seller(User):
    """Seller class - inherits from User."""
    
    def __init__(self, user_id, name, email, phone, shop_name):
        super().__init__(user_id, name, email, phone)
        self.shop_name = shop_name
        self.products = []
        self.total_sales = 0
    
    def add_product(self, product):
        """Add product to  seller's catalog."""
        product.seller = self
        self.products.append(product)
        return f"✓ Product '{product.name}' added to {self.shop_name}"
    
    def get_product_catalog(self):
        """Get product catalog."""
        if not self.products:
            return "No products available"
        
        catalog = f"\n{'='*60}\n"
        catalog += f"{self.shop_name.upper()} - PRODUCT CATALOG\n"
        catalog += f"{'='*60}\n"
        for i, product in enumerate(self.products, 1):
            catalog += f"{i}. {product.name} - Rp {product.final_price:,.0f} (Stock: {product.stock})\n"
        catalog += f"{'='*60}\n"
        return catalog


class Order:
    """Order class."""
    
    def __init__(self, order_id, customer, items):
        self.order_id = order_id
        self.customer = customer
        self.items = items
        self.order_date = __import__('datetime').datetime.now()
        self.status = "Pending"
        self.total_amount = sum(item["price"] * item["quantity"] for item in items)
    
    def update_status(self, new_status):
        """Update order status."""
        self.status = new_status
        return f"✓ Order {self.order_id} status updated to: {new_status}"
    
    def get_summary(self):
        """Get order summary."""
        summary = f"Order ID: {self.order_id}\n"
        summary += f"Date: {self.order_date.strftime('%Y-%m-%d %H:%M')}\n"
        summary += f"Status: {self.status}\n"
        summary += f"Total: Rp {self.total_amount:,}\n"
        return summary
    
    def __str__(self):
        return f"Order({self.order_id}) - {self.customer.name} - Rp {self.total_amount:,}"


# Demonstrasi E-Commerce System
print("\n--- Setting Up E-Commerce System ---")

# Create sellers
seller1 = Seller("SEL001", "TechStore", "tech@store.com", "08111111111", "TechGadget Store")
seller2 = Seller("SEL002", "FashionHub", "fashion@hub.com", "08122222222", "Fashion Paradise")

# Create products
laptop = Product("PRD001", "Gaming Laptop", 15000000, 10)
laptop.stock = 50
seller1.add_product(laptop)

mouse = Product("PRD002", "Wireless Mouse", 250000, 0)
mouse.stock = 100
seller1.add_product(mouse)

keyboard = Product("PRD003", "Mechanical Keyboard", 800000, 5)
keyboard.stock = 75
seller1.add_product(keyboard)

# Display product catalog
print(seller1.get_product_catalog())

# Create customer
customer = Customer("CUST001", "Tomas Anderson", "tomas@email.com", "08199999999", "Jakarta")

print(f"\n--- Customer: {customer} ---")

# Shopping flow
print("\n--- Shopping ---")
print(customer.add_to_cart(laptop, 1))
print(customer.add_to_cart(mouse, 2))
print(customer.add_to_cart(keyboard, 1))

print("\n--- Cart Summary ---")
print(customer.cart.get_summary())

# Checkout
print("\n--- Checkout ---")
print(customer.checkout())

# Order history
print(customer.get_order_history())

# Another order
print("\n--- Second Purchase ---")
print(customer.add_to_cart(keyboard, 2))
print(customer.checkout())

# Final order history
print(customer.get_order_history())


# ============================================================================
# PENUTUP
# ============================================================================
print("\n" + "=" * 70)
print("SELESAI - PYTHON OOP")
print("=" * 70)
print("""
File ini mencakup semua konsep OOP Python:

✓ Class dan Object Basics
✓ Instance vs Class Attributes
✓ Instance, Class, dan Static Methods
✓ Encapsulation (Public, Protected, Private)
✓ Inheritance (Single, Multiple, MRO)
✓ Polymorphism (Method Overriding, Duck Typing)
✓ Abstract Classes dan Interfaces
✓ Property Decorators (@property, @setter)
✓ Magic/Dunder Methods
✓ Composition vs Inheritance
✓ Real-World Projects:
  - Bank Account System
  - Employee Management System
  - Notification Service
  - Payment Processing
  - Shopping Cart & E-Commerce
  - Car Manufacturing

BEST PRACTICES YANG DIPELAJARI:
- Favor composition over inheritance
- Use property decorators untuk validation
- Implement magic methods untuk better UX
- Follow encapsulation principles
- Use abstract classes untuk enforce contracts
- Apply SOLID principles
- Write clean, maintainable code

Next Steps:
- Practice dengan project sendiri
- Explore design patterns (Singleton, Factory, Observer, dll)
- Learn about dataclasses (Python 3.7+)
- Study advanced OOP concepts

Happy coding! 🚀
""")
