alien_color = 'red'
if alien_color == 'green':
    print("You get 5 points!")

if alien_color == 'green':
    print("You get 5 points")
if alien_color == 'yellow':
    print("You get 10 points")
if alien_color == 'red':
    print("You get 15 points")


age  = 1
if age < 2:
    print("Baby")
elif age < 4:
    print("panshanxuebu")
elif age < 13:
    print("child")
elif age < 20:
    print("adult")
elif age < 65:
    print("chengnianren")
elif age > 65:
    print("laonianren")
else:
    print("输入错误")


favorite_fruits = ['apple','banana','orange','peach']
favorite_fruit = 'banana'
if favorite_fruit in favorite_fruits:
    print("You really like banbana")