"""
🚀 QUICK START - PAYROLL API

Script untuk menjalankan Payroll API dengan mudah
"""

import subprocess
import sys
import os

def main():
    print("=" * 60)
    print("🚀 PAYROLL MANAGEMENT API")
    print("=" * 60)
    print()
    
    # Check if in correct directory
    if not os.path.exists("app/main.py"):
        print("❌ Error: Tidak menemukan app/main.py")
        print("   Jalankan script ini dari folder: 03_mini_project_payroll_api/")
        return
    
    # Check dependencies
    print("📦 Checking dependencies...")
    try:
        import fastapi
        import uvicorn
        import pydantic
        print("✅ All dependencies installed!")
    except ImportError as e:
        print(f"❌ Missing dependency: {e}")
        print()
        print("📥 Installing dependencies...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("✅ Dependencies installed!")
    
    print()
    print("=" * 60)
    print("🌐 Starting API Server...")
    print("=" * 60)
    print()
    print("📍 API akan berjalan di: http://localhost:8000")
    print("📖 Dokumentasi (Swagger): http://localhost:8000/docs")
    print("📖 Dokumentasi (ReDoc): http://localhost:8000/redoc")
    print()
    print("⏹️  Tekan CTRL+C untuk stop server")
    print("=" * 60)
    print()
    
    # Start server
    try:
        subprocess.run([
            sys.executable, "-m", "uvicorn",
            "app.main:app",
            "--reload",
            "--host", "0.0.0.0",
            "--port", "8000"
        ])
    except KeyboardInterrupt:
        print()
        print()
        print("=" * 60)
        print("👋 API Server stopped!")
        print("=" * 60)

if __name__ == "__main__":
    main()
