multiplier = input("Enter a number to see its multiples of ten: ")
number = int(multiplier)

if number % 10 == 0:
    print(f"{number} is a multiple of ten.")
else:
    print(f"{number} is not a multiple of ten.")