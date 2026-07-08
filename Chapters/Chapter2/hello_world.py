# Assign a string value to the variable 'message'
message = "Hello Python World!"
# Print the current value of 'message' to the console
print(message)

# Reassign 'message' with a new string value (this overwrites the previous value)
message = "Hello Python Crash Course World!"
# Print the updated value of 'message'
print(message)

# NOTE: 'mesage' is spelled differently from 'message' above — it's a separate variable.
# This looks like a typo. Python treats it as a brand-new variable rather than
# reusing 'message', which is a common source of bugs.
mesage = "Hello Python Crash Course World!"
# Print the value of 'mesage' (the misspelled variable)
print(mesage)