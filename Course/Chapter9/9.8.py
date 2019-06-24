class Privileges():
    def __init__(self):
        self.privileges = ['can add post','can delete post','can ban user']

    def show_privileges(self):
        for self.privilege in privileges:
            print("Admin " + self.privilege + ".")

