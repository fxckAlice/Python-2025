from .perfomance import Performance

class DesiredPerformance(Performance):
    def __init__(self, subjects: list[str], scores: list[float], desired_average: float):
        super().__init__(subjects, scores)
        self._desired_average = desired_average

    def get_desired_average(self) -> float:
        return self._desired_average

    def set_desired_average(self, value: float) -> None:
        self._desired_average = value

    def average(self) -> float:
        return float(self._desired_average)
