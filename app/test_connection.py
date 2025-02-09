from db.database import engine
from sqlalchemy.sql import text  # Import `text` to wrap raw SQL queries

def test_connection():
    try:
        with engine.connect() as connection:
            result = connection.execute(text("SELECT 1"))  # Use `text()` to wrap raw SQL
            print("✅ Connection successful!" if result.scalar() == 1 else "❌ Connection failed.")
    except Exception as e:
        print(f"❌ Connection error: {e}")

if __name__ == "__main__":
    test_connection()
