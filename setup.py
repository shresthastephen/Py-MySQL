from database import get_connection
from mysql.connector import errorcode

DB_NAME = "pythonsql"


TABLES = {}

TABLES['students'] = (
    "CREATE TABLE `students` ("
    "  `id` int(11) NOT NULL AUTO_INCREMENT,"
    "  `name` varchar(255) NOT NULL,"
    "  `email` varchar(255) NOT NULL,"
    "  PRIMARY KEY (`id`)"
    ") ENGINE=InnoDB")

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
    
def create_tables():
    db = get_connection()
    db.database = DB_NAME
    cursor = db.cursor()
    
    for table_name in TABLES:
        table_description = TABLES[table_name]
        try:
            print(f"Creating table {table_name}: ", end='')
            cursor.execute(table_description)
        except Exception as e:
            print(f"Failed creating table {table_name}: {e}")
        else:
            print("OK")
    
    cursor.close()
    db.close()

if __name__ == "__main__":
    create_database()
    create_tables()

