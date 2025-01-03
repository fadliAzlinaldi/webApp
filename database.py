from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker

# Koneksi database dengan SQLAlchemy (sync)
DATABASE_URL = "mssql+pyodbc://@.\\SQLExpress/database?driver=ODBC+Driver+17+for+SQL+Server&Trusted_Connection=yes"

# Koneksi database
engine = create_engine(DATABASE_URL, pool_pre_ping=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

metadata = MetaData()

# Fungsi untuk mendapatkan session database
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
