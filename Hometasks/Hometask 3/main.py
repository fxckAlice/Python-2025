from typing import List, Union
from worker import Worker
from manager import Manager


def format_money(value: float) -> str:
    return f"{value:,.2f} грн".replace(",", " ")


def show_staff_summary(staff: List[Union[Worker, Manager]]) -> None:
    print("Розрахунок зарплат і бонусів")
    print("-" * 72)
    for person in staff:
        role = "Менеджер" if isinstance(person, Manager) else "Співробітник"
        pay = person.calc_month_pay()
        bonus = person.calc_bonus()
        print(f"{role:12} | {person.get_name():22} | Зарплата: {format_money(pay):>12} | Бонус: {format_money(bonus):>12}")
        if isinstance(person, Manager):
            print(f"  {person.generate_report()}")
    print("-" * 72)


if __name__ == "__main__":
    s1 = Worker("Іван Петренко", 30000, 28, 10)
    s2 = Worker("Олена Коваль", 28000, 30)
    s3 = Worker("Максим Романюк", 35000, 26, 5)

    m1 = Manager("Наталія Білозір", 45000, 29, num_subordinates=5, bonus_percent=8)
    m2 = Manager("Андрій Скиба", 50000, 27, num_subordinates=12, bonus_percent=12)

    staff = [s1, s2, s3, m1, m2]
    show_staff_summary(staff)
