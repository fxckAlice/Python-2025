from domain.student import Student
from domain.real_performance import RealPerformance
from domain.desired_performance import DesiredPerformance
from domain.student_data import StudentData
from repo.student_repository import StudentRepository

class StudentService:
    def __init__(self, repo: StudentRepository):
        self._repo = repo

    def create_or_update_student_data(self, student: Student, real_subjects: list[str], real_scores: list[float], desired_scores: list[float]) -> int:
        student_id = self._ensure_student(student)
        self._repo.upsert_grades(student_id, real_subjects, real_scores)
        self._repo.upsert_desired_grades(student_id, real_subjects, desired_scores)
        return student_id

    def _ensure_student(self, student: Student) -> int:
        existing_id = self._repo.find_student_id_by_name_and_group(student.get_full_name(), student.get_group_number())
        if existing_id is not None:
            self._repo.update_student(existing_id, student.get_full_name(), student.get_group_number(), student.get_birth_date(), student.get_address())
            return existing_id
        return self._repo.insert_student(student.get_full_name(), student.get_group_number(), student.get_birth_date(), student.get_address())

    def load_student_data(self, student_id: int) -> StudentData | None:
        data = self._repo.get_student_with_grades(student_id)
        if not data:
            return None
        s_row, real_rows, desired_rows = data
        student = Student(s_row[1], s_row[2], s_row[3], s_row[4])
        subjects = [r[0] for r in real_rows]
        real_scores = [float(r[1]) for r in real_rows]
        desired_map = {d[0]: float(d[1]) for d in desired_rows}
        desired_scores = [desired_map.get(subj, 0.0) for subj in subjects]
        real_perf = RealPerformance(subjects, real_scores)
        desired_avg = 0.0 if not desired_scores else sum(desired_scores) / len(desired_scores)
        desired_perf = DesiredPerformance(subjects, desired_scores, desired_avg)
        return StudentData(student, real_perf, desired_perf)
