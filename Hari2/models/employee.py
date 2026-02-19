"""
Employee Model - Base employee class dengan common attributes dan methods.
"""

from datetime import datetime
from abc import abstractmethod
from models.person import Person


class Employee(Person):
    """Base Employee class dengan common attributes dan methods."""
    
    # Class attributes
    company_name = "TechCorp Solutions"
    total_employees = 0
    
    def __init__(self, emp_id, name, email, phone, date_of_birth, 
                 join_date, department, base_salary, position):
        super().__init__(emp_id, name, email, phone, date_of_birth)
        
        self.emp_id = emp_id
        self.join_date = join_date
        self.department = department
        self.base_salary = base_salary
        self.position = position
        self.status = "Active"
        
        # Performance tracking
        self.performance_ratings = []
        
        # Leave management
        self.annual_leave_balance = 12  # days per year
        self.sick_leave_balance = 12
        self.leave_history = []
        
        # Attendance
        self.attendance_records = []
        
        Employee.total_employees += 1
    
    def calculate_tenure(self):
        """Calculate employee tenure in years."""
        join = datetime.strptime(self.join_date, "%Y-%m-%d")
        tenure = datetime.now() - join
        years = tenure.days // 365
        months = (tenure.days % 365) // 30
        return years, months
    
    @abstractmethod
    def calculate_salary(self):
        """Calculate total salary (to be implemented by subclasses)."""
        pass
    
    def add_performance_rating(self, rating, review_date, reviewer, comments=""):
        """Add performance rating (1-5 scale)."""
        if not 1 <= rating <= 5:
            return "❌ Rating harus antara 1-5"
        
        review = {
            "rating": rating,
            "date": review_date,
            "reviewer": reviewer,
            "comments": comments
        }
        self.performance_ratings.append(review)
        return f"✓ Performance rating {rating} added for {self.name}"
    
    def get_average_rating(self):
        """Get average performance rating."""
        if not self.performance_ratings:
            return 0
        return sum(r["rating"] for r in self.performance_ratings) / len(self.performance_ratings)
    
    def request_leave(self, leave_type, start_date, end_date, reason):
        """Request leave."""
        start = datetime.strptime(start_date, "%Y-%m-%d")
        end = datetime.strptime(end_date, "%Y-%m-%d")
        days = (end - start).days + 1
        
        if leave_type == "annual":
            if days > self.annual_leave_balance:
                return f"❌ Saldo cuti tahunan tidak cukup. Tersedia: {self.annual_leave_balance} hari"
            balance_field = "annual_leave_balance"
        elif leave_type == "sick":
            if days > self.sick_leave_balance:
                return f"❌ Saldo cuti sakit tidak cukup. Tersedia: {self.sick_leave_balance} hari"
            balance_field = "sick_leave_balance"
        else:
            return "❌ Tipe cuti tidak valid (annual/sick)"
        
        leave_request = {
            "type": leave_type,
            "start_date": start_date,
            "end_date": end_date,
            "days": days,
            "reason": reason,
            "status": "pending",
            "requested_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        
        self.leave_history.append(leave_request)
        return f"✓ Leave request submitted: {days} days ({leave_type})"
    
    def approve_leave(self, leave_index):
        """Approve leave request."""
        if leave_index >= len(self.leave_history):
            return "❌ Leave request not found"
        
        leave = self.leave_history[leave_index]
        if leave["status"] != "pending":
            return f"❌ Leave already {leave['status']}"
        
        leave["status"] = "approved"
        leave["approved_at"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # Deduct from balance
        if leave["type"] == "annual":
            self.annual_leave_balance -= leave["days"]
        elif leave["type"] == "sick":
            self.sick_leave_balance -= leave["days"]
        
        return f"✓ Leave approved: {leave['days']} days ({leave['type']})"
    
    def clock_in(self, clock_in_time=None):
        """Clock in for attendance."""
        if clock_in_time is None:
            clock_in_time = datetime.now()
        
        # Check if already clocked in today
        today = datetime.now().date()
        for record in self.attendance_records:
            if record["date"] == str(today) and record["clock_in"]:
                return "❌ Already clocked in today"
        
        attendance = {
            "date": str(today),
            "clock_in": clock_in_time.strftime("%H:%M:%S"),
            "clock_out": None,
            "hours_worked": 0,
            "status": "present"
        }
        self.attendance_records.append(attendance)
        return f"✓ Clocked in at {clock_in_time.strftime('%H:%M:%S')}"
    
    def clock_out(self, clock_out_time=None):
        """Clock out for attendance."""
        if clock_out_time is None:
            clock_out_time = datetime.now()
        
        today = str(datetime.now().date())
        
        # Find today's attendance record
        for record in self.attendance_records:
            if record["date"] == today and record["clock_in"] and not record["clock_out"]:
                record["clock_out"] = clock_out_time.strftime("%H:%M:%S")
                
                # Calculate hours worked
                clock_in = datetime.strptime(f"{today} {record['clock_in']}", "%Y-%m-%d %H:%M:%S")
                hours = (clock_out_time - clock_in).total_seconds() / 3600
                record["hours_worked"] = round(hours, 2)
                
                return f"✓ Clocked out at {clock_out_time.strftime('%H:%M:%S')}. Hours worked: {record['hours_worked']}"
        
        return "❌ No clock-in record found for today"
    
    def get_monthly_attendance_summary(self, year, month):
        """Get attendance summary for a specific month."""
        present_days = 0
        total_hours = 0
        
        for record in self.attendance_records:
            record_date = datetime.strptime(record["date"], "%Y-%m-%d")
            if record_date.year == year and record_date.month == month:
                present_days += 1
                total_hours += record["hours_worked"]
        
        return {
            "present_days": present_days,
            "total_hours": total_hours,
            "average_hours": total_hours / present_days if present_days > 0 else 0
        }
    
    def get_info(self):
        """Get employee basic information."""
        years, months = self.calculate_tenure()
        return f"""
{'='*70}
EMPLOYEE INFORMATION
{'='*70}
ID: {self.emp_id}
Name: {self.name}
Email: {self.email}
Phone: {self.phone}
Age: {self.get_age()} years
Position: {self.position}
Department: {self.department}
Status: {self.status}
Join Date: {self.join_date}
Tenure: {years} years {months} months
Base Salary: Rp {self.base_salary:,}
{'='*70}
        """
