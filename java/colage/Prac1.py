def Prac1(n):
    if n <= 0:
        n = -n  

    print(f"{n} =", end=" ")

    if n % 2 == 0:
        n /= 2
    else:
        n = 3 * n + 1

    print(n)

while True:
    print("\nEnter a natural number or 0 to Exit : ")
    try:
        num = float(input())
        if num == 0:
            print("Exiting...")
            break
        Prac1(num)
    except ValueError:
        print("Invalid input. Please enter a valid number.")
