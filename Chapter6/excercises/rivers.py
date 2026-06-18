rivers = {
    "nile": "egypt",
    "limpopo": "south africa",
    "danube": "germany",
    "amazon": "brazil"
}

for river, country in rivers.items():
    print(f"The {river.title()} runs through {country.title()}!")

print(f"\nThe rivers are:\n")

for river in rivers.keys():
        # print the name of each river
        print(f"\t\t{river.title()}")

print(f"\nThe Countries are:\n")
for country in rivers.values():
        # print the name of each river
        print(f"\t\t{country.title()}")