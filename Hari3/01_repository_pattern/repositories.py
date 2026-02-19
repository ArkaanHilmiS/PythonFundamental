"""
========================================================================
HARI 3 - REPOSITORY IMPLEMENTATIONS
Implementasi Repository Pattern untuk CSV, SQLite, dan Mock
========================================================================
"""

import csv
import sqlite3
import json
from abc import ABC, abstractmethod
from typing import List, Dict, Optional
from datetime import datetime


# ========================================================================
# 1. ABSTRACT BASE REPOSITORY (Interface)
# ========================================================================

class IEmployeeRepository(ABC):
    """
    Interface untuk Employee Repository.
    Semua repository harus implement methods ini.
    
    Benefits:
    - Consistency: Semua repository punya interface yang sama
    - Replaceable: Bisa ganti implementation tanpa ubah business logic
    - Testable: Bisa mock dengan mudah
    """
    
    @abstractmethod
    def load(self) -> List[Dict]:
        """Load all employees from storage."""
        pass
    
    @abstractmethod
    def save(self, employees: List[Dict]) -> None:
        """Save employees to storage."""
        pass
    
    @abstractmethod
    def get_by_id(self, emp_id: str) -> Optional[Dict]:
        """Get employee by ID."""
        pass
    
    @abstractmethod
    def add(self, employee: Dict) -> None:
        """Add new employee."""
        pass
    
    @abstractmethod
    def delete(self, emp_id: str) -> bool:
        """Delete employee by ID."""
        pass


# ========================================================================
# 2. CSV REPOSITORY (File-Based Storage)
# ========================================================================

