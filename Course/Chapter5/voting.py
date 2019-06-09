age = 19
if age > 18 :
    print("You are lod enough to vote!")


age = 64
if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age < 65:
    price = 10
else:
    price = 20
print("You should pay for "+ str(price) +".")