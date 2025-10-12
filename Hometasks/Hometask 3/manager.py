from typing import ClassVar
from worker import Worker


class Manager(Worker):
    PREMIUM_AMOUNT: ClassVar[float] = 300.0

    def __init__(self, name: str, salary_month: float, days_worked: int, num_subordinates: int, bonus_percent: float = 0.0):
        super().__init__(name, salary_month, days_worked, bonus_percent)
        self._num_subordinates = int(num_subordinates)

    def get_num_subordinates(self) -> int:
        return self._num_subordinates

    def set_num_subordinates(self, value: int) -> None:
        self._num_subordinates = int(value)

    def calc_bonus(self) -> float:
        base_bonus = super().calc_bonus()
        return base_bonus + (self._num_subordinates * Manager.PREMIUM_AMOUNT)

    def generate_report(self) -> str:
        return f"Менеджер {self.get_name()} керує {self._num_subordinates} співробітниками."
