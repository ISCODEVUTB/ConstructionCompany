from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "mysql+pymysql://root:root@localhost:3306/ConstructionCompany"

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

