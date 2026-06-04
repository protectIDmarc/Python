# This works fine. The string is wrapped in DOUBLE quotes (" "), so the
# apostrophe in "Python's" is treated as a normal character inside the string.
message = "One of Python's strengths is its diverse community."
print(message)

# # THIS LINE CAUSES A SYNTAX ERROR.
# # The string is wrapped in SINGLE quotes (' '), but "Python's" also contains
# # a single quote (the apostrophe). Python sees the apostrophe as the END of
# # the string, then gets confused by the leftover text "s strengths...".
message = 'One of Python's strengths is its diverse community.'
print(message)