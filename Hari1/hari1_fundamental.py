"""
PYTHON FUNDAMENTALS - COMPREHENSIVE GUIDE
==========================================
File ini berisi fundamental Python dengan penjelasan mendalam dan 
contoh studi kasus implementatif di dunia kerja.
"""

# ============================================================================
# 1. KOMENTAR (COMMENTS)
# ============================================================================
"""
PENJELASAN:
Komentar digunakan untuk dokumentasi kode. Tidak dieksekusi oleh Python.
- Single line comment menggunakan #
- Multi-line comment menggunakan triple quotes ''' atau \"\"\"
- Docstring digunakan untuk dokumentasi fungsi, class, dan module

KEGUNAAN DI DUNIA KERJA:
- Dokumentasi kode untuk tim development
- Code review dan maintainability
- API documentation generation
"""

# Ini adalah single line comment
'''
Ini adalah multi-line comment
yang bisa mencakup beberapa baris
'''


# ============================================================================
# 2. PRINT DAN OUTPUT
# ============================================================================
"""
PENJELASAN:
print() adalah fungsi built-in untuk menampilkan output ke console.
Mendukung berbagai tipe data dan formatting.

STUDI KASUS - LOGGING SISTEM:
Di production environment, print() sering diganti dengan logging module
untuk tracking aplikasi dan debugging.
"""

print("=" * 50) #=============================
print("BAGIAN 1: PRINT DAN OUTPUT")
print("=" * 50) #=============================

# Basic print
print("Hello World")

# Print dengan multiple arguments
print("Nama:", "Tomas", "| Umur:", 22)

# Print dengan separator custom
print("Python", "Java", "JavaScript", sep=" | ")

# Print dengan end custom (default end='\n')
print("Loading", end="... ")
print("Done!")

# Formatted string (f-string) - Python 3.6+
nama_user = "Tomas"
umur_user = 22
print(f"Halo {nama_user}, umur kamu {umur_user} tahun")

# Format dengan alignment dan padding
print(f"{'Nama':<15} {'Umur':>5} {'Status':^10}")
print(f"{nama_user:<15} {umur_user:>5} {'Aktif':^10}")


# ============================================================================
# 3. VARIABEL DAN TIPE DATA
# ============================================================================
"""
PENJELASAN:
Python adalah dynamically typed language. Tidak perlu deklarasi tipe data.
Tipe data ditentukan saat runtime berdasarkan value yang di-assign.

TIPE DATA DASAR:
- String (str): Teks, immutable
- Integer (int): Bilangan bulat, unlimited precision
- Float (float): Bilangan desimal, 64-bit precision
- Boolean (bool): True/False
- List (list): Ordered, mutable collection
- Tuple (tuple): Ordered, immutable collection
- Dictionary (dict): Key-value pairs, mutable
- Set (set): Unordered unique elements

STUDI KASUS - EMPLOYEE MANAGEMENT SYSTEM:
"""

print("\n" + "=" * 50)
print("BAGIAN 2: VARIABEL DAN TIPE DATA")
print("=" * 50)

# String - untuk menyimpan data teks seperti nama, alamat, email
nama_karyawan = "Tomas Anderson"
email = "tomas.anderson@company.com"
departemen = "IT"

# Integer - untuk data numerik bulat seperti umur, jumlah hari kerja
umur = 22
jumlah_cuti = 12
tahun_bergabung = 2020

# Float - untuk data numerik desimal seperti gaji, rating performance
gaji_pokok = 8500000.50
rating_performance = 4.5
bonus_persentase = 0.15

# Boolean - untuk status atau flag
is_aktif = True
has_insurance = True
is_remote = False

# List - mutable, untuk data yang sering berubah
skills = ["Python", "SQL", "Docker", "Git"]
project_history = ["ProjectA", "ProjectB", "ProjectC"]

# Tuple - immutable, untuk data yang tidak berubah
koordinat_kantor = (-6.2088, 106.8456)  # Latitude, Longitude Jakarta
tanggal_lahir = (1999, 5, 15)  # (tahun, bulan, tanggal)

# Dictionary - untuk data terstruktur dengan key-value
data_karyawan = {
    "id": "EMP001",
    "nama": nama_karyawan,
    "umur": umur,
    "departemen": departemen,
    "gaji": gaji_pokok,
    "skills": skills,
    "is_aktif": is_aktif
}

# Set - untuk data unik, menghilangkan duplikat
teknologi_digunakan = {"Python", "SQL", "Docker", "Python", "Git"}  # Duplikat dihapus otomatis

print(f"\nData Karyawan: {data_karyawan['nama']}")
print(f"Gaji Pokok: Rp {gaji_pokok:,.2f}")
print(f"Skills: {', '.join(skills)}")
print(f"Teknologi (unique): {teknologi_digunakan}")


# ============================================================================
# 4. TYPE CHECKING DAN CONVERSION
# ============================================================================
"""
PENJELASAN:
Python menyediakan built-in functions untuk cek tipe data dan konversi.
- type(): Mengembalikan tipe data object
- isinstance(): Cek apakah object adalah instance dari class tertentu
- Type conversion: int(), float(), str(), bool(), list(), tuple(), dict()

STUDI KASUS - DATA VALIDATION API:
Saat menerima data dari user input atau API, perlu validasi tipe data.
"""

print("\n" + "=" * 50)
print("BAGIAN 3: TYPE CHECKING DAN CONVERSION")
print("=" * 50)

# Type checking
print(f"Type nama_karyawan: {type(nama_karyawan)}")
print(f"Type umur: {type(umur)}")
print(f"Type gaji_pokok: {type(gaji_pokok)}")
print(f"Type is_aktif: {type(is_aktif)}")
print(f"Type skills: {type(skills)}")
print(f"Type tanggal_lahir: {type(tanggal_lahir)}")
print(f"Type data_karyawan: {type(data_karyawan)}")

