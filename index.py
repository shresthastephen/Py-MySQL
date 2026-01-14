from crud import (
    insert_student,
    get_all_students,
    get_student_by_id,
    update_student,
    delete_student,
    truncate_students
)

# insert_student("Stephen", "stephen@email.com")

print(get_all_students())

print(get_student_by_id(2))

# update_student(1, "Stephen G", "stephen.g@email.com")

# delete_student(2)

# truncate_students()
