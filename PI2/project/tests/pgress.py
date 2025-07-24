from sqlalchemy import create_engine, text

USER = "nicolas"
PASSWORD = "5000"
HOST = "localhost"
PORT = "5432"
DBNAME = "test_db"
SCHEMA ="public"

engine = create_engine(f"postgresql+psycopg2://{USER}:{PASSWORD}@{HOST}:{PORT}/{DBNAME}")

try:
    with engine.connect() as conn:
        result = conn.execute(text("SELECT version();"))
        print("Conectado a:", result.fetchone()[0])
except Exception as e:
    print("Error de conexión:", e)