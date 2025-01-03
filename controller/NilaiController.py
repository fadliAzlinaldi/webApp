# controller/nilai_controller.py
from fastapi import APIRouter
from fastapi.responses import FileResponse
from service.NilaiService import generate_nilai_csv  # Import service untuk generate CSV

# Membuat objek router untuk nilai
nilai_router = APIRouter()

# Endpoint untuk generate CSV nilai
@nilai_router.get("/generate-csv")
async def generate_csv():
    # Memanggil service untuk generate CSV
    file_path = generate_nilai_csv()
    
    # Mengembalikan file sebagai respons
    return FileResponse(file_path, media_type='text/csv', filename="nilai_mahasiswa.csv")
