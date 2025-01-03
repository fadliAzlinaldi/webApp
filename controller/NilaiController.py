# controller/nilai_controller.py
from fastapi import APIRouter, Depends, UploadFile, HTTPException
from fastapi.responses import FileResponse
from sqlalchemy.orm import Session
from service.NilaiService import NilaiService
from database import get_db
import os

# Membuat objek router untuk nilai
nilai_router = APIRouter()

# Inisialisasi service
nilai_service = NilaiService()

# Endpoint untuk generate CSV nilai
@nilai_router.get("/generate-csv")
async def generate_csv():
    try:
        # Memanggil service untuk generate CSV
        file_path = nilai_service.generate_nilai_csv()

        # Mengembalikan file sebagai respons
        return FileResponse(file_path, media_type='text/csv', filename="nilai_mahasiswa.csv")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error generating CSV: {str(e)}")


# Endpoint untuk insert data dari CSV
@nilai_router.post("/insert-csv")
async def insert_nilai_mahasiswa(file: UploadFile, db: Session = Depends(get_db)):
    file_path = f"temp_{file.filename}"
    try:
        # Simpan file CSV yang diunggah sementara di disk
        with open(file_path, "wb") as buffer:
            buffer.write(await file.read())

        # Panggil service untuk insert data dari CSV
        response = nilai_service.insert_nilai_from_csv(file_path, db)

        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error inserting data: {str(e)}")
    finally:
        # Hapus file sementara setelah selesai
        if os.path.exists(file_path):
            os.remove(file_path)
