favourite_lanagues = {
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python',
}
print("Sarah's favourite is "+
      favourite_lanagues['sarah'].title()+
      ".")

for name,lanague in favourite_lanagues.items():
    print(name.title() +"'s favorite language is "+
          lanague.title() + ".")

# 6.3.2遍历字典中所有键
for name in favourite_lanagues.keys():
    print(name.title())

# 打印出朋友喜欢的语言
friends = ['phil','sarah']
for name in favourite_lanagues.keys():
    print(name.title())
    if name in friends:
        print("Hi"+ name.title()+
              ",I see your favorite lanage is "+
              favourite_lanagues[name].title() + ".")

favourite_lanagues = {
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python',
}

if 'erin' not in favourite_lanagues.keys():
    print("Erin,please take our poll!")

for name in sorted(favourite_lanagues.keys()):
    print(name.title() + ",thank you for taking the poll.")

# 提取字典中的值
for lanague in favourite_lanagues.values():
    print(lanague.title())

# set()方法调用
for lanague in set(favourite_lanagues.values()):
    print(lanague.title())