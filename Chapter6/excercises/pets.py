pet_0 = {
    'animal_type': 'cat',
    'ownerFirstName': 'John',
    'ownerLastName': 'doe',    
}

pet_1 = {
    'animal_type': 'dog',
    'ownerFirstName': 'Jane',
    'ownerLastName': 'doe',    
}
pet_2 = {
    'animal_type': 'parrot',
    'ownerFirstName': 'sarah',
    'ownerLastName': 'cummins',    
}
pet_3 = {
    'animal_type': 'snake',
    'ownerFirstName': 'joe',
    'ownerLastName': 'bowdler',    
}

# STORE THESE PET DICTIONARIES INTO A LIST:
pets = []

for pet in (pet_0, pet_1, pet_2, pet_3):
    pets.append(pet)
    print(pets)
    
for p in pets:
    print(f"\nPet type: {p['animal_type'].title()}.")
    print(f"Owner: {p['ownerFirstName'].title()} {p['ownerLastName'].title()}.")
            

