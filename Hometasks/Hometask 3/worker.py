from typing import Optional


class Worker:
    def __init__(self, name: str, salary_month: float, days_worked: int, bonus_percent: float = 0.0):
        self._name = name
        self._salary_month = float(salary_month)
        self._days_worked = int(days_worked)
        self._bonus_percent = float(bonus_percent)

    def get_name(self) -> str:
        return self._name

    def set_name(self, value: str) -> None:
        self._name = value

    def get_salary_month(self) -> float:
        return self._salary_month

    def set_salary_month(self, value: float) -> None:
        self._salary_month = float(value)

    def get_days_worked(self) -> int:
        return self._days_worked

    def set_days_worked(self, value: int) -> None:
        self._days_worked = int(value)

    def get_bonus_percent(self) -> float:
        return self._bonus_percent

    def set_bonus_percent(self, value: float) -> None:
        self._bonus_percent = float(value)

    def calc_month_pay(self) -> float:
        return (self._salary_month / 30.0) * self._days_worked

    def calc_bonus(self) -> float:
        return self.calc_month_pay() * (self._bonus_percent / 100.0)
