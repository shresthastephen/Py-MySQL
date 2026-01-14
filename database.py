import mysql.connector

config = {
    "user": "pyuser",
    "password": "Iphone123$$",
    "host": "localhost",
    "database": "pythonsql"
    
}

def get_connection():
    return mysql.connector.connect(**config)