# isinstance() - lebih baik untuk type checking
print(f"\nApakah gaji_pokok bertipe float? {isinstance(gaji_pokok, float)}")
print(f"Apakah skills bertipe list? {isinstance(skills, list)}")

# Type conversion - contoh real world: data dari form/API sering berupa string
input_gaji = "9500000"  # String dari form input
input_umur = "25"
input_bonus = "12.5"

# Convert ke tipe yang benar
gaji_converted = float(input_gaji)
umur_converted = int(input_umur)
bonus_converted = float(input_bonus)

print(f"\nSetelah konversi:")
print(f"Gaji: Rp {gaji_converted:,.0f} (tipe: {type(gaji_converted).__name__})")
print(f"Umur: {umur_converted} tahun (tipe: {type(umur_converted).__name__})")
print(f"Bonus: {bonus_converted}% (tipe: {type(bonus_converted).__name__})")


# ============================================================================
# 5. STRING OPERATIONS DAN METHODS
# ============================================================================
"""
PENJELASAN:
String adalah sequence of characters. Python menyediakan banyak built-in methods.

METHODS PENTING:
- len(): Panjang string
- upper(), lower(), title(), capitalize(): Case conversion
- strip(), lstrip(), rstrip(): Menghapus whitespace
- split(), join(): Memisah dan menggabungkan string
- replace(): Mengganti substring
- find(), index(): Mencari substring
- startswith(), endswith(): Cek prefix/suffix
- isdigit(), isalpha(), isalnum(): Validasi karakter

STUDI KASUS - TEXT PROCESSING & DATA CLEANING:
"""

print("\n" + "=" * 50)
print("BAGIAN 4: STRING OPERATIONS")
print("=" * 50)

# Data mentah dari database/input (sering tidak bersih)
raw_data = "  tomas.anderson@COMPANY.com  "
nama_lengkap = "tomas anderson"
kode_produk = "PROD-2024-001"

# Cleaning dan formatting
email_clean = raw_data.strip().lower()  # Hapus whitespace, lowercase
nama_proper = nama_lengkap.title()  # Capitalize each word

print(f"Email bersih: {email_clean}")
print(f"Nama proper: {nama_proper}")
print(f"Panjang nama: {len(nama_proper)} karakter")

# String manipulation untuk business logic
kode_parts = kode_produk.split("-")  # ['PROD', '2024', '001']
tahun_produk = kode_parts[1]
nomor_produk = kode_parts[2]

print(f"\nKode Produk: {kode_produk}")
print(f"Tahun: {tahun_produk}")
print(f"Nomor: {nomor_produk}")

# String validation
nomor_telepon = "081234567890"
if nomor_telepon.isdigit() and len(nomor_telepon) >= 10:
    print(f"\n✓ Nomor telepon valid: {nomor_telepon}")
else:
    print("\n✗ Nomor telepon tidak valid")

# String replacement untuk data masking
kartu_kredit = "1234-5678-9012-3456"
masked_kartu = kartu_kredit[:4] + "-****-****-" + kartu_kredit[-4:]
print(f"Kartu kredit masked: {masked_kartu}")


# ============================================================================
# 6. COLLECTION OPERATIONS (LIST, TUPLE, DICT, SET)
# ============================================================================
"""
PENJELASAN:
Collections adalah struktur data untuk menyimpan multiple items.

LIST: Mutable, ordered, allows duplicates
- Append, insert, remove, pop, sort, reverse
- List comprehension untuk transformasi data

TUPLE: Immutable, ordered, allows duplicates
- Lebih cepat dari list, digunakan untuk data konstan

DICTIONARY: Key-value pairs, mutable, no duplicate keys
- Fast lookup O(1), ideal untuk mapping dan caching

SET: Unordered, unique elements, mutable
- Union, intersection, difference untuk operasi set
- Menghilangkan duplikat

STUDI KASUS - DATA PROCESSING PIPELINE:
"""

print("\n" + "=" * 50)
print("BAGIAN 5: COLLECTION OPERATIONS")
print("=" * 50)

# LIST - Employee management
karyawan_aktif = ["Tomas", "John", "Sarah", "Mike"]
print(f"Karyawan aktif: {karyawan_aktif}")
print(f"Jumlah: {len(karyawan_aktif)}")

# List methods
karyawan_aktif.append("Lisa")  # Tambah di akhir
karyawan_aktif.insert(0, "Boss")  # Tambah di index 0
print(f"Setelah tambah: {karyawan_aktif}")

karyawan_keluar = karyawan_aktif.pop()  # Hapus terakhir
print(f"{karyawan_keluar} keluar. Sisa: {karyawan_aktif}")

# List comprehension - filtering dan transformasi
gaji_bulanan = [5000000, 7500000, 6000000, 8000000, 5500000]
gaji_diatas_6jt = [g for g in gaji_bulanan if g > 6000000]
gaji_tahunan = [g * 12 for g in gaji_bulanan]

print(f"\nGaji di atas 6jt: {gaji_diatas_6jt}")
print(f"Total gaji tahunan: Rp {sum(gaji_tahunan):,}")

# TUPLE - Database query result (immutable)
employee_record = ("EMP001", "Tomas", "IT", 8500000)
emp_id, emp_name, emp_dept, emp_salary = employee_record  # Unpacking
print(f"\nEmployee: {emp_name} ({emp_id}) - {emp_dept}")

# DICTIONARY - Configuration dan mapping
salary_grades = {
    "Junior": (5000000, 7000000),
    "Middle": (7000000, 10000000),
    "Senior": (10000000, 15000000),
    "Lead": (15000000, 25000000)
}

