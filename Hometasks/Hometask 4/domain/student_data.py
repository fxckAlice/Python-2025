from .student import Student
from .perfomance import Performance

class StudentData:
    def __init__(self, student: Student, real_performance: Performance, desired_performance: Performance):
        self._student = student
        self._real_performance = real_performance
        self._desired_performance = desired_performance

    def get_student(self) -> Student:
        return self._student

    def get_real_performance(self) -> Performance:
        return self._real_performance

    def get_desired_performance(self) -> Performance:
        return self._desired_performance
