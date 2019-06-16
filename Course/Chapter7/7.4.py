# active = True
# while active:
#     pizza = input("Tell me which foot material would you like to add:")
#     if pizza != 'quit':
#         active = True
#         pizza += input("We will add this material.")
#
#     else:
#         active = False
#         print("You have already finish.")

active = True
while active:
    ticket_rates = input("Tell me your age:")
    if ticket_rates == 'quit':
        break
    ticket_rate = int(ticket_rates)
    if ticket_rate < 3:
        print("Ticket rate is free")
    elif (ticket_rate >= 3) and (ticket_rate <= 12):
        print("Ticket rate is 10 dollars")
    else:
        print("Ticket rate is 15 dollars")

x = 1
while  x < 5:
    print('循环执行')