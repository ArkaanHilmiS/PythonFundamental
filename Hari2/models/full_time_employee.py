"""
Full-Time Employee Model - Karyawan tetap dengan benefits lengkap.
"""

from models.employee import Employee


class FullTimeEmployee(Employee):
    """Full-time employee dengan benefits lengkap."""
    
    def __init__(self, emp_id, name, email, phone, date_of_birth, 
                 join_date, department, base_salary, position, grade):
        super().__init__(emp_id, name, email, phone, date_of_birth,
                        join_date, department, base_salary, position)
        
        self.grade = grade  # Junior, Mid, Senior, Lead
        self.health_insurance = True
        self.pension_contribution = 0.05  # 5% of salary
    
    def calculate_salary(self):
        """Calculate full-time employee salary dengan benefits."""
        # Grade bonus
        grade_bonus = {
            "Junior": 0,
            "Mid": 2000000,
            "Senior": 5000000,
            "Lead": 8000000
        }
        
        # Performance bonus (based on average rating)
        avg_rating = self.get_average_rating()
        performance_bonus = 0
        if avg_rating >= 4.5:
            performance_bonus = self.base_salary * 0.20  # 20%
        elif avg_rating >= 4.0:
            performance_bonus = self.base_salary * 0.15  # 15%
        elif avg_rating >= 3.5:
            performance_bonus = self.base_salary * 0.10  # 10%
        
        # Tenure bonus (1% per year, max 10%)
        years, _ = self.calculate_tenure()
        tenure_bonus = min(self.base_salary * years * 0.01, self.base_salary * 0.10)
        
        # Total salary
        total = (self.base_salary + 
                grade_bonus.get(self.grade, 0) + 
                performance_bonus + 
                tenure_bonus)
        
        # Deductions
        pension = total * self.pension_contribution
        
        return {
            "base_salary": self.base_salary,
            "grade_bonus": grade_bonus.get(self.grade, 0),
            "performance_bonus": performance_bonus,
            "tenure_bonus": tenure_bonus,
            "gross_salary": total,
            "pension_deduction": pension,
            "net_salary": total - pension
        }
