"""
Person Model - Base class untuk semua person di sistem.
"""

from datetime import datetime


class Person:
    """Base class untuk semua person di sistem."""
    
    def __init__(self, person_id, name, email, phone, date_of_birth):
        self.person_id = person_id
        self.name = name
        self.email = email
        self.phone = phone
        self.date_of_birth = date_of_birth
        self.created_at = datetime.now()
    
    def get_age(self):
        """Calculate age from date of birth."""
        today = datetime.now()
        dob = datetime.strptime(self.date_of_birth, "%Y-%m-%d")
        age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
        return age
    
    def __str__(self):
        return f"{self.name} ({self.email})"
    
    def __repr__(self):
        return f"Person(id='{self.person_id}', name='{self.name}')"
