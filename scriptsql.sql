CREATE TABLE mahasiswa (
    id INT PRIMARY KEY IDENTITY(1,1), -- Kolom ID sebagai primary key dengan auto increment
    nim NVARCHAR(255),               -- Kolom NIM sebagai string (NVARCHAR untuk dukungan Unicode)
    nama NVARCHAR(255)               -- Kolom Nama sebagai string (NVARCHAR untuk dukungan Unicode)
);

CREATE TABLE mataKuliah (
    id INT PRIMARY KEY IDENTITY(1,1),  -- ID sebagai primary key dengan auto increment
    kode NVARCHAR(100) UNIQUE NOT NULL,  -- Kode mata kuliah, unik dan tidak boleh null
    nama NVARCHAR(255) NOT NULL  -- Nama mata kuliah, tidak boleh null
);

CREATE TABLE nilaiMahasiswa (
    id INT IDENTITY(1,1) PRIMARY KEY, -- Kolom ID sebagai primary key dengan auto-increment
    nilai FLOAT NOT NULL              -- Kolom nilai untuk menyimpan nilai mahasiswa
);

-- Hasilkan kombinasi penuh antara mahasiswa dan mata kuliah tanpa nilai
SELECT 
    m.nim AS nim_mahasiswa,
    m.nama AS nama_mahasiswa,
    mk.kode AS kode_matakuliah,
    mk.nama AS nama_matakuliah
FROM 
    mahasiswa m
CROSS JOIN 
    matakuliah mk
ORDER BY 
    m.nim, mk.kode;