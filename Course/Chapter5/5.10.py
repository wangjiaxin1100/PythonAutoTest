current_users = ['user1','user2','user3','user4','user5']
new_users = ['User2','user5','user6','user7','user8']
for new_user in new_users:
    if new_user.lower() in current_users:
        print(new_user + " has already in use,please try another one!")
    else:
        print("you can use this name.")