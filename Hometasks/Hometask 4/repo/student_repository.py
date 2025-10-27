from typing import Iterable
from db.base import Database

class StudentRepository:
    def __init__(self, db: Database):
        self._db = db

    def init_schema(self) -> None:
        self._db.execute("""
        CREATE TABLE IF NOT EXISTS students(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            full_name TEXT NOT NULL,
            group_number TEXT NOT NULL,
            birth_date TEXT,
            address TEXT
        )""")
        self._db.execute("""
        CREATE TABLE IF NOT EXISTS grades(
            student_id INTEGER NOT NULL,
            subject TEXT NOT NULL,
            score REAL NOT NULL,
            PRIMARY KEY(student_id, subject),
            FOREIGN KEY(student_id) REFERENCES students(id) ON DELETE CASCADE
        )""")
        self._db.execute("""
        CREATE TABLE IF NOT EXISTS desired_grades(
            student_id INTEGER NOT NULL,
            subject TEXT NOT NULL,
            desired_score REAL NOT NULL,
            PRIMARY KEY(student_id, subject),
            FOREIGN KEY(student_id) REFERENCES students(id) ON DELETE CASCADE
        )""")

    def insert_student(self, full_name: str, group_number: str, birth_date: str | None, address: str | None) -> int:
        self._db.execute(
            "INSERT INTO students(full_name, group_number, birth_date, address) VALUES(?,?,?,?)",
            (full_name, group_number, birth_date, address)
        )
        row = self._db.fetchone("SELECT last_insert_rowid()")
        return int(row[0]) if row else 0

    def update_student(self, student_id: int, full_name: str, group_number: str, birth_date: str | None, address: str | None) -> int:
        return self._db.execute(
            "UPDATE students SET full_name=?, group_number=?, birth_date=?, address=? WHERE id=?",
            (full_name, group_number, birth_date, address, student_id)
        )

    def delete_student(self, student_id: int) -> int:
        return self._db.execute("DELETE FROM students WHERE id=?", (student_id,))

    def upsert_grades(self, student_id: int, subjects: Iterable[str], scores: Iterable[float]) -> int:
        pairs = list(zip(subjects, scores))
        changed = 0
        for subject, score in pairs:
            count = self._db.execute(
                "UPDATE grades SET score=? WHERE student_id=? AND subject=?",
                (score, student_id, subject)
            )
            if count == 0:
                changed += self._db.execute(
                    "INSERT INTO grades(student_id, subject, score) VALUES(?,?,?)",
                    (student_id, subject, score)
                )
            else:
                changed += count
        return changed

    def upsert_desired_grades(self, student_id: int, subjects: Iterable[str], desired_scores: Iterable[float]) -> int:
        pairs = list(zip(subjects, desired_scores))
        changed = 0
        for subject, score in pairs:
            count = self._db.execute(
                "UPDATE desired_grades SET desired_score=? WHERE student_id=? AND subject=?",
                (score, student_id, subject)
            )
            if count == 0:
                changed += self._db.execute(
                    "INSERT INTO desired_grades(student_id, subject, desired_score) VALUES(?,?,?)",
                    (student_id, subject, score)
                )
            else:
                changed += count
        return changed

    def find_student_id_by_name_and_group(self, full_name: str, group_number: str) -> int | None:
        row = self._db.fetchone(
            "SELECT id FROM students WHERE full_name=? AND group_number=?",
            (full_name, group_number)
        )
        return int(row[0]) if row else None

    def get_student_with_grades(self, student_id: int) -> tuple | None:
        student = self._db.fetchone(
            "SELECT id, full_name, group_number, birth_date, address FROM students WHERE id=?",
            (student_id,)
        )
        if not student:
            return None
        grades = self._db.fetchall(
            "SELECT subject, score FROM grades WHERE student_id=? ORDER BY subject",
            (student_id,)
        )
        desired = self._db.fetchall(
            "SELECT subject, desired_score FROM desired_grades WHERE student_id=? ORDER BY subject",
            (student_id,)
        )
        return student, grades, desired
