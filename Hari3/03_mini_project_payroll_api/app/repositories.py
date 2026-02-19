"""
========================================================================
PAYROLL API - Repositories
Data Access Layer for Employee Management
========================================================================
"""

import csv
import sqlite3
from abc import ABC, abstractmethod
from typing import List, Dict, Optional


# ========================================================================
# ABSTRACT REPOSITORY INTERFACE
# ========================================================================

class IEmployeeRepository(ABC):
    """Interface untuk Employee Repository."""
    
    @abstractmethod
    def load(self) -> List[Dict]:
        """Load all employees."""
        pass
    
    @abstractmethod
    def save(self, employees: List[Dict]) -> None:
        """Save employees."""
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
# CSV REPOSITORY IMPLEMENTATION
# ========================================================================

class EmployeeCSVRepository(IEmployeeRepository):
    """CSV-based Employee Repository."""
    
    def __init__(self, filename: str):
        self.filename = filename
        self._ensure_file_exists()
    
    def _ensure_file_exists(self):
        """Create file with header if not exists."""
        try:
            with open(self.filename, 'r') as f:
                pass
        except FileNotFoundError:
            with open(self.filename, 'w', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                writer.writerow(['id', 'nama', 'email', 'departemen', 'gaji', 'join_date'])
    
    def load(self) -> List[Dict]:
        """Load all employees from CSV."""
        employees = []
        
        try:
            with open(self.filename, 'r', newline='', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    if 'gaji' in row:
                        row['gaji'] = float(row['gaji'])
                    employees.append(row)
            
            return employees
            
        except FileNotFoundError:
            return []
        except Exception as e:
            print(f"Error loading CSV: {e}")
            return []
    
    def save(self, employees: List[Dict]) -> None:
        """Save employees to CSV."""
        if not employees:
            return
        
        try:
            with open(self.filename, 'w', newline='', encoding='utf-8') as f:
                fieldnames = sorted(set().union(*[emp.keys() for emp in employees]))
                writer = csv.DictWriter(f, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(employees)
                
        except Exception as e:
            print(f"Error saving CSV: {e}")
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
    
    def delete(self, emp_id: str) -> bool:
        """Delete employee by ID."""
        employees = self.load()
        original_count = len(employees)
        
        employees = [emp for emp in employees if emp.get('id') != emp_id]
        
        if len(employees) < original_count:
            self.save(employees)
            return True
        
        return False
    
    def update(self, emp_id: str, updated_data: Dict) -> Optional[Dict]:
        """Update employee data."""
        employees = self.load()
        
        for emp in employees:
            if emp.get('id') == emp_id:
                emp.update(updated_data)
                self.save(employees)
                return emp
        
        return None


# ========================================================================
# MOCK REPOSITORY (FOR TESTING)
# ========================================================================

class MockEmployeeRepository(IEmployeeRepository):
    """Mock repository for testing."""
    
    def __init__(self, initial_data: List[Dict] = None):
        self._data = initial_data if initial_data else []
    
    def load(self) -> List[Dict]:
        return self._data.copy()
    
    def save(self, employees: List[Dict]) -> None:
        self._data = employees.copy()
    
    def get_by_id(self, emp_id: str) -> Optional[Dict]:
        for emp in self._data:
            if emp.get('id') == emp_id:
                return emp.copy()
        return None
    
    def add(self, employee: Dict) -> None:
        if any(emp.get('id') == employee.get('id') for emp in self._data):
            raise ValueError(f"Employee ID {employee.get('id')} already exists")
        
        self._data.append(employee.copy())
    
    def delete(self, emp_id: str) -> bool:
        original_count = len(self._data)
        self._data = [emp for emp in self._data if emp.get('id') != emp_id]
        return len(self._data) < original_count
    
    def update(self, emp_id: str, updated_data: Dict) -> Optional[Dict]:
        for emp in self._data:
            if emp.get('id') == emp_id:
                emp.update(updated_data)
                return emp.copy()
        return None
