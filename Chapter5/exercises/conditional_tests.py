# car = 'subaru'

# print("Is car == 'subaru'? I predict True.")
# print(car == 'subaru')

# print("\nIs car == 'audi'? I predict False.")
# print(car == 'audi')

# # A string and a number
# favorite_number = 7
# print("\nIs favorite_number == 7? I predict True.")
# print(favorite_number == 7)

# print("\nIs favorite_number > 10? I predict False.")
# print(favorite_number > 10)

# # Case sensitivity in strings
# name = 'Eric'
# print("\nIs name.lower() == 'eric'? I predict True.")
# print(name.lower() == 'eric')

# print("\nIs name == 'eric'? I predict False.")
# print(name == 'eric')

# # Inequality
# age = 25
# print("\nIs age != 30? I predict True.")
# print(age != 30)

# print("\nIs age != 25? I predict False.")
# print(age != 25)

# # Numerical comparisons
# temperature = 18
# print("\nIs temperature <= 20? I predict True.")
# print(temperature <= 20)

# print("\nIs temperature >= 25? I predict False.")
# print(temperature >= 25)

# # Membership in a list
# fruits = ['apple', 'banana', 'mango']
# print("\nIs 'banana' in fruits? I predict True.")
# print('banana' in fruits)

# print("\nIs 'orange' in fruits? I predict False.")
# print('orange' in fruits)

# # Using 'and' / 'or'
# print("\nIs (age > 18 and temperature < 30)? I predict True.")
# print(age > 18 and temperature < 30)

# print("\nIs (age > 30 or temperature > 30)? I predict False.")
# print(age > 30 or temperature > 30)

# --- String equality and inequality ---
car = 'subaru'

print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')

print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')

print("\nIs car != 'toyota'? I predict True.")
print(car != 'toyota')

print("\nIs car != 'subaru'? I predict False.")
print(car != 'subaru')

# --- Tests using the lower() method ---
name = 'Eric'

print("\nIs name.lower() == 'eric'? I predict True.")
print(name.lower() == 'eric')

print("\nIs name.lower() == 'Eric'? I predict False.")
print(name.lower() == 'Eric')

# --- Numerical equality and inequality ---
age = 25

print("\nIs age == 25? I predict True.")
print(age == 25)

print("\nIs age == 30? I predict False.")
print(age == 30)

print("\nIs age != 18? I predict True.")
print(age != 18)

print("\nIs age != 25? I predict False.")
print(age != 25)

# --- Greater than / less than ---
print("\nIs age > 18? I predict True.")
print(age > 18)

print("\nIs age > 40? I predict False.")
print(age > 40)

print("\nIs age < 40? I predict True.")
print(age < 40)

print("\nIs age < 18? I predict False.")
print(age < 18)

# --- Greater than or equal to / less than or equal to ---
print("\nIs age >= 25? I predict True.")
print(age >= 25)

print("\nIs age >= 26? I predict False.")
print(age >= 26)

print("\nIs age <= 25? I predict True.")
print(age <= 25)

print("\nIs age <= 24? I predict False.")
print(age <= 24)

# --- Tests using the and keyword ---
print("\nIs (age > 18 and age < 40)? I predict True.")
print(age > 18 and age < 40)

print("\nIs (age > 18 and age < 20)? I predict False.")
print(age > 18 and age < 20)

# --- Tests using the or keyword ---
print("\nIs (age > 40 or age < 30)? I predict True.")
print(age > 40 or age < 30)

print("\nIs (age > 40 or age < 20)? I predict False.")
print(age > 40 or age < 20)

# --- Test whether an item is in a list ---
fruits = ['apple', 'banana', 'mango']

print("\nIs 'banana' in fruits? I predict True.")
print('banana' in fruits)

print("\nIs 'orange' in fruits? I predict False.")
print('orange' in fruits)

# --- Test whether an item is not in a list ---
print("\nIs 'orange' not in fruits? I predict True.")
print('orange' not in fruits)

print("\nIs 'apple' not in fruits? I predict False.")
print('apple' not in fruits)