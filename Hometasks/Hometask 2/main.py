from employees_input import get_employees
from payroll import compute_all
from recursion_utils import print_names_recursive

def main():
    employees = get_employees()
    if not employees:
        print("No employees found.")
        return

    pays = compute_all(employees)
    print("\n=== Income (with bonuses) ===")
    for name, total in pays.items():
        print(f"{name}: {total:.2f}$")

    print("\n=== Names list (recursive) ===")
    print_names_recursive(list(employees.keys()))


main()