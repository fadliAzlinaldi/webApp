from sqlalchemy import Column, Integer, Float
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class NilaiMahasiswa(Base):
    __tablename__ = "nilaiMahasiswa"

    id = Column(Integer, primary_key=True, index=True)
    nilai = Column(Float)  # Nilai mahasiswa
