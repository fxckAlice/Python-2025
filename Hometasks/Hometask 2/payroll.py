from typing import Dict

DAILY_DIVISOR = 30

def monthly_salary(base_monthly_salary: float, days_worked: int) -> float:
    return (base_monthly_salary / 30) * days_worked

def bonus(days_worked: int, base_monthly_salary: float) -> float:
    if days_worked >= 30:
        return 0.1 * base_monthly_salary
    elif days_worked >= 28:
        return 0.05 * base_monthly_salary
    else:
        return 0

def compute_all(employees: Dict[str, Dict[str, float]]) -> Dict[str, float]:
    result: Dict[str, float] = {}
    for name, rec in employees.items():
        base = monthly_salary(rec["salary"], int(rec["days"]))
        extra = bonus(int(rec["days"]), rec["salary"])
        result[name] = round(base + extra, 2)
    return result