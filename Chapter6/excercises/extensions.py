cities = {
    'dublin': {
        'country': 'ireland',
        'population': 592_713,
        'language': 'english (and irish)',
        'founded': '9th century, by the vikings',
        'landmark': 'trinity college, home to the book of kells',
        'fact': "the river liffey splits the city into the north side and south side.",
    },
    'lisbon': {
        'country': 'portugal',
        'population': 545_000,
        'language': 'portuguese',
        'founded': 'over 3,000 years ago by the phoenicians',
        'landmark': 'the belém tower on the river tagus',
        'fact': "it is mainland europe's westernmost capital city.",
    },
    'tokyo': {
        'country': 'japan',
        'population': 14_200_000,
        'language': 'japanese',
        'founded': '1457, originally as the village of edo',
        'landmark': 'the senso-ji temple in asakusa',
        'fact': "it sits at the core of the world's largest urban region.",
    },
}

print("=" * 45)
print("CITY FACT FILE".center(45))
print("=" * 45)

for city, info in cities.items():
    print(f"\n*|* {city.upper()}, {info['country'].title()}")
    print("-" * 45)
    print(f"  Population : {info['population']:>12,}")
    print(f"  Language   : {info['language'].title()}")
    print(f"  Founded    : {info['founded'].capitalize()}")
    print(f"  Landmark   : {info['landmark'].capitalize()}")
    print(f"  Did you know? {info['fact'].capitalize()}")

print("\n" + "=" * 45)