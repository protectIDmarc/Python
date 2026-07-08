# range(1, 21, 2) generates numbers starting at 1, stopping BEFORE 21,
# stepping by 2 each time -> 1, 3, 5, 7 ... 19 (all the odd numbers).
#
# The three arguments are: range(start, stop, step)
#   start = 1   -> begin at 1
#   stop  = 21  -> stop before 21, so 20 would have been the last possible
#                  value, but the step of 2 means we land on 19
#   step  = 2   -> jump forward 2 each time, which skips every even number
#
# range() on its own produces a lazy "range object", not an actual list.
# Wrapping it in list() forces it to build the real list [1, 3, 5, ..., 19].
odd_numbers = list(range(1, 21, 2))

# Loop through the list one item at a time. On each pass, the variable
# odd_number holds the current value, which we then print.
for odd_number in odd_numbers:
    print(odd_number)