class EmployeeCSVRepository(IEmployeeRepository):
    """
    CSV Repository Implementation.
    
    Use Case:
    - Small applications
    - Simple data storage
    - Easy to edit manually
    - No database setup needed
    
    Pros:
    ✅ Simple
    ✅ Human readable
    ✅ No database required
    ✅ Easy backup (just copy file)
    
    Cons:
    ❌ Not scalable for large data
    ❌ No concurrent access control
    ❌ Limited query capabilities
    """
    
    def __init__(self, filename: str):
        """
        Initialize CSV Repository.
        
        Args:
            filename: Path to CSV file
        """
        self.filename = filename
        self._ensure_file_exists()
    
    def _ensure_file_exists(self):
        """Create file with header if not exists."""
        try:
            with open(self.filename, 'r') as f:
                pass
        except FileNotFoundError:
            # Create file with header
            with open(self.filename, 'w', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                writer.writerow(['id', 'nama', 'email', 'departemen', 'gaji', 'join_date'])
    
    def load(self) -> List[Dict]:
        """
        Load all employees from CSV file.
        
        Returns:
            List of employee dictionaries
        """
        employees = []
        
        try:
            with open(self.filename, 'r', newline='', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    # Convert gaji to float
                    if 'gaji' in row:
                        row['gaji'] = float(row['gaji'])
                    employees.append(row)
            
            print(f"✓ Loaded {len(employees)} employees from CSV")
            return employees
            
        except FileNotFoundError:
            print(f"⚠ File {self.filename} tidak ditemukan")
            return []
        except Exception as e:
            print(f"❌ Error loading CSV: {e}")
            return []
    
    def save(self, employees: List[Dict]) -> None:
        """
        Save employees to CSV file.
        
        Args:
            employees: List of employee dictionaries
        """
        if not employees:
            print("⚠ No employees to save")
            return
        
        try:
            with open(self.filename, 'w', newline='', encoding='utf-8') as f:
                # Get all unique keys from all employees
                fieldnames = set()
                for emp in employees:
                    fieldnames.update(emp.keys())
                
                fieldnames = sorted(fieldnames)  # Sort for consistency
                
                writer = csv.DictWriter(f, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(employees)
            
            print(f"✓ Saved {len(employees)} employees to CSV")
            
        except Exception as e:
            print(f"❌ Error saving CSV: {e}")
            raise
    
    def get_by_id(self, emp_id: str) -> Optional[Dict]:
        """Get employee by ID."""
        employees = self.load()
        for emp in employees:
            if emp.get('id') == emp_id:
                return emp
        return None
    
    def add(self, employee: Dict) -> None:
        """Add new employee."""
        employees = self.load()
        
        # Check if ID already exists
        if any(emp.get('id') == employee.get('id') for emp in employees):
            raise ValueError(f"Employee ID {employee.get('id')} already exists")
        
        employees.append(employee)
        self.save(employees)
        print(f"✓ Added employee: {employee.get('nama')}")
    
    def delete(self, emp_id: str) -> bool:
        """Delete employee by ID."""
        employees = self.load()
        original_count = len(employees)
        
        employees = [emp for emp in employees if emp.get('id') != emp_id]
        
        if len(employees) < original_count:
            self.save(employees)
            print(f"✓ Deleted employee ID: {emp_id}")
            return True
        
        print(f"⚠ Employee ID {emp_id} not found")
        return False


# ========================================================================
# 3. SQLITE REPOSITORY (Database Storage)
# ========================================================================

class EmployeeSQLiteRepository(IEmployeeRepository):
    """
    SQLite Repository Implementation.
    
    Use Case:
    - Medium applications
    - Need ACID properties
    - Concurrent access
    - Complex queries
    
    Pros:
    ✅ ACID compliant
    ✅ Concurrent access
    ✅ Good performance
    ✅ SQL query support
    ✅ No server required
    
    Cons:
    ❌ Binary format (not human readable)
    ❌ Single file can be large
    """
    
    def __init__(self, db_path: str):
        """
        Initialize SQLite Repository.
        
        Args:
            db_path: Path to SQLite database file
        """
        self.db_path = db_path
        self._create_table()
    
    def _create_table(self):
        """Create employees table if not exists."""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS employees (
                id TEXT PRIMARY KEY,
                nama TEXT NOT NULL,
                email TEXT,
                departemen TEXT,
                gaji REAL NOT NULL,
                join_date TEXT,
                created_at TEXT DEFAULT CURRENT_TIMESTAMP
            )
        """)
        
        conn.commit()
        conn.close()
        print(f"✓ SQLite database initialized: {self.db_path}")
    
    def load(self) -> List[Dict]:
        """Load all employees from database."""
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row  # Enable column access by name
        cursor = conn.cursor()
        
        cursor.execute("SELECT * FROM employees")
        rows = cursor.fetchall()
        
        employees = [dict(row) for row in rows]
        
        conn.close()
        print(f"✓ Loaded {len(employees)} employees from SQLite")
        return employees
    
    def save(self, employees: List[Dict]) -> None:
        """
        Save employees to database.
        This replaces all data (use with caution!).
        """
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        # Clear table
        cursor.execute("DELETE FROM employees")
        
        # Insert all employees
        for emp in employees:
            cursor.execute("""
                INSERT INTO employees (id, nama, email, departemen, gaji, join_date)
                VALUES (?, ?, ?, ?, ?, ?)
            """, (
                emp.get('id'),
                emp.get('nama'),
                emp.get('email'),
                emp.get('departemen'),
                emp.get('gaji'),
                emp.get('join_date')
            ))
        
        conn.commit()
        conn.close()
        print(f"✓ Saved {len(employees)} employees to SQLite")
    
    def get_by_id(self, emp_id: str) -> Optional[Dict]:
        """Get employee by ID."""
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        
        cursor.execute("SELECT * FROM employees WHERE id = ?", (emp_id,))
        row = cursor.fetchone()
        
        conn.close()
        
        return dict(row) if row else None
    
    def add(self, employee: Dict) -> None:
        """Add new employee."""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        try:
            cursor.execute("""
                INSERT INTO employees (id, nama, email, departemen, gaji, join_date)
                VALUES (?, ?, ?, ?, ?, ?)
            """, (
                employee.get('id'),
                employee.get('nama'),
                employee.get('email'),
                employee.get('departemen'),
                employee.get('gaji'),
                employee.get('join_date')
            ))
            
            conn.commit()
            print(f"✓ Added employee: {employee.get('nama')}")
            
        except sqlite3.IntegrityError:
            raise ValueError(f"Employee ID {employee.get('id')} already exists")
        finally:
            conn.close()
    
    def delete(self, emp_id: str) -> bool:
        """Delete employee by ID."""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute("DELETE FROM employees WHERE id = ?", (emp_id,))
        deleted = cursor.rowcount > 0
        
        conn.commit()
        conn.close()
        
        if deleted:
            print(f"✓ Deleted employee ID: {emp_id}")
        else:
            print(f"⚠ Employee ID {emp_id} not found")
        
        return deleted
    
    def get_by_department(self, departemen: str) -> List[Dict]:
        """Get all employees in a department (SQL-specific feature)."""
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        
        cursor.execute("SELECT * FROM employees WHERE departemen = ?", (departemen,))
        rows = cursor.fetchall()
        
        employees = [dict(row) for row in rows]
        conn.close()
        
        return employees
    
    def get_salary_range(self, min_gaji: float, max_gaji: float) -> List[Dict]:
        """Get employees within salary range (SQL-specific feature)."""
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        
        cursor.execute(
            "SELECT * FROM employees WHERE gaji BETWEEN ? AND ?",
            (min_gaji, max_gaji)
        )
        rows = cursor.fetchall()
        
        employees = [dict(row) for row in rows]
        conn.close()
        
        return employees


# ========================================================================
# 4. MOCK REPOSITORY (For Testing)
# ========================================================================

class MockEmployeeRepository(IEmployeeRepository):
    """
    Mock Repository for Testing.
    
    Use Case:
    - Unit testing
    - Integration testing
    - Development tanpa setup database
    
    Pros:
    ✅ Super fast
    ✅ No file/database needed
    ✅ Perfect for testing
    ✅ Full control of data
    
    Cons:
    ❌ Data hilang setelah program stop
    ❌ Tidak untuk production
    """
    
    def __init__(self, initial_data: List[Dict] = None):
        """
        Initialize Mock Repository with optional initial data.
        
        Args:
            initial_data: Initial employee data
        """
        self._data = initial_data if initial_data else []
        print(f"✓ Mock repository initialized with {len(self._data)} employees")
    
    def load(self) -> List[Dict]:
        """Load all employees from memory."""
        return self._data.copy()  # Return copy to prevent external modification
    
    def save(self, employees: List[Dict]) -> None:
        """Save employees to memory."""
        self._data = employees.copy()
        print(f"✓ Mock: Saved {len(employees)} employees")
    
    def get_by_id(self, emp_id: str) -> Optional[Dict]:
        """Get employee by ID."""
        for emp in self._data:
            if emp.get('id') == emp_id:
                return emp.copy()
        return None
    
    def add(self, employee: Dict) -> None:
        """Add new employee."""
        if any(emp.get('id') == employee.get('id') for emp in self._data):
            raise ValueError(f"Employee ID {employee.get('id')} already exists")
        
        self._data.append(employee.copy())
        print(f"✓ Mock: Added employee {employee.get('nama')}")
    
    def delete(self, emp_id: str) -> bool:
        """Delete employee by ID."""
        original_count = len(self._data)
        self._data = [emp for emp in self._data if emp.get('id') != emp_id]
        
        deleted = len(self._data) < original_count
        if deleted:
            print(f"✓ Mock: Deleted employee ID {emp_id}")
        else:
            print(f"⚠ Mock: Employee ID {emp_id} not found")
        
        return deleted


# ========================================================================
# 5. JSON REPOSITORY (Bonus!)
# ========================================================================

class EmployeeJSONRepository(IEmployeeRepository):
    """
    JSON Repository Implementation.
    
    Use Case:
    - API integration
    - Config storage
    - Human-readable structured data
    
    Pros:
    ✅ Human readable
    ✅ Nested data support
    ✅ Easy to parse
    ✅ Standard format
    
    Cons:
    ❌ Larger file size than CSV
    ❌ Not as performant as binary formats
    """
    
    def __init__(self, filename: str):
        """Initialize JSON Repository."""
        self.filename = filename
        self._ensure_file_exists()
    
    def _ensure_file_exists(self):
        """Create empty JSON file if not exists."""
        try:
            with open(self.filename, 'r') as f:
                pass
        except FileNotFoundError:
            with open(self.filename, 'w', encoding='utf-8') as f:
                json.dump([], f)
    
    def load(self) -> List[Dict]:
        """Load employees from JSON file."""
        try:
            with open(self.filename, 'r', encoding='utf-8') as f:
                employees = json.load(f)
            print(f"✓ Loaded {len(employees)} employees from JSON")
            return employees
        except Exception as e:
            print(f"❌ Error loading JSON: {e}")
            return []
    
    def save(self, employees: List[Dict]) -> None:
        """Save employees to JSON file."""
        try:
            with open(self.filename, 'w', encoding='utf-8') as f:
                json.dump(employees, f, indent=2, ensure_ascii=False)
            print(f"✓ Saved {len(employees)} employees to JSON")
        except Exception as e:
            print(f"❌ Error saving JSON: {e}")
            raise
    
    def get_by_id(self, emp_id: str) -> Optional[Dict]:
        """Get employee by ID."""
        employees = self.load()
        for emp in employees:
            if emp.get('id') == emp_id:
                return emp
        return None
    
    def add(self, employee: Dict) -> None:
        """Add new employee."""
        employees = self.load()
        
        if any(emp.get('id') == employee.get('id') for emp in employees):
            raise ValueError(f"Employee ID {employee.get('id')} already exists")
        
        employees.append(employee)
        self.save(employees)
        print(f"✓ Added employee: {employee.get('nama')}")
    
    def delete(self, emp_id: str) -> bool:
        """Delete employee by ID."""
        employees = self.load()
        original_count = len(employees)
        
        employees = [emp for emp in employees if emp.get('id') != emp_id]
        
        if len(employees) < original_count:
            self.save(employees)
            print(f"✓ Deleted employee ID: {emp_id}")
            return True
        
        print(f"⚠ Employee ID {emp_id} not found")
        return False


# ========================================================================
# DEMO USAGE
# ========================================================================

if __name__ == "__main__":
    print("="*70)
    print("REPOSITORY PATTERN IMPLEMENTATIONS DEMO")
    print("="*70)
    
    # Sample employee data
    sample_employees = [
        {
            "id": "EMP001",
            "nama": "Tomas Anderson",
            "email": "tomas@company.com",
            "departemen": "IT",
            "gaji": 15000000,
            "join_date": "2020-01-15"
        },
        {
            "id": "EMP002",
            "nama": "Sarah Connor",
            "email": "sarah@company.com",
            "departemen": "IT",
            "gaji": 20000000,
            "join_date": "2019-03-01"
        },
        {
            "id": "EMP003",
            "nama": "John Wick",
            "email": "john@company.com",
            "departemen": "Finance",
            "gaji": 18000000,
            "join_date": "2021-06-15"
        }
    ]
    
    print("\n" + "="*70)
    print("1. CSV REPOSITORY DEMO")
    print("="*70)
    
    csv_repo = EmployeeCSVRepository("employees_demo.csv")
    csv_repo.save(sample_employees)
    loaded = csv_repo.load()
    print(f"Loaded employees: {[emp['nama'] for emp in loaded]}")
    
    print("\n" + "="*70)
    print("2. SQLITE REPOSITORY DEMO")
    print("="*70)
    
    sqlite_repo = EmployeeSQLiteRepository("employees_demo.db")
    sqlite_repo.save(sample_employees)
    loaded = sqlite_repo.load()
    print(f"Loaded employees: {[emp['nama'] for emp in loaded]}")
    
    # SQL-specific features
    it_employees = sqlite_repo.get_by_department("IT")
    print(f"IT Department: {[emp['nama'] for emp in it_employees]}")
    
    print("\n" + "="*70)
    print("3. MOCK REPOSITORY DEMO (Perfect for Testing)")
    print("="*70)
    
    mock_repo = MockEmployeeRepository(sample_employees)
    emp = mock_repo.get_by_id("EMP001")
    print(f"Found employee: {emp['nama']}")
    
    print("\n" + "="*70)
    print("4. JSON REPOSITORY DEMO")
    print("="*70)
    
    json_repo = EmployeeJSONRepository("employees_demo.json")
    json_repo.save(sample_employees)
    loaded = json_repo.load()
    print(f"Loaded employees: {[emp['nama'] for emp in loaded]}")
    
    print("\n" + "="*70)
    print("✓ ALL REPOSITORIES WORK WITH SAME INTERFACE!")
    print("This is the power of Repository Pattern!")
    print("="*70)
