import math

def calculate_function(x, t):
    numerator = 9 * math.pi * t + 10 * math.cos(x)
    denominator = math.sqrt(t) - math.fabs(math.sin(t))
    return (numerator / denominator) * math.exp(x)

def main():
    x = float(input("Enter x: "))
    t = float(input("Enter t: "))
    print(f"y = {calculate_function(x, t):.2f}")

main()