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

class Admin(User):
    def __init__(self,first_name,last_name,description):
        super().__init__(first_name,last_name,description)
        #9-8将实例用作属性
        self.privilege =  Privileges()


class Privileges():
    def __init__(self):
        self.privileges = ['can add post','can delete post','can ban user']

    def show_privileges(self):
        for self.privilege in privileges:
            print("Admin " + self.privilege + ".")

privileges = ['can add post','can delete post','can ban user']
# admin = Admin('admin','admin','administor')
# admin.privilege.show_privileges()