from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker, Session
from backend.app.api.database.schemas.users_db import Base
from backend.app.api.database.db import get_db
import os
from dotenv import load_dotenv
from sqlalchemy.pool import StaticPool

load_dotenv()

TESTING = os.getenv("TESTING", "0") == "1"

if TESTING:
    DATABASE_URL = "sqlite:///:memory:"
    engine = create_engine(
        DATABASE_URL,
        connect_args={"check_same_thread": False},
        poolclass=StaticPool
    )
else:
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

def get_db():
    db: Session = SessionLocal()
    try:
        yield db
    finally:
        db.close()

if __name__ == "__main__":
    print("Probando conexión a la base de datos...")
    test_connection()
    # Crear tablas si no existen
    Base.metadata.create_all(bind=engine)

