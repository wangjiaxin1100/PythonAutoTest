from random import randint
class Die():
    """定义一个色子"""
    def __init__(self):
        self.sides = 6

    def roll_die(self):
        number = randint(1,self.sides)
        print(number)

die = Die()
die.roll_die()
die.sides = 10
die.roll_die()
die.sides = 20
die.roll_die()