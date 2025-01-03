import pandas as pd
import os
import random

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

        # Generate data mata kuliah
        for i in range(num_courses):
            kode = f"MK{random.randint(100, 999)}"  # Kode mata kuliah acak
            nama = self.matakuliah_list[i % len(self.matakuliah_list)]  # Nama mata kuliah
            data.append([kode, nama])

        # Simpan ke CSV menggunakan pandas
        file_path = os.path.join(self.output_dir, "matakuliah.csv")
        df = pd.DataFrame(data, columns=["KodeMK", "Mata Kuliah"])
        df.to_csv(file_path, index=False)

        return file_path
