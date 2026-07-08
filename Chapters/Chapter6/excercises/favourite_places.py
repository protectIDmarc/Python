favorite_places = {
    'nicole': ['cape town', 'the kruger', 'zanzibar'],
    'trudie': ['durban'],
    'james': ['drakensberg', 'knysna'],
}

for name, places in favorite_places.items():
    print(f"\n{name.title()}'s favourite places are:")
    for place in places:
        print(f"- {place.title()}")