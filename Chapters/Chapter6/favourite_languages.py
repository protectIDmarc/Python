favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
    }

# language = favorite_languages['sarah'].title()
# print(f"Sarah's favorite language is {language}.")

# **** Looping through all Key | Value pairs in a Dictionary ****

# for name, language in favorite_languages.items():
#     print(f"{name.title()}'s favourite language is {language.title()}.")

# LOOPING THROUGH ALL KEYS IN A DICTIONARY

# # EXAMPLE 1:
# for name in favorite_languages.keys():
#     print(name.title())
    
# print("\n***************")

# # EXAMPLE 2:
# for name in favorite_languages:
#     print(name.title())


# ******************* LOOPING THROUGH DICTIONARY TO ACCESS VALUES ***********************

# friends = ['phil', 'sarah']

# for name in favorite_languages.keys():
#     print(f"\nHi {name.title()}.")
        
#     if name in friends:
#         language = favorite_languages[name].title()
#         print(f"\t- {name.title()}, I see you love {language}!")
        
# if 'erin' not in favorite_languages:
#     print(f"\n**************************\nErin, please take our poll!\n**************************\n")
    


# LOOPING THROUGH KEYS IN A PARTICULAR ORDER:

for name in sorted(favorite_languages):
    print(f"\n{name.title()}, thank you for taking the poll.")
    
print(f"\nThe following languages have been mentiond:\n")
for language in favorite_languages.values():
    print(f"\n{language.title()}.")
    



    

        
