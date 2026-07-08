odd_numbers = list(range(1, 21, 2))
print(odd_numbers)

print("The first three items in the list are: ")
print(odd_numbers[:3])


print("\nThree items from the middle of the list are:")
print(odd_numbers[((len(odd_numbers) // 2) ++ 1):-1])

print("\nThe last three items in the list are:")
print(odd_numbers[-3:])