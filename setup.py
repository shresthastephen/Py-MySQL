from database import get_connection

DB_NAME = "pythonsql"

def create_database():
    db = get_connection()
    cursor = db.cursor()
    cursor.execute(
        f"CREATE DATABASE IF NOT EXISTS {DB_NAME} "
        "DEFAULT CHARACTER SET 'utf8'"
    )
    print(f"Database {DB_NAME} created or already exists.")
    cursor.close()
    db.close()

if __name__ == "__main__":
    create_database()
