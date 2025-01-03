from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
from controller.StudentController import student_router  # Import router untuk students
from controller.MatakuliahController import matakuliah_router  # Import router untuk matakuliah
from controller.NilaiController import nilai_router  # Import router untuk nilai

# Inisialisasi FastAPI
app = FastAPI()

# Mendaftarkan router
app.include_router(student_router, prefix="/students", tags=["Students"])
app.include_router(matakuliah_router, prefix="/matakuliah", tags=["Matakuliah"])
app.include_router(nilai_router, prefix="/nilai", tags=["Nilai"])