employee_data = {
    "EMP001": {"nama": "Tomas", "grade": "Middle", "departemen": "IT"},
    "EMP002": {"nama": "Sarah", "grade": "Senior", "departemen": "Finance"},
    "EMP003": {"nama": "Mike", "grade": "Junior", "departemen": "IT"}
}

# Dictionary operations
print("\n--- Salary Ranges ---")
for grade, (min_sal, max_sal) in salary_grades.items():
    print(f"{grade}: Rp {min_sal:,} - Rp {max_sal:,}")

# Nested dictionary access
print("\n--- Employee Details ---")
for emp_id, details in employee_data.items():
    grade = details["grade"]
    sal_range = salary_grades[grade]
    print(f"{emp_id}: {details['nama']} - {grade} (Rp {sal_range[0]:,} - Rp {sal_range[1]:,})")

# Dictionary methods
print(f"\nApakah EMP001 ada? {'EMP001' in employee_data}")
print(f"Keys: {list(employee_data.keys())}")
print(f"Total employees: {len(employee_data)}")

# SET - Unique operations
dept_it = {"Tomas", "John", "Mike", "Sarah"}
dept_finance = {"Sarah", "Lisa", "David"}
dept_hr = {"Mike", "Anna", "Tom"}

# Set operations for analysis
all_employees = dept_it | dept_finance | dept_hr  # Union
multi_dept = (dept_it & dept_finance) | (dept_it & dept_hr)  # Intersection
only_it = dept_it - dept_finance - dept_hr  # Difference

print(f"\n--- Department Analysis ---")
print(f"Total unique employees: {len(all_employees)}")
print(f"Multi-department: {multi_dept}")
print(f"Hanya IT: {only_it}")


# ============================================================================
# 7. OPERASI ARITMATIKA
# ============================================================================
"""
PENJELASAN:
Python mendukung semua operasi matematika dasar dan advanced.

OPERATOR:
+ : Penjumlahan
- : Pengurangan
* : Perkalian
/ : Pembagian (float result)
// : Floor division (integer result)
% : Modulus (sisa bagi)
** : Pangkat

STUDI KASUS - PAYROLL CALCULATION SYSTEM:
"""

print("\n" + "=" * 50)
print("BAGIAN 6: OPERASI ARITMATIKA - PAYROLL SYSTEM")
print("=" * 50)

# Data karyawan
gaji_pokok_monthly = 8500000
jam_lembur = 15  # jam
rate_lembur_per_jam = 50000
bonus_performance = 0.10  # 10%
potongan_pajak = 0.05  # 5% PPh21
potongan_bpjs = 200000

# Perhitungan payroll
upah_lembur = jam_lembur * rate_lembur_per_jam
bonus = gaji_pokok_monthly * bonus_performance
total_pendapatan = gaji_pokok_monthly + upah_lembur + bonus

pajak = total_pendapatan * potongan_pajak
total_potongan = pajak + potongan_bpjs
gaji_bersih = total_pendapatan - total_potongan

print(f"Gaji Pokok       : Rp {gaji_pokok_monthly:>12,}")
print(f"Upah Lembur      : Rp {upah_lembur:>12,} ({jam_lembur} jam x Rp {rate_lembur_per_jam:,})")
print(f"Bonus Performance: Rp {bonus:>12,.0f} ({bonus_performance*100}%)")
print(f"{'-'*40}")
print(f"Total Pendapatan : Rp {total_pendapatan:>12,.0f}")
print(f"\nPotongan Pajak   : Rp {pajak:>12,.0f} ({potongan_pajak*100}%)")
print(f"BPJS             : Rp {potongan_bpjs:>12,}")
print(f"{'-'*40}")
print(f"GAJI BERSIH      : Rp {gaji_bersih:>12,.0f}")

# Floor division dan modulus untuk time calculation
total_menit_kerja = 2450  # menit dalam sebulan
jam_kerja = total_menit_kerja // 60  # Floor division
sisa_menit = total_menit_kerja % 60  # Modulus

print(f"\nTotal waktu kerja: {jam_kerja} jam {sisa_menit} menit")

# Pangkat untuk compound interest calculation
modal_awal = 10000000  # 10 juta
bunga_tahunan = 0.08  # 8% per tahun
tahun = 5
modal_akhir = modal_awal * ((1 + bunga_tahunan) ** tahun)

print(f"\nInvestasi setelah {tahun} tahun: Rp {modal_akhir:,.0f}")
print(f"Keuntungan: Rp {modal_akhir - modal_awal:,.0f}")


# ============================================================================
# 8. OPERATOR PERBANDINGAN DAN LOGIKA
# ============================================================================
"""
PENJELASAN:
Operator perbandingan mengembalikan Boolean (True/False).

PERBANDINGAN:
==, !=, <, >, <=, >=

LOGIKA:
and : Kedua kondisi True
or  : Salah satu kondisi True
not : Negasi (kebalikan)

STUDI KASUS - ACCESS CONTROL & BUSINESS LOGIC:
"""

print("\n" + "=" * 50)
print("BAGIAN 7: OPERATOR PERBANDINGAN DAN LOGIKA")
print("=" * 50)

# User authentication dan authorization
username = "tomas"
password = "securepass123"
is_logged_in = True
user_role = "admin"
account_age_days = 45

# Perbandingan
is_valid_username = len(username) >= 5
is_strong_password = len(password) >= 8
is_new_account = account_age_days < 30

print(f"Username valid: {is_valid_username}")
print(f"Password kuat: {is_strong_password}")
print(f"Akun baru: {is_new_account}")

# Logika AND - semua kondisi harus true
can_access_admin_panel = is_logged_in and user_role == "admin"
print(f"\nAkses admin panel: {can_access_admin_panel}")

# Logika OR - salah satu kondisi true
can_edit_document = user_role == "admin" or user_role == "editor"
print(f"Bisa edit dokumen: {can_edit_document}")

