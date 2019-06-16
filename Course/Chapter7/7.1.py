# car = input("Do you want to rent a car?")
# print("Let me see if I can find you a "+str(car)+ ".")

# member = input("How many people will come for the dinner?")
# member = int(member)
# if member > 8:
#     print("There is not a table for you.")
# else:
#     print("There is a table for you.")

number = input("Please type a number,and I will tell you is or not %10:")
if int(number) % 10 == 0:
    print(number + " is integral multiple.")
else:
    print(number + " is not intergral multiple")