favorite_numbers = {
    "luis": [7, 42, 13],
    "trudie": [8],
    "eugene": [9, 21],
    "kelvin": [10, 100, 1000],
    "kagiso": [11, 4],
}

for name, numbers in sorted(favorite_numbers.items()):
    print(f"\n{name.title()}'s favourite numbers are:")
    for number in numbers:
        print(f"- {number}")