# Logika NOT - negasi
is_restricted = not is_logged_in
print(f"Akses terbatas: {is_restricted}")

# Complex business logic
gaji = 9000000
tahun_pengalaman = 3
has_certification = True

# Kriteria promosi: gaji >= 8jt DAN (pengalaman > 2 tahun ATAU punya sertifikasi)
eligible_for_promotion = gaji >= 8000000 and (tahun_pengalaman > 2 or has_certification)
print(f"\nEligible untuk promosi: {eligible_for_promotion}")

# Membership checking dengan 'in'
allowed_departments = ["IT", "Finance", "HR"]
user_department = "IT"
has_department_access = user_department in allowed_departments
print(f"Akses departemen: {has_department_access}")


# ============================================================================
# 9. CONDITIONAL STATEMENTS (IF-ELIF-ELSE)
# ============================================================================
"""
PENJELASAN:
Control flow untuk menjalankan code berdasarkan kondisi tertentu.

SYNTAX:
if condition:
    # code jika True
elif another_condition:
    # code jika condition pertama False dan ini True
else:
    # code jika semua False

STUDI KASUS - EMPLOYEE PERFORMANCE GRADING:
"""

print("\n" + "=" * 50)
print("BAGIAN 8: CONDITIONAL STATEMENTS")
print("=" * 50)

# Performance grading system
performance_score = 85  # Score 0-100
attendance_rate = 95  # Percentage
project_completed = 8

print(f"Performance Score: {performance_score}")
print(f"Attendance Rate: {attendance_rate}%")
print(f"Projects Completed: {project_completed}")

# Multi-level grading
if performance_score >= 90 and attendance_rate >= 95:
    grade = "A - Outstanding"
    bonus_multiplier = 1.5
elif performance_score >= 80 and attendance_rate >= 90:
    grade = "B - Excellent"
    bonus_multiplier = 1.2
elif performance_score >= 70 and attendance_rate >= 85:
    grade = "C - Good"
    bonus_multiplier = 1.0
elif performance_score >= 60:
    grade = "D - Satisfactory"
    bonus_multiplier = 0.5
else:
    grade = "E - Needs Improvement"
    bonus_multiplier = 0.0

print(f"\nPerformance Grade: {grade}")
print(f"Bonus Multiplier: {bonus_multiplier}x")

# Nested conditions untuk complex business rules
base_salary = 8000000

if grade.startswith("A") or grade.startswith("B"):
    if project_completed >= 10:
        total_bonus = base_salary * bonus_multiplier * 1.2  # Extra 20%
        print(f"🎉 Bonus dengan extra project: Rp {total_bonus:,.0f}")
    else:
        total_bonus = base_salary * bonus_multiplier
        print(f"✓ Bonus standar: Rp {total_bonus:,.0f}")
else:
    total_bonus = base_salary * bonus_multiplier
    print(f"Bonus: Rp {total_bonus:,.0f}")

# Ternary operator (one-line if-else)
status = "APPROVED" if total_bonus > 0 else "NO BONUS"
print(f"Status: {status}")


# ============================================================================
# 10. LOOPS - FOR DAN WHILE
# ============================================================================
"""
PENJELASAN:
Loops untuk menjalankan code berulang kali.

FOR LOOP:
- Iterate over sequence (list, tuple, string, range)
- Digunakan saat tahu berapa kali iterasi

WHILE LOOP:
- Berjalan selama kondisi True
- Digunakan saat tidak tahu pasti berapa kali iterasi

CONTROL STATEMENTS:
- break: Keluar dari loop
- continue: Skip iterasi saat ini, lanjut ke berikutnya
- else: Dieksekusi jika loop selesai normal (tanpa break)

STUDI KASUS - BATCH PROCESSING & REPORT GENERATION:
"""

print("\n" + "=" * 50)
print("BAGIAN 9: LOOPS - BATCH PROCESSING")
print("=" * 50)

# FOR LOOP - Processing employee list
employees = [
    {"id": "EMP001", "nama": "Tomas", "departemen": "IT", "gaji": 8500000},
    {"id": "EMP002", "nama": "Sarah", "departemen": "Finance", "gaji": 9000000},
    {"id": "EMP003", "nama": "Mike", "departemen": "IT", "gaji": 7500000},
    {"id": "EMP004", "nama": "Lisa", "departemen": "HR", "gaji": 8000000},
    {"id": "EMP005", "nama": "David", "departemen": "Finance", "gaji": 9500000},
]

print("--- Laporan Gaji Karyawan ---")
total_payroll = 0

for idx, emp in enumerate(employees, start=1):
    total_payroll += emp["gaji"]
    print(f"{idx}. {emp['id']}: {emp['nama']:<10} - {emp['departemen']:<10} - Rp {emp['gaji']:>10,}")

print(f"\nTotal Payroll: Rp {total_payroll:,}")
print(f"Rata-rata Gaji: Rp {total_payroll / len(employees):,.0f}")

# FOR LOOP dengan range - Generating invoice numbers
print("\n--- Generate Invoice Numbers ---")
tahun = 2024
bulan = 2  # Februari

for nomor in range(1, 6):  # Generate 5 invoice
    invoice_number = f"INV-{tahun}{bulan:02d}-{nomor:04d}"
    print(f"Invoice: {invoice_number}")

# List comprehension dengan condition - Filtering
print("\n--- Filter IT Department ---")
it_employees = [emp for emp in employees if emp["departemen"] == "IT"]
for emp in it_employees:
    print(f"- {emp['nama']} (Gaji: Rp {emp['gaji']:,})")

# WHILE LOOP - Process queue (misal: job queue)
print("\n--- Processing Job Queue ---")
job_queue = ["Job1", "Job2", "Job3", "Job4", "Job5"]
max_retry = 3

