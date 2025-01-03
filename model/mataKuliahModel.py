from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class MataKuliah(Base):
    __tablename__ = "mataKuliah"

    id = Column(Integer, primary_key=True, index=True)
    kode = Column(String(100), unique=True, index=True)  # Kode mata kuliah
    nama = Column(String(255))  # Nama mata kuliah
