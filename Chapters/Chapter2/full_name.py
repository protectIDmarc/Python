# Store the first and last name as separate string variables
first_name = "luis"
last_name = "marques"

# Use an f-string to combine the two names into a single full name (with a space between)
full_name = f"{first_name} {last_name}"
print(full_name)

# .title() capitalises the first letter of each word: "luis marques" -> "Luis Marques"
print(f"Hello, {full_name.title()}!")

# Same as above, but storing the greeting in a variable first, then printing it
full_name = f"{first_name} {last_name}"
message = f"Hello, {full_name.title()}!"
print(message)


# Plain print with no special characters
print("Python")
# \t inserts a tab (indent); \n inserts a newline (line break after "Python")
print("\tPython\n")

# \n breaks the text onto a new line each time, creating a vertical list
print("Languages:\nPython\nC\nJavaScript")

# Combine \n (newline) and \t (tab) to create an indented list
print("Languages:\n\tPython\n\tC\n\tJavaScript")

# This string has a leading space and a trailing space + period: ' python .'
favourite_language = ' python .'
print(favourite_language)

# .rstrip(" .") removes spaces and periods from the RIGHT-hand end -> ' python'
print(favourite_language.rstrip(" ."))
# .lstrip() removes whitespace from the LEFT-hand end -> 'python .'
print(favourite_language.lstrip())

# .removeprefix() strips the given text from the START of the string
nostarch_url = 'https://nostarch.com'
nostarch_url = nostarch_url = nostarch_url.removeprefix('https://')
print(nostarch_url)