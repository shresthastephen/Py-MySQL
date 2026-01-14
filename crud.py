from database import get_connection


# create
def insert_student(name, email):
    db = get_connection()
    cursor = db.cursor()

    query = (
        "INSERT INTO students (name, email) "
        "VALUES (%s, %s)"
    )
    cursor.execute(query, (name, email))
    db.commit()

    print(f"Inserted student: {name} ({email})")

    cursor.close()
    db.close()


# read(all)
def get_all_students():
    db = get_connection()
    cursor = db.cursor(dictionary=True)

    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()

    cursor.close()
    db.close()

    return students


# read(by id)
def get_student_by_id(student_id):
    db = get_connection()
    cursor = db.cursor(dictionary=True)

    cursor.execute(
        "SELECT * FROM students WHERE id = %s",
        (student_id,)
    )
    student = cursor.fetchone()

    cursor.close()
    db.close()

    return student


# update
def update_student(student_id, name, email):
    db = get_connection()
    cursor = db.cursor()

    cursor.execute(
        "UPDATE students SET name=%s, email=%s WHERE id=%s",
        (name, email, student_id)
    )
    db.commit()

    print(f"Updated student ID {student_id}")

    cursor.close()
    db.close()


# delete
def delete_student(student_id):
    db = get_connection()
    cursor = db.cursor()

    cursor.execute(
        "DELETE FROM students WHERE id = %s",
        (student_id,)
    )
    db.commit()

    print(f"Deleted student ID {student_id}")

    cursor.close()
    db.close()
    
    
def truncate_students():
    db = get_connection()
    cursor = db.cursor()

    cursor.execute("TRUNCATE TABLE students")

    print("Students table truncated")

    cursor.close()
    db.close()

