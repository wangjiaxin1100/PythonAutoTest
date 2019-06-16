# sandwich_orders = ['apple','peach','mango']
# finished_sandwiches = []
#
# active = True
# while active:
#     sandwich_order = sandwich_orders.pop()
#     print("I made your " + sandwich_order + " sandwich.")
#     finished_sandwiches.append(sandwich_order)
#     if sandwich_order == 'apple':
#         active = False
# print(finished_sandwiches)


sandwich_orders = ['apple','pastrami','peach','pastrami','mango','pastrami']
print("Pastrami is sold out!")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
finished_sandwiches = sandwich_orders
print(finished_sandwiches)

