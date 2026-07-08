getAge = input("How old are you? ")
age = int(getAge)

if age < 3:
    print("Your ticket is free!")
elif age < 13:
    print("Your ticket is R10.")
else:
    print("Your ticket is R15.")
    
    