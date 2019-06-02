lists = ['zhangliquan','limengfei','lixuan','zhagnwenchao','wangxin']
for i in range(len(lists)):
    print(lists[i])

# 得知有位嘉宾不能参加，因此需要邀请另外一名，已防三缺一
absence = 'wangxin'
lists.remove(absence)
print(absence+' can not appear.')

lists.insert(3,'wangpeng')
print(lists)
for i in range(len(lists)):
    print(lists[i])


lists.insert(0,'yaoshanshan')
lists.insert(3,'wangshuang')
lists.append('guchunye')
for i in range(len(lists)):
    print(lists[i]+',Welcome to my party!')
print("I can only invite two person")
lists_poped = lists.pop(2)
print(lists_poped+',对不起，您不能参加邀请')
lists_poped = lists.pop(2)
print(lists_poped+',对不起，您不能参加邀请')
lists_poped = lists.pop(2)
print(lists_poped+',对不起，您不能参加邀请')
lists_poped = lists.pop(2)
print(lists_poped+',对不起，您不能参加邀请')
lists_poped = lists.pop(2)
print(lists_poped+',对不起，您不能参加邀请')
lists_poped = lists.pop(2)
print(lists_poped+',对不起，您不能参加邀请')
print(len(lists))
print(lists[0]+',你可以继续参加宴会')
print(lists[1]+',你可以继续参加宴会')
del lists[0]
del lists[0]
print(lists)