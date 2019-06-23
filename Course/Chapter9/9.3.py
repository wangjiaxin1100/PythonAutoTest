class User():
    def __init__(self,first_name,last_name,description):
        self.first_name = first_name
        self.last_name = last_name
        self.description = description
        self.full_name = self.first_name.title() +" " + self.last_name.title()
        self.login_attempts = 0

    def describe_user(self):
        print(self.description)

    def greet_user(self):
        print("Hello," + self.full_name + ".")

    def increment_login_attempts(self):
        # 调用该方法使尝试登陆次数加1
        self.login_attempts += 1
    def reset_login_attempts(self):
        self.login_attempts = 0

donald_John_Trump  = User('donald','trump',
                          "Beijing",)

donald_John_Trump.describe_user()
donald_John_Trump.greet_user()

chen_hongyu = User('chen','hongyu','finance')
chen_hongyu.describe_user()
chen_hongyu.greet_user()

wangjiaxin = User('wang','jiaxin','age=30')
wangjiaxin.increment_login_attempts()
wangjiaxin.increment_login_attempts()
wangjiaxin.increment_login_attempts()
print(wangjiaxin.login_attempts)
wangjiaxin.reset_login_attempts()
print(wangjiaxin.login_attempts)