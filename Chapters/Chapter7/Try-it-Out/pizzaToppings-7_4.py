toppings = []

while True:
    topping = input("Enter a pizza topping (or 'quit' to finish): ")
    if topping.lower() == 'quit':
        break
    toppings.append(topping)    

print("Your pizza will have the following toppings:")
for topping in toppings:
    print(f"- {topping}")