def main():
    n = float(input("Enter n: "))
    if n <= 1:
        print("n is less than or equal to 1")
        return
    num1 = float(input("Enter num1: "))
    num2 = float(input("Enter num2: "))
    num3 = float(input("Enter num3: "))

    print("Result: ")
    if 1 <= num1 <= n:
        print(num1)
    if 1 <= num2 <= n:
        print(num2)
    if 1 <= num3 <= n:
        print(num3)

main()