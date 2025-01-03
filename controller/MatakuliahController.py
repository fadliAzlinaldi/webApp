from fastapi import APIRouter, HTTPException, UploadFile, File, Depends
from fastapi.responses import FileResponse
from service.MatakuliahService import MatakuliahService
from sqlalchemy.orm import Session
from database import get_db

# Inisialisasi router FastAPI
matakuliah_router = APIRouter()

# Inisialisasi Service
matakuliah_service = MatakuliahService()

@matakuliah_router.get("/generate-csv")
async def generate_csv():
    # Memanggil method untuk membuat file CSV
    file_path = matakuliah_service.generate_matakuliah_data()
    
    # Kirim file CSV sebagai respons
    return FileResponse(path=file_path, media_type='text/csv', filename="matakuliah.csv")

@matakuliah_router.post("/insert-csv")
async def insert_mata_kuliah(file: UploadFile = File(...), db: Session = Depends(get_db)):
    try:
        # Simpan file CSV yang diupload sementara di disk
        file_path = f"temp_{file.filename}"
        with open(file_path, "wb") as buffer:
            buffer.write(await file.read())
        
        # Panggil service untuk insert data ke database
        response = matakuliah_service.insert_mata_kuliah_from_csv(file_path, db)

        return response
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")
