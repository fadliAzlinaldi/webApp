# service/nilai_service.py
import csv
import random
import os

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
