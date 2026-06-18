# First we declare the current list of guests and print the invitations.
guests = ['john', 'peter', 'luis']

# now, for each guest in the list, we print an invitation and then increase the selector by 1 to move to the next guest.
def print_invitations(guests):
    for guest in guests:
        print("Dear " + guest.title() + ", you are cordially invited to dinner.")

print_invitations(guests)

print("\nI found a bigger table!\n")

# Now we add new guests to the list. We use the insert() method to add a new guest at the beginning of the list, and the append() method to add a new guest at the end of the list. We also use the insert() method again to add a new guest in the middle of the list.
guests.insert(0, 'connor')
guests.append('sarah')
guests.insert(len(guests) // 2, 'siobhan')


print_invitations(guests)

print(f"\nI currently have {len(guests)} people for dinner, but can now ONLY invite 2 people for dinner because i cannot arrange a piss-up in a brewery.\n")

# HERE I KNOW MY LSIT IS 6 LONG. I COULD USE A WHILE LOOP TO POP GUESTS UNTIL THE LENGTH OF THE LIST IS 2, BUT I KNOW THAT I NEED TO POP 4 GUESTS.
# SO I WILL JUST USE A FOR LOOP TO POP 4 GUESTS.
for i in range(len(guests) - 2):
    removed_guest = guests.pop()
    print(f'Sorry, {removed_guest.title()}, I can\'t invite you to dinner.')
    
print("\nThe guests that are still invited to dinner are:")
print_invitations(guests)

# Now I will remove all guests from the list, and print the list to show that it is empty.
del guests[0]
del guests[0]
print(f"\nThe list of guests is now empty: {guests}")