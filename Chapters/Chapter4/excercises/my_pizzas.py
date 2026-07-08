pizzas = ['pepperoni', 'hawaiian', 'bbq-chicken']

friend_pizza = pizzas[:]

print("My pizzas are:")
print(pizzas)


print("\nMy friend's pizzas are:")
print(friend_pizza)

pizzas.append('bacon and feta')
friend_pizza.append('seafood')

print("\nMy favourite pizza's are: ")

for p in pizzas:
    print(p)
      
print("\nMy friend's favourite pizza's are: ")

for f in friend_pizza:
    print(f)



# for pizza in pizzas:
#     print(f"I like {pizza} pizza.")
# print("\nI really love pizza!")