from fastapi import APIRouter
from fastapi.responses import FileResponse
from service.MatakuliahService import MatakuliahService

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
