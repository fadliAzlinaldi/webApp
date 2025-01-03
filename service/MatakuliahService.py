import pandas as pd
import os
import random
import csv
from sqlalchemy.orm import Session
from model.mataKuliahModel import MataKuliah

class MatakuliahService:
    def __init__(self):
        # Daftar nama mata kuliah
        self.matakuliah_list = [
            "Pemrograman Dasar", "Struktur Data", "Sistem Operasi", "Basis Data",
            "Jaringan Komputer", "Kecerdasan Buatan", "Pemrograman Web",
            "Analisis Algoritma", "Komputer Grafik", "Manajemen Proyek TI"
        ]
        self.output_dir = "output_files"
        os.makedirs(self.output_dir, exist_ok=True)

    def generate_matakuliah_data(self, num_courses: int = 10) -> str:
        """Generate matakuliah data and save to CSV."""
        data = []
        kode_set = set()  # Set untuk menyimpan kode unik

        # Generate data mata kuliah
        for i in range(num_courses):
            # Pastikan kode unik
            while True:
                kode = f"MK{random.randint(100, 999)}"  # Kode mata kuliah acak
                if kode not in kode_set:  # Cek jika kode sudah ada
                    kode_set.add(kode)  # Tambahkan kode ke set
                    break  # Kode unik ditemukan, keluar dari while loop
            
            nama = self.matakuliah_list[i % len(self.matakuliah_list)]  # Nama mata kuliah
            data.append([kode, nama])

        # Simpan ke CSV menggunakan pandas
        file_path = os.path.join(self.output_dir, "matakuliah.csv")
        df = pd.DataFrame(data, columns=["KodeMK", "Mata Kuliah"])
        df.to_csv(file_path, index=False)

        return file_path

    @staticmethod
    def insert_mata_kuliah_from_csv(file_path: str, db: Session):
        try:
            # Baca file CSV
            with open(file_path, mode='r') as file:
                reader = csv.reader(file)
                next(reader)  # Skip header

                mataKuliah_list = []
                for row in reader:
                    kode = row[0]  # Kode Mata Kuliah
                    nama = row[1]  # Nama Mata Kuliah

                    # Buat instance MataKuliah
                    mataKuliah = MataKuliah(kode=kode, nama=nama)
                    mataKuliah_list.append(mataKuliah)

                # Masukkan mata kuliah ke database
                db.add_all(mataKuliah_list)
                db.commit()

            return {"message": "Data mata kuliah berhasil dimasukkan ke database"}
        
        except Exception as e:
            db.rollback()
            raise Exception(f"Error inserting data: {str(e)}")
