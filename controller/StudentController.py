from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import FileResponse
from sqlalchemy.orm import Session
from service.StudentService import StudentService
from database import get_db  # Pastikan Anda memiliki metode ini untuk mendapatkan session DB
import os

student_router = APIRouter()

# Inisialisasi Service
student_service = StudentService()

@student_router.get("/generate-csv")
async def generate_csv():
    file_path = student_service.generate_student_data()
    
    # Kirim file CSV sebagai respons
    return FileResponse(path=file_path, media_type='text/csv', filename="students.csv")

@student_router.post("/insert-csv")
async def insert_students_from_csv(file_path: str, db: Session = Depends(get_db)):
    try:
        # Memasukkan mahasiswa dari CSV ke database
        result = student_service.insert_mahasiswa_from_csv(file_path, db)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")
