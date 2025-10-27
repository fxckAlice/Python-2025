from abc import ABC, abstractmethod

class Performance(ABC):
    def __init__(self, subjects: list[str], scores: list[float]):
        self._subjects = subjects
        self._scores = scores

    def get_subjects(self) -> list[str]:
        return self._subjects

    def set_subjects(self, subjects: list[str]) -> None:
        self._subjects = subjects

    def get_scores(self) -> list[float]:
        return self._scores

    def set_scores(self, scores: list[float]) -> None:
        self._scores = scores

    @abstractmethod
    def average(self) -> float:
        ...
