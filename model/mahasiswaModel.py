from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# Inisialisasi Base untuk class declarative SQLAlchemy
Base = declarative_base()

class Mahasiswa(Base):
    __tablename__ = "mahasiswa"

    # Kolom dengan tipe data yang sesuai
    id = Column(Integer, primary_key=True, index=True)
    nim = Column(String(255), index=True)  # NIM mahasiswa
    nama = Column(String(255))  # Nama mahasiswa, harusnya String, bukan Integer

# Pastikan metadata dan koneksi ke database ada pada file database.py
