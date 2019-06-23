magicians = ['Dande','Tramp']
def show_magicians(magicians):
    for magician in magicians:
        print("Hello," + magician)

show_magicians(magicians)


def make_greet(magicians,greet_magicians):
    """定义函数，遍历magicians列表
    """
    while magicians:
        magician = magicians.pop()
        # 修改magician为greet magician
        greet_magician = "the Greet " + magician
        # 将greet magician存储到greet_magicians列表中
        greet_magicians.append(greet_magician)
# 入参
magicians = ['Dande','Tramp']
greet_magicians = []
# 函数调用
make_greet(magicians[:],greet_magicians)
show_magicians(magicians)
show_magicians(greet_magicians)
