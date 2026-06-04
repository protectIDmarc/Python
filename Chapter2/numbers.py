# Inside an f-string, {} evaluates the expression and inserts the result.
# So {2 + 3} runs the maths and prints 5.
print(f"2 + 3 = {2 + 3}")        # addition
print(f"2 - 3 = {2 - 3}")        # subtraction -> -1
print(f"2 * 3 = {2 * 3}")        # multiplication -> 6
print(f"2 / 3 = {2 / 3}")        # division ALWAYS returns a float -> 0.6666...

print(f"2 ** 3 = {2 ** 3}")      # ** is exponentiation (2 to the power of 3) -> 8
print(f"(2 + 3) * 4 = {(2 + 3) * 4}")  # parentheses control order of operations -> 20

# FLOATS
# Floats are numbers with a decimal point. Watch out: floating-point maths
# can produce tiny rounding surprises (e.g. 0.1 + 0.2 famously isn't exactly 0.3).
print(f"0.1 + 0.1 = {0.1 + 0.1}")    # -> 0.2
print(f"2 * 0.2 = {2 * 0.2}")        # -> 0.4

# INTEGERS & FLOATS
# Mixing an int with a float (or using /) gives a float result.
print (f"4 / 2 = {4 / 2}")       # -> 2.0 (a float, not 2), because / always returns a float
print (f"1 + 2.0 = {1 + 2.0}")   # -> 3.0, because adding a float promotes the result to float

# UNDERSCORES IN NUMBERS
# Underscores are just visual separators to make large numbers readable.
# Python ignores them, so 14_000_000_000 is the same as 14000000000.
universe_age = 14_000_000_000
print(f"Universe age is: {universe_age}")   # prints without the underscores

# MULTIPLE ASSIGNMENT
# Assign several variables on one line: x gets 1, y gets 2, z gets 3.
x, y, z = 1, 2, 3
print(f"x: {x}, y: {y}, z: {z}")

# CONSTANTS
# Python has no built-in constant type. By convention, ALL_CAPS names signal
# "don't change this" to other programmers — but Python won't actually stop you.
MAX_CONNECTIONS = 5000
print(f"Max connections: {MAX_CONNECTIONS}")