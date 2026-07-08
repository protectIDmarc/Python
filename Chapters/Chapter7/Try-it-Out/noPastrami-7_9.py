sandwich_orders = ['tuna', 'pastrami', 'veggie', 'pastrami', 'chicken', 'pastrami']
finished_sandwiches = []

print("The deli has run out of pastrami.")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
    