while job_queue:
    current_job = job_queue.pop(0)  # Ambil job pertama
    print(f"Processing: {current_job}")
    
    # Simulasi: Job3 gagal, perlu retry
    if current_job == "Job3" and max_retry > 0:
        print(f"  ⚠ {current_job} failed, retrying... (retry left: {max_retry})")
        job_queue.append(current_job)  # Masukkan kembali ke queue
        max_retry -= 1
        continue
    
    print(f"  ✓ {current_job} completed")

# WHILE dengan break - User session timeout
print("\n--- Session Timeout Simulation ---")
session_duration = 0
max_session_time = 10  # minutes

while True:
    session_duration += 1
    print(f"Session active: {session_duration} minutes")
    
    if session_duration >= max_session_time:
        print("⏱ Session timeout! Please login again.")
        break
    
    # Simulasi: user activity setiap 3 menit memperpanjang session
    if session_duration % 3 == 0:
        print("  👤 User activity detected, session extended")


# ============================================================================
# 11. FUNCTIONS (FUNGSI)
# ============================================================================
"""
PENJELASAN:
Function adalah block code reusable yang melakukan tugas spesifik.

KEUNTUNGAN:
- Code reusability
- Modularity dan organization
- Easier testing dan debugging
- Abstraction

COMPONENTS:
- def: Keyword untuk define function
- Parameters: Input ke function
- Return: Output dari function
- Docstring: Dokumentasi function

PARAMETER TYPES:
- Positional parameters
- Default parameters
- Keyword arguments
- *args: Variable positional arguments
- **kwargs: Variable keyword arguments

STUDI KASUS - BUSINESS LOGIC FUNCTIONS:
"""

print("\n" + "=" * 50)
print("BAGIAN 10: FUNCTIONS")
print("=" * 50)

# Basic function
def calculate_annual_salary(monthly_salary):
    """
    Menghitung gaji tahunan dari gaji bulanan.
    
    Args:
        monthly_salary (float): Gaji bulanan
        
    Returns:
        float: Gaji tahunan
    """
    return monthly_salary * 12

# Test basic function
gaji_bulanan = 8500000
gaji_tahunan = calculate_annual_salary(gaji_bulanan)
print(f"Gaji Bulanan: Rp {gaji_bulanan:,}")
print(f"Gaji Tahunan: Rp {gaji_tahunan:,}")


# Function dengan multiple parameters dan default values
def calculate_total_compensation(base_salary, bonus_percentage=0.1, allowance=0, overtime_hours=0, overtime_rate=50000):
    """
    Menghitung total kompensasi karyawan.
    
    Args:
        base_salary (float): Gaji pokok
        bonus_percentage (float): Persentase bonus (default 10%)
        allowance (float): Tunjangan tetap (default 0)
        overtime_hours (int): Jam lembur (default 0)
        overtime_rate (float): Rate per jam lembur (default 50000)
        
    Returns:
        dict: Dictionary berisi breakdown kompensasi
    """
    bonus = base_salary * bonus_percentage
    overtime_pay = overtime_hours * overtime_rate
    total = base_salary + bonus + allowance + overtime_pay
    
    return {
        "base_salary": base_salary,
        "bonus": bonus,
        "allowance": allowance,
        "overtime_pay": overtime_pay,
        "total": total
    }

# Test dengan berbagai cara pemanggilan
print("\n--- Total Compensation Calculation ---")

# Menggunakan default values
comp1 = calculate_total_compensation(8000000)
print(f"\nKaryawan 1 (default bonus):")
print(f"  Total: Rp {comp1['total']:,}")

# Dengan keyword arguments
comp2 = calculate_total_compensation(
    base_salary=9000000,
    bonus_percentage=0.15,
    allowance=1000000,
    overtime_hours=10
)
print(f"\nKaryawan 2 (custom parameters):")
print(f"  Base: Rp {comp2['base_salary']:,}")
print(f"  Bonus: Rp {comp2['bonus']:,}")
print(f"  Allowance: Rp {comp2['allowance']:,}")
print(f"  Overtime: Rp {comp2['overtime_pay']:,}")
print(f"  Total: Rp {comp2['total']:,}")


# Function dengan *args dan **kwargs
def generate_employee_report(employee_name, *achievements, **details):
    """
    Generate laporan karyawan dengan achievements dan details dinamis.
    
    Args:
        employee_name (str): Nama karyawan
        *achievements: Variable positional arguments untuk achievements
        **details: Variable keyword arguments untuk detail tambahan
    """
    print(f"\n{'='*50}")
    print(f"EMPLOYEE REPORT: {employee_name.upper()}")
    print(f"{'='*50}")
    
    if achievements:
        print("\nAchievements:")
        for i, achievement in enumerate(achievements, 1):
            print(f"  {i}. {achievement}")
    
    if details:
        print("\nAdditional Details:")
        for key, value in details.items():
            print(f"  {key.replace('_', ' ').title()}: {value}")

# Test *args dan **kwargs
generate_employee_report(
    "Tomas Anderson",
    "Completed 10 projects",
    "Led team of 5 developers",
    "Reduced bug rate by 30%",
    department="IT",
    years_of_service=3,
    rating="A",
    skills="Python, SQL, Docker"
)


# Lambda functions (anonymous functions)
# Berguna untuk operations singkat dan one-time use
print("\n--- Lambda Functions ---")

employees_data = [
    {"nama": "Tomas", "gaji": 8500000},
    {"nama": "Sarah", "gaji": 9000000},
    {"nama": "Mike", "gaji": 7500000},
    {"nama": "Lisa", "gaji": 8000000},
]

# Sort by salary using lambda
sorted_by_salary = sorted(employees_data, key=lambda emp: emp["gaji"], reverse=True)
print("\nEmployees sorted by salary (highest first):")
for emp in sorted_by_salary:
    print(f"  {emp['nama']}: Rp {emp['gaji']:,}")

