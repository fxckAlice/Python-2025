from typing import Dict, Any

def _input_float(prompt: str) -> float:
    while True:
        try:
            val = float(input(prompt).replace(",", "."))
            if val < 0:
                print("Value must be positive.")
                continue
            return val
        except ValueError:
            print("Invalid input. Please try again.")

def _input_int(prompt: str) -> int:
    while True:
        try:
            val = int(input(prompt))
            if not 0 <= val <= 31:
                print("Value must be between 0 and 31.")
                continue
            return val
        except ValueError:
            print("Invalid input. Please try again.")

def get_employees() -> Dict[str, Dict[str, Any]]:
    data: Dict[str, Dict[str, Any]] = {}
    print("Enter employees` data. Print 'stop' to finish.")
    while True:
        name = input("Enter name: ").strip()
        if name.lower() == "stop":
            break
        if not name:
            print("Name is required.")
            continue
        data[name] = {
            "salary": _input_float("Enter salary: "),
            "days": _input_int("Enter days: "),
        }
        print(f"Employee {name} added.")
    return data