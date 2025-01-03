import random
import pandas as pd
import os
import csv
from sqlalchemy.orm import Session
from model.mahasiswaModel import Mahasiswa

class StudentService:
    def __init__(self):
        # Daftar nama statis untuk kecepatan
        self.names = [
            "John Doe", "Jane Smith", "Michael Johnson", "Emily Davis", "Daniel Wilson",
            "Sarah Brown", "David Lee", "Anna Clark", "James Harris", "Sophia Lewis",
            "Daniel Walker", "Isabella Young", "Benjamin Scott", "Ava Allen", "Lucas King"
        ]
        self.output_dir = "output_files"
        os.makedirs(self.output_dir, exist_ok=True)

    def generate_student_data(self, num_students: int = 1000000) -> str:
        """Generate student data and save to CSV."""
        data = []

        # Generate data mahasiswa
        for _ in range(num_students):
            nim = f"MA{random.randint(100000000, 999999999)}"  # NIM acak
            name = random.choice(self.names)  # Pilih nama acak dari daftar
            data.append([nim, name])

        # Simpan ke CSV menggunakan pandas
        file_path = os.path.join(self.output_dir, "students.csv")
        df = pd.DataFrame(data, columns=["NIM", "Nama"])
        df.to_csv(file_path, index=False)

        return file_path

    def insert_mahasiswa_from_csv(self, file_path: str, db: Session):
        try:
            # Baca file CSV
            with open(file_path, mode='r') as file:
                reader = csv.reader(file)
                next(reader)  # Skip header
                
                mahasiswa_list = []
                for row in reader:
                    # Parse data mahasiswa dari CSV
                    nim = row[0]  # NIM
                    nama = row[1]  # Nama
                    
                    mahasiswa = Mahasiswa(nim=nim, nama=nama)
                    mahasiswa_list.append(mahasiswa)
                
                # Masukkan mahasiswa ke database menggunakan bulk_save_objects
                db.bulk_save_objects(mahasiswa_list)
                db.commit()
            
            return {"message": "Data mahasiswa berhasil dimasukkan ke database"}
        
        except Exception as e:
            db.rollback()
            return {"error": f"Error inserting data: {str(e)}"}
