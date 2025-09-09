import math

def calculate_when_positive(x):
    return 0.5 - math.pow(math.fabs(x), 1 / 4)

def calculate_when_negative(x):
    numerator = math.pow(math.sin(x ** 2), 2)
    denominator = math.fabs(x + 1)
    return numerator / denominator

def main():
    x = float(input("Enter x: "))
    if x >= 0:
        print(f"y = {calculate_when_positive(x)}")
    else:
        print(f"y = {calculate_when_negative(x)}")

main()