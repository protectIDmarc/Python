# A dictionary of major rivers mapped to the country each one flows through.
rivers = {
    "nile": "egypt",
    "limpopo": "south africa",
    "danube": "germany",
    "amazon": "brazil"
}

# Loop over each key/value pair and print a sentence describing the river.
for river, country in rivers.items():
    print(f"The {river.title()} runs through {country.title()}!")

# Heading for the list of river names.
print(f"\nThe rivers are:\n")

# Loop over just the dictionary keys to list every river name.
for river in rivers.keys():
    # Print the name of each river, capitalised and indented.
    print(f"\t\t{river.title()}")

# Heading for the list of country names.
print(f"\nThe Countries are:\n")

# Loop over just the dictionary values to list every country name.
for country in rivers.values():
    # Print the name of each country, capitalised and indented.
    print(f"\t\t{country.title()}")
