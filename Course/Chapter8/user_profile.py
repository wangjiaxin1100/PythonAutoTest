def build_profile(first,last,**user_info):
    """创建一个字典，其中包含我们知道的有关用户的一切"""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    # 遍历user_info中的键-值对，将每个键值都加入到字典profile中
    for key, value in user_info.items():
        profile[key] = value
        return profile
user_profile = build_profile('albert','einstein',
                          location='princeton',
                          field='physics')
print(user_profile)