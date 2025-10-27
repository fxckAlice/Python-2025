from db.sqlite_db import SQLiteDatabase
from repo.student_repository import StudentRepository
from service.student_service import StudentService
from domain.student import Student

def run():
    db = SQLiteDatabase("students.db")
    db.connect()
    repo = StudentRepository(db)
    repo.init_schema()
    service = StudentService(repo)

    student = Student("John Smith", "CS-101", "2004-05-12", "Kyiv")
    subjects = ["Math", "Physics", "Databases"]
    real_scores = [85, 90, 88]
    desired_scores = [95, 95, 95]

    student_id = service.create_or_update_student_data(student, subjects, real_scores, desired_scores)
    data = service.load_student_data(student_id)
    if data:
        rp = data.get_real_performance().average()
        dp = data.get_desired_performance().average()
        print(f"real_average={rp} desired_average={dp}")

    db.close()

if __name__ == "__main__":
    run()
