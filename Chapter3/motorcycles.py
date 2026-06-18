# A list is a collection of items in a particular order. You can make a list that includes the letters of the alphabet, the digits from 0 to 9, or the names of all the people in your family. A list is a versatile data structure that allows you to store and manipulate multiple items in a single variable.
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

# MODIFYING A LIST
motorcycles[0] = 'ducati'
print(motorcycles)

# ADDING ELEMENTS TO A LIST
motorcycles.append('honda')
print(motorcycles)
motorcycles.append('yamaha')
print(motorcycles)


motorcycles = []
motorcycles.append('honda')
print(motorcycles)

motorcycles.append('yamaha')
print(motorcycles)

motorcycles.append('suzuki')
print(motorcycles)

motorcycles.append('ducati')
print(motorcycles)

# INSERTING ELEMENTS INTO A LIST
motorcycles.insert(0, 'ducati')
print(motorcycles)
motorcycles.insert(2, 'test')
print(motorcycles)


# REMOVING ELEMENTS FROM A LIST
del motorcycles[0:2]
print(motorcycles)