# Map function dengan lambda - apply tax calculation
tax_rate = 0.05
salaries_after_tax = list(map(lambda emp: {
    "nama": emp["nama"],
    "gaji_bersih": emp["gaji"] * (1 - tax_rate)
}, employees_data))

print(f"\nSalaries after {tax_rate*100}% tax:")
for emp in salaries_after_tax:
    print(f"  {emp['nama']}: Rp {emp['gaji_bersih']:,.0f}")


# ============================================================================
# 12. EXCEPTION HANDLING
# ============================================================================
"""
PENJELASAN:
Exception handling untuk menangani error dan prevent program crash.

TRY-EXCEPT STRUCTURE:
- try: Code yang mungkin menimbulkan error
- except: Code yang dieksekusi jika error terjadi
- else: Dieksekusi jika tidak ada error
- finally: Selalu dieksekusi (cleanup operations)

COMMON EXCEPTIONS:
- ValueError: Invalid value conversion
- TypeError: Wrong type operation
- KeyError: Dictionary key not found
- IndexError: List index out of range
- FileNotFoundError: File tidak ditemukan
- ZeroDivisionError: Division by zero

STUDI KASUS - ROBUST API & USER INPUT HANDLING:
"""

print("\n" + "=" * 50)
print("BAGIAN 11: EXCEPTION HANDLING")
print("=" * 50)

# Example 1: Handling division by zero
def calculate_average_salary(total_salary, num_employees):
    """Calculate average salary dengan error handling."""
    try:
        average = total_salary / num_employees
        return average
    except ZeroDivisionError:
        print("Error: Tidak ada karyawan untuk dihitung rata-rata")
        return 0
    except TypeError:
        print("Error: Input harus berupa angka")
        return 0

print("--- Division Error Handling ---")
avg1 = calculate_average_salary(50000000, 5)
print(f"Rata-rata gaji (5 karyawan): Rp {avg1:,.0f}")

avg2 = calculate_average_salary(50000000, 0)  # Zero division
print(f"Rata-rata gaji (0 karyawan): Rp {avg2:,.0f}")


# Example 2: Data validation dengan multiple exceptions
def process_employee_data(emp_data):
    """
    Process employee data dengan comprehensive error handling.
    """
    try:
        emp_id = emp_data["id"]
        emp_name = emp_data["nama"]
        emp_salary = float(emp_data["gaji"])  # Bisa raise ValueError
        emp_department = emp_data.get("departemen", "Unknown")  # Safe get
        
        print(f"\n✓ Processing: {emp_id} - {emp_name}")
        print(f"  Department: {emp_department}")
        print(f"  Salary: Rp {emp_salary:,.0f}")
        
        return True
        
    except KeyError as e:
        print(f"\n✗ Error: Missing required field {e}")
        return False
    except ValueError as e:
        print(f"\n✗ Error: Invalid salary value - {e}")
        return False
    except Exception as e:
        print(f"\n✗ Error: Unexpected error - {e}")
        return False
    finally:
        # Cleanup atau logging operation
        print(f"  [Log] Processed data at {__import__('datetime').datetime.now()}")

print("\n--- Data Validation Examples ---")

# Valid data
valid_emp = {"id": "EMP001", "nama": "Tomas", "gaji": "8500000", "departemen": "IT"}
process_employee_data(valid_emp)

# Missing key
invalid_emp1 = {"id": "EMP002", "nama": "Sarah"}  # Missing 'gaji'
process_employee_data(invalid_emp1)

# Invalid value
invalid_emp2 = {"id": "EMP003", "nama": "Mike", "gaji": "invalid"}  # Invalid gaji
process_employee_data(invalid_emp2)


# Example 3: Custom exception
class InsufficientBalanceError(Exception):
    """Custom exception untuk insufficient balance."""
    pass

def process_payment(balance, amount):
    """
    Process payment dengan custom exception.
    """
    try:
        if amount <= 0:
            raise ValueError("Amount harus lebih dari 0")
        
        if amount > balance:
            raise InsufficientBalanceError(f"Saldo tidak cukup. Saldo: Rp {balance:,}, Tagihan: Rp {amount:,}")
        
        new_balance = balance - amount
        print(f"✓ Pembayaran berhasil: Rp {amount:,}")
        print(f"  Sisa saldo: Rp {new_balance:,}")
        return new_balance
        
    except InsufficientBalanceError as e:
        print(f"✗ {e}")
        return balance
    except ValueError as e:
        print(f"✗ Error: {e}")
        return balance

print("\n--- Payment Processing ---")
saldo = 10000000
saldo = process_payment(saldo, 5000000)  # Success
saldo = process_payment(saldo, 8000000)  # Insufficient
saldo = process_payment(saldo, -1000)    # Invalid amount


# ============================================================================
# 13. MODULES DAN IMPORTS
# ============================================================================
"""
PENJELASAN:
Module adalah file Python yang berisi functions, classes, dan variables.
Import digunakan untuk menggunakan code dari module lain.

IMPORT STYLES:
- import module
- from module import function
- from module import *
- import module as alias

STANDARD LIBRARY MODULES:
- math: Mathematical operations
- datetime: Date and time operations
- random: Random number generation
- os: Operating system interface
- json: JSON encoding/decoding
- re: Regular expressions

STUDI KASUS - REAL BUSINESS OPERATIONS:
"""

print("\n" + "=" * 50)
print("BAGIAN 12: MODULES DAN IMPORTS")
print("=" * 50)

# Math module untuk financial calculations
import math

