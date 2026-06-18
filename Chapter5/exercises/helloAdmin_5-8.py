usernames = ['admin', 'user1', 'user2', 'user3', 'user4', 'user5']

index = len(usernames)
print(f'There are {index} usernames in my list!')

for user in usernames:
    if user == 'admin':
        print('Hello Admin, would you like to see a status report?')
    else:
        print(f'Hello {user}, thank you for logging in again.')