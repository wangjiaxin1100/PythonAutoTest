lists = [1,2,3,'a',5]

# 字典用｛｝表示
dicts = {'username':'zhangsan','password':'123456'}
print (dicts.keys())
print (dicts.values())

# ？？此处不解
print (dicts.items())
for k,v in dicts.items():
    print("dicts keys is %r" %k)
    print("dicts values is %r" %v)

# 通过zip方法合并两个List为Dictionary
# 遍历会按原先的顺序
keys = ['b','a','c','e','d']
values = ['2','1','3','5','4']
for key,value in zip(keys,values):
    print (key,value) 