def calculate_loan_payment(principal, annual_rate, years):
    """
    Menghitung cicilan bulanan kredit (EMI - Equated Monthly Installment).
    
    Formula: EMI = [P x R x (1+R)^N] / [(1+R)^N-1]
    """
    monthly_rate = annual_rate / 12 / 100
    num_payments = years * 12
    
    if monthly_rate == 0:
        return principal / num_payments
    
    emi = (principal * monthly_rate * math.pow(1 + monthly_rate, num_payments)) / \
          (math.pow(1 + monthly_rate, num_payments) - 1)
    
    return emi

print("--- Loan Calculator ---")
loan_amount = 300000000  # 300 juta
interest_rate = 8  # 8% per tahun
loan_years = 15

monthly_payment = calculate_loan_payment(loan_amount, interest_rate, loan_years)
total_payment = monthly_payment * loan_years * 12
total_interest = total_payment - loan_amount

print(f"Pinjaman: Rp {loan_amount:,}")
print(f"Bunga: {interest_rate}% per tahun")
print(f"Tenor: {loan_years} tahun")
print(f"\nCicilan per bulan: Rp {monthly_payment:,.0f}")
print(f"Total pembayaran: Rp {total_payment:,.0f}")
print(f"Total bunga: Rp {total_interest:,.0f}")


# Datetime module untuk time-based operations
from datetime import datetime, timedelta

print("\n--- Date & Time Operations ---")

# Current date and time
now = datetime.now()
print(f"Current datetime: {now.strftime('%Y-%m-%d %H:%M:%S')}")

# Calculate employee tenure
hire_date = datetime(2020, 3, 15)
tenure = now - hire_date
years = tenure.days // 365
months = (tenure.days % 365) // 30

print(f"\nHire date: {hire_date.strftime('%Y-%m-%d')}")
print(f"Tenure: {years} tahun {months} bulan")

# Calculate deadline
project_start = datetime.now()
project_duration = 90  # days
deadline = project_start + timedelta(days=project_duration)

print(f"\nProject start: {project_start.strftime('%Y-%m-%d')}")
print(f"Deadline: {deadline.strftime('%Y-%m-%d')}")
print(f"Days until deadline: {(deadline - now).days}")


# Random module untuk sampling dan testing
import random

print("\n--- Random Sampling ---")

# Random employee selection untuk audit
all_employees = ["EMP001", "EMP002", "EMP003", "EMP004", "EMP005", 
                 "EMP006", "EMP007", "EMP008", "EMP009", "EMP010"]

# Select 3 random employees untuk random audit
audit_sample = random.sample(all_employees, 3)
print(f"Random audit sample: {audit_sample}")

# Random assignment
projects = ["ProjectA", "ProjectB", "ProjectC"]
assigned_project = random.choice(projects)
print(f"Assigned project: {assigned_project}")


# ============================================================================
# 14. FILE HANDLING
# ============================================================================
"""
PENJELASAN:
File handling untuk read/write data ke files.

MODES:
- 'r': Read (default)
- 'w': Write (overwrite)
- 'a': Append
- 'r+': Read and write
- 'b': Binary mode

BEST PRACTICES:
- Gunakan context manager (with statement) untuk auto close file
- Handle exceptions untuk file not found, permission error, etc.
- Use proper encoding (utf-8)

STUDI KASUS - DATA EXPORT & LOG FILES:
"""

print("\n" + "=" * 50)
print("BAGIAN 13: FILE HANDLING")
print("=" * 50)

# Example 1: Export employee report to text file
employees_export = [
    {"id": "EMP001", "nama": "Tomas", "departemen": "IT", "gaji": 8500000},
    {"id": "EMP002", "nama": "Sarah", "departemen": "Finance", "gaji": 9000000},
    {"id": "EMP003", "nama": "Mike", "departemen": "IT", "gaji": 7500000},
]

