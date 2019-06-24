class Restaurant():

    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    # 创建一个名为describe_restaurant()方法
    def describe_restaurant(self):
        print("Welcome to " + self.restaurant_name + ".")
        print("Our restaurant is " + self.cuisine_type + ".")


    # 创建一个名为open_restaurant()方法
    def open_restaurant(self):
        print("Now is Open")

    def set_number_served(self,numbers):
        # 设置就餐人数
        self.number_served = numbers

    def increment_number_served(self,add_number):
        # 通过传递参数值方式增加就餐人数
        self.number_served += add_number