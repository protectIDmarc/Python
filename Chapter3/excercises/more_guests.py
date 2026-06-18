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