from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from src.backend.app.api.models.users_db import Base
import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def test_connection():
    try:
        with engine.connect() as connection:
            result = connection.execute(text("SELECT 1"))
            print("Conexión exitosa:", result.scalar())
    except Exception as e:
        print("Error al conectar a la base de datos:", e)

if __name__ == "__main__":
    print("Probando conexión a la base de datos...")
    test_connection()
    # Crear tablas si no existen
    Base.metadata.create_all(bind=engine)

