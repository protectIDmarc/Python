# # ++++++++++++++ CONDITIONAL TESTS ++++++++++++++

# prompt = "\nEnter a pizza topping to add:"
# prompt += "\nEnter 'quit' when you're finished. "

# topping = ""
# while topping != 'quit':
#     topping = input(prompt)
#     if topping != 'quit':
#         print(f"Adding {topping} to your pizza.")
        
# # ++++++++++++++ ACTIVE FLAG VARIABLE ++++++++++++++
# prompt = "\nEnter a pizza topping to add:"
# prompt += "\nEnter 'quit' when you're finished. "

# active = True
# while active:
#     topping = input(prompt)
#     if topping == 'quit':
#         active = False
#     else:
#         print(f"Adding {topping} to your pizza.")
        
# ++++++++++++++ BREAK STATEMENT ++++++++++++++
prompt = "\nEnter a pizza topping to add:"
prompt += "\nEnter 'quit' when you're finished. "
while True:
    topping = input(prompt)
    if topping == 'quit':
        break
    else:
        print(f"Adding {topping} to your pizza.")


