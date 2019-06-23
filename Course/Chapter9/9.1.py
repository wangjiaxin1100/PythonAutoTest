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

restaurant = Restaurant('Da zhong','Chinese')
restaurant.describe_restaurant()
restaurant.open_restaurant()

restaurant = Restaurant('Gao duan','West')
restaurant.describe_restaurant()

restaurant = Restaurant('Zhong duan','Tai')
restaurant.describe_restaurant()

print(restaurant.number_served)
restaurant.number_served = 25
print(restaurant.number_served)

restaurant.set_number_served(30)
restaurant.increment_number_served(10)
print(restaurant.number_served)

