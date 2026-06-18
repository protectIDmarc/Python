# 3.5 SOMEONE CAN'T MAKE IT TO DINNER, SO YOU NEED TO INVITE SOMEONE ELSE.

# First we declare the current list of guests and print the invitations.
guests = ['michael', 'peter', 'luis']

# Now we declare a variable to keep track of the index of the current guest in the list.
selector = 0

# now, for each guest in the list, we print an invitation and then increase the selector by 1 to move to the next guest.
for guest in guests:
    print("Dear " + guests[selector].title() + ", you are cordially invited to dinner.")
    selector += 1
    
# A Guest cannot make it to dinner, so we print a message to that effect and then replace the guest's name in the list with the name of the new guest.
print((f'Unfortunately, {guests[0].title()} can\'t make it to dinner.'))

guests[0] = 'john'

# Now we print the invitations again, using the same loop as before.
selector = 0
for guest in guests:
    print("Dear " + guests[selector].title() + ", you are cordially invited to dinner.")
    selector += 1