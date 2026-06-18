person_0 = {'first_name': 'nicole', 'last_name': 'brews-sammons', 'age': 45, 'city': 'johannesburg'}
person_1 = {'first_name': 'trudie', 'last_name': 'marques', 'age': 21, 'city': 'bela bela'}
person_2 = {'first_name': 'james', 'last_name': 'thorton', 'age': 50, 'city': 'polokwane'}

# CREATE AN EMPTY LIST FOR PEOPLE
people = []

# COMPILE A LIST OF PEOPLE FROM MY DICTIONARIES
for person in (person_0, person_1, person_2):
    people.append(person)

# THIS IS MY FINAL LIST:
print(f"\nThis is my List!")
print(people)

# NOW WE LOOP THROUGH THE LIST AND PRINT ALL INFO:
for p in people:
    print(f"\n{p['first_name'].title()} {p['last_name'].title()}, age {p['age']}, lives in {p['city'].title()}.\n")
