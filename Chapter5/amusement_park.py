age = 12
if age < 4:
    print("Your admission cost is R0.")
elif age < 18:
    print("Your admission cost is R25.")
else:
    print("Your admission cost is R40.")
    
    
# EXAMPLE 1:

age = 12

if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
else:
    price = 20

print("Your admission cost is " + str(price) + ".")

