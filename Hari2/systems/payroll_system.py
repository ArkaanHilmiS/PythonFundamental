"""
Payroll System - Sistem untuk mengelola penggajian karyawan.
"""

from datetime import datetime


class PayrollSystem:
    """System untuk mengelola payroll."""
    
    def __init__(self):
        self.payslips = []
        self.company_tax_rate = 0.05  # 5% PPh21
    
    def generate_payslip(self, employee, period_month, period_year):
        """Generate payslip for employee."""
        salary_breakdown = employee.calculate_salary()
        
        # Calculate tax
        gross = salary_breakdown["gross_salary"]
        tax = gross * self.company_tax_rate
        
        # Attendance bonus/penalty
        attendance = employee.get_monthly_attendance_summary(period_year, period_month)
        attendance_bonus = 0
        if attendance["present_days"] >= 22:  # Full attendance
            attendance_bonus = 500000
        
        final_net = salary_breakdown["net_salary"] - tax + attendance_bonus
        
        payslip = {
            "employee_id": employee.emp_id,
            "employee_name": employee.name,
            "period": f"{period_year}-{period_month:02d}",
            "basic_salary": employee.base_salary,
            "salary_breakdown": salary_breakdown,
            "tax": tax,
            "attendance_bonus": attendance_bonus,
            "attendance_days": attendance["present_days"],
            "final_net_salary": final_net,
            "generated_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        
        self.payslips.append(payslip)
        return payslip
    
    def print_payslip(self, payslip):
        """Print formatted payslip."""
        breakdown = payslip["salary_breakdown"]
        
        output = f"""
{'='*70}
                            PAYSLIP
{'='*70}
Employee ID    : {payslip['employee_id']}
Employee Name  : {payslip['employee_name']}
Period         : {payslip['period']}
Generated      : {payslip['generated_at']}

{'='*70}
EARNINGS
{'='*70}
Base Salary              : Rp {breakdown.get('base_salary', 0):>15,.0f}
"""
        
        # Additional earnings
        if "grade_bonus" in breakdown and breakdown["grade_bonus"] > 0:
            output += f"Grade Bonus              : Rp {breakdown['grade_bonus']:>15,.0f}\n"
        if "performance_bonus" in breakdown and breakdown["performance_bonus"] > 0:
            output += f"Performance Bonus        : Rp {breakdown['performance_bonus']:>15,.0f}\n"
        if "tenure_bonus" in breakdown and breakdown["tenure_bonus"] > 0:
            output += f"Tenure Bonus             : Rp {breakdown['tenure_bonus']:>15,.0f}\n"
        if payslip["attendance_bonus"] > 0:
            output += f"Attendance Bonus         : Rp {payslip['attendance_bonus']:>15,.0f}\n"
        
        output += f"""
{'-'*70}
Gross Salary             : Rp {breakdown['gross_salary']:>15,.0f}

{'='*70}
DEDUCTIONS
{'='*70}
"""
        
        if "pension_deduction" in breakdown:
            output += f"Pension (5%)             : Rp {breakdown['pension_deduction']:>15,.0f}\n"
        
        output += f"""Tax (5%)                 : Rp {payslip['tax']:>15,.0f}

{'-'*70}
NET SALARY               : Rp {payslip['final_net_salary']:>15,.0f}
{'='*70}

Attendance: {payslip['attendance_days']} days
"""
        return output
