# Set the age we want to classify.
age = 78

# Check each age bracket in order, top to bottom. Python runs the FIRST
# branch whose condition is True, then skips all the rest. Because the
# checks run in sequence, each elif only needs to set its UPPER limit —
# the lower limit is already guaranteed by the branches that came before.

if age < 2:
    # 0 or 1 years old.
    print('The person is a baby.')

elif age >= 2 and age < 4:
    # 2 or 3 years old.
    print('The person is a toddler.')

elif age >= 4 and age < 13:
    # 4 up to 12 years old.
    print('The person is a kid.')

elif age >= 13 and age < 20:
    # 13 up to 19 years old.
    print('The person is a teenager.')

elif age >= 20 and age < 65:
    # 20 up to 64 years old.
    print('The person is an Adult.')

else:
    # 65 or older — anything not caught above.
    print('The person is an elder.')