# Write to file
report_filename = "employee_report.txt"
try:
    with open(report_filename, "w", encoding="utf-8") as file:
        file.write("=" * 60 + "\n")
        file.write("LAPORAN KARYAWAN\n")
        file.write("Tanggal: " + datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n")
        file.write("=" * 60 + "\n\n")
        
        for emp in employees_export:
            file.write(f"ID: {emp['id']}\n")
            file.write(f"Nama: {emp['nama']}\n")
            file.write(f"Departemen: {emp['departemen']}\n")
            file.write(f"Gaji: Rp {emp['gaji']:,}\n")
            file.write("-" * 60 + "\n")
        
        total_gaji = sum(emp["gaji"] for emp in employees_export)
        file.write(f"\nTotal Payroll: Rp {total_gaji:,}\n")
    
    print(f"✓ Report berhasil di-export ke {report_filename}")
except IOError as e:
    print(f"✗ Error writing file: {e}")

# Read from file
try:
    with open(report_filename, "r", encoding="utf-8") as file:
        content = file.read()
        print(f"\n--- Content of {report_filename} ---")
        print(content)
except FileNotFoundError:
    print(f"✗ File {report_filename} tidak ditemukan")
except IOError as e:
    print(f"✗ Error reading file: {e}")


# Example 2: Append to log file
log_filename = "system_log.txt"
def write_log(message, level="INFO"):
    """Write log entry ke file."""
    try:
        with open(log_filename, "a", encoding="utf-8") as file:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            log_entry = f"[{timestamp}] [{level}] {message}\n"
            file.write(log_entry)
        return True
    except IOError as e:
        print(f"✗ Error writing log: {e}")
        return False

# Write some logs
write_log("System started", "INFO")
write_log("User 'tomas' logged in", "INFO")
write_log("Processing payroll for 50 employees", "INFO")
write_log("Database connection failed", "ERROR")
write_log("Payroll processing completed", "INFO")

print(f"\n✓ Logs written to {log_filename}")

# Read and display logs
try:
    with open(log_filename, "r", encoding="utf-8") as file:
        lines = file.readlines()
        print(f"\n--- Last 5 Log Entries ---")
        for line in lines[-5:]:  # Display last 5 entries
            print(line.strip())
except FileNotFoundError:
    print(f"✗ Log file tidak ditemukan")


# Example 3: CSV-like data handling
csv_filename = "employees.csv"
try:
    # Write CSV
    with open(csv_filename, "w", encoding="utf-8") as file:
        # Header
        file.write("ID,Nama,Departemen,Gaji\n")
        # Data
        for emp in employees_export:
            file.write(f"{emp['id']},{emp['nama']},{emp['departemen']},{emp['gaji']}\n")
    
    print(f"\n✓ CSV data exported to {csv_filename}")
    
    # Read CSV
    with open(csv_filename, "r", encoding="utf-8") as file:
        lines = file.readlines()
        print(f"\n--- CSV Content ---")
        for line in lines:
            print(line.strip())
            
except IOError as e:
    print(f"✗ Error handling CSV: {e}")


# ============================================================================
# 15. BEST PRACTICES SUMMARY
# ============================================================================
"""
BEST PRACTICES UNTUK PRODUCTION CODE:

1. NAMING CONVENTIONS:
   - snake_case untuk variables dan functions
   - PascalCase untuk classes
   - UPPER_CASE untuk constants
   - Descriptive names (calculate_salary bukan calc_sal)

2. CODE ORGANIZATION:
   - Gunakan functions untuk reusable code
   - Kelompokkan related functions
   - Pisahkan business logic dari presentation

3. ERROR HANDLING:
   - Selalu handle expected errors
   - Provide meaningful error messages
   - Log errors untuk debugging

4. DOCUMENTATION:
   - Write docstrings untuk functions/classes
   - Comment complex logic
   - Keep comments up-to-date

5. PERFORMANCE:
   - Use list comprehension untuk simple iterations
   - Avoid nested loops when possible
   - Use appropriate data structures

6. SECURITY:
   - Validate all user input
   - Don't expose sensitive data in logs
   - Use environment variables untuk credentials

7. TESTING:
   - Write unit tests
   - Test edge cases
   - Test error handling

CONTOH IMPLEMENTASI:
"""

print("\n" + "=" * 50)
print("BAGIAN 14: BEST PRACTICES EXAMPLE")
print("=" * 50)

# Constants
MAX_SALARY = 50000000
MIN_SALARY = 5000000
TAX_RATE = 0.05

# Clean, reusable function dengan proper documentation
def validate_and_calculate_payroll(employee_data):
    """
    Validate employee data dan calculate payroll.
    
    Args:
        employee_data (dict): Dictionary dengan keys: id, nama, gaji
        
    Returns:
        dict: Payroll information atau None jika invalid
        
    Raises:
        ValueError: Jika gaji di luar range
    """
    # Input validation
    required_fields = ["id", "nama", "gaji"]
    for field in required_fields:
        if field not in employee_data:
            write_log(f"Missing field: {field}", "ERROR")
            return None
    
    try:
        salary = float(employee_data["gaji"])
        
        # Business rule validation
        if salary < MIN_SALARY or salary > MAX_SALARY:
            raise ValueError(f"Gaji harus antara Rp {MIN_SALARY:,} - Rp {MAX_SALARY:,}")
        
        # Calculate
        tax = salary * TAX_RATE
        net_salary = salary - tax
        
        result = {
            "employee_id": employee_data["id"],
            "employee_name": employee_data["nama"],
            "gross_salary": salary,
            "tax": tax,
            "net_salary": net_salary,
            "processed_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        
        write_log(f"Payroll processed for {employee_data['id']}", "INFO")
        return result
        
    except ValueError as e:
        write_log(f"Validation error: {e}", "ERROR")
        return None
    except Exception as e:
        write_log(f"Unexpected error: {e}", "ERROR")
        return None

# Test function dengan berbagai cases
test_employees = [
    {"id": "EMP001", "nama": "Tomas", "gaji": 8500000},  # Valid
    {"id": "EMP002", "nama": "Sarah"},  # Missing gaji
    {"id": "EMP003", "nama": "Mike", "gaji": 60000000},  # Too high
    {"id": "EMP004", "nama": "Lisa", "gaji": 7500000},  # Valid
]

print("\n--- Payroll Processing Results ---")
for emp in test_employees:
    result = validate_and_calculate_payroll(emp)
    if result:
        print(f"\n✓ {result['employee_id']}: {result['employee_name']}")
        print(f"  Gross: Rp {result['gross_salary']:,.0f}")
        print(f"  Tax: Rp {result['tax']:,.0f}")
        print(f"  Net: Rp {result['net_salary']:,.0f}")
    else:
        print(f"\n✗ Failed to process: {emp.get('id', 'Unknown')}")


# ============================================================================
# PENUTUP
# ============================================================================
print("\n" + "=" * 50)
print("SELESAI - PYTHON FUNDAMENTALS")
print("=" * 50)
print("""
File ini mencakup:
✓ Print dan Output Formatting
✓ Variabel dan Tipe Data (String, Int, Float, Boolean, List, Tuple, Dict, Set)
✓ Type Checking dan Conversion
✓ String Operations dan Methods
✓ Collection Operations (List, Tuple, Dictionary, Set)
✓ Operasi Aritmatika
✓ Operator Perbandingan dan Logika
✓ Conditional Statements (if-elif-else)
✓ Loops (for, while) dengan break, continue, else
✓ Functions (basic, default params, *args, **kwargs, lambda)
✓ Exception Handling (try-except-else-finally)
✓ Modules dan Imports (math, datetime, random)
✓ File Handling (read, write, append)
✓ Best Practices untuk Production Code

Setiap bagian dilengkapi dengan:
- Penjelasan mendalam tentang konsep
- Contoh implementasi real-world
- Studi kasus dari dunia kerja
- Best practices dan patterns

Happy coding! 🚀
""")






