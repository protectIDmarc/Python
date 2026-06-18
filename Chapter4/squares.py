digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(digits)

print(f"Minimum: {min(digits)}")
print(f"Maximum: {max(digits)}")
print(f"Sum: {sum(digits)}")

print("\nUsing a list comprehension to generate squares:")

squares = [value**2 for value in range(1, 11)]
print(squares)