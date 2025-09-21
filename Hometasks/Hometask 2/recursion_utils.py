from typing import List

def print_names_recursive(names: List[str], index: int = 0) -> None:
    if index >= len(names):
        return
    print(f"{names[index]}")
    print_names_recursive(names, index + 1)