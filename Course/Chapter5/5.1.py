char1 = 'monkey'
char2 = 'cat'
if char1 == char2:
    print("They are the same.")
else:
    print("Not equal!")

char2 = 'Monkey'
if char1 == char2.lower():
    print('equal')
else:
    print("not")

animals = ['elephant','dog','mouse','dragon','cat','fish']
animal = 'dog'
if animal in animals:
    print("In")
else:
    print("Not in")

animal = 'elephant'
if animal not in animals:
    print("not in")
else:
    print('in'.title())