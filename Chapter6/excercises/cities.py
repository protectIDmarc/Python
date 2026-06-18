cities = {
    'dublin': {
        'country': 'ireland',
        'population': 592_713,
        'fact': "home to the Guinness brewery and the medieval Trinity College, which holds the Book of Kells.",
    },
    'lisbon': {
        'country': 'portugal',
        'population': 545_000,
        'fact': "mainland Europe's westernmost capital, and one of the oldest cities in the world, predating Rome.",
    },
    'tokyo': {
        'country': 'japan',
        'population': 14_200_000,
        'fact': "the core of the world's largest urban region, though the UN recently ranked it third behind Jakarta and Dhaka.",
    },
}

for city, info in cities.items():
    print(f"\n{city.title()}")
    print(f"  Country: {info['country'].title()}")
    print(f"  Population: {info['population']:,}")
    print(f"  Fact: {info['fact'].capitalize()}")