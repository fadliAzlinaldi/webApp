import csv
import random
import os
from sqlalchemy.orm import Session
from model.nilaiMahasiswaModel import NilaiMahasiswa


class NilaiService:
    @staticmethod
    def generate_nilai_csv():
        # Tentukan path file CSV
        output_dir = "output_files"
        os.makedirs(output_dir, exist_ok=True)
        file_path = os.path.join(output_dir, "nilai_mahasiswa.csv")

        # Menulis data ke dalam file CSV
        with open(file_path, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["id", "nilai"])  # Menulis header CSV
            for i in range(1, 1000001):  # 1 juta data
                nilai = random.randint(10, 100)  # Nilai acak antara 10 dan 100
                writer.writerow([i, nilai])

        return file_path  # Mengembalikan path file CSV yang telah dibuat

    def insert_nilai_from_csv(self, file_path: str, db: Session):
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File {file_path} tidak ditemukan")

        try:
            # Baca file CSV
            with open(file_path, mode='r') as file:
                reader = csv.reader(file)
                next(reader)  # Skip header jika ada

                nilai_list = []
                for row in reader:
                    # Periksa apakah baris memiliki setidaknya dua kolom
                    if len(row) >= 2:
                        try:
                            nilai = float(row[1])  # Ambil kolom kedua sebagai nilai
                            nilai_mahasiswa = NilaiMahasiswa(nilai=nilai)
                            nilai_list.append(nilai_mahasiswa)
                        except ValueError:
                            print(f"Baris tidak valid, tidak bisa mengonversi nilai: {row}")
                    else:
                        print(f"Baris tidak lengkap: {row}")

                # Masukkan data ke database
                if nilai_list:
                    db.add_all(nilai_list)
                    db.commit()
                    return {"message": "Data nilai mahasiswa berhasil dimasukkan ke database"}
                else:
                    return {"message": "Tidak ada data valid yang dimasukkan, pastikan CSV memiliki data yang valid"}

        except Exception as e:
            db.rollback()
            raise Exception(f"Error inserting data: {str(e)}")
