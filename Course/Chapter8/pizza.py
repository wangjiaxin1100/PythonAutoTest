# 传递任意数量的实参，形参将他们保存为一个元组
# 位置实参和形参结合
def make_pizza(size,*toppings):
    """打印顾客点的所有配料"""
    print("\nMaking a " + str(size) +
          "-inch pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)
# make_pizza(16,'pepperoni')
# make_pizza(12,'mushrooms','green peppers','extra cheese')
