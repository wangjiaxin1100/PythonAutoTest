bicycles = ['trek','cannondale','redline','specialized']
print(bicycles[0].title())
# 返回最后一个元素
print(bicycles[-1])

message = 'My first bicycle was a ' + bicycles[0].title() +'.'
print(message)

# 存储名字，遍历列表
names = ['wangshuang','zhangbo','zhangwenchao','zhangliquan','luhongjian']
for i in range(len(names)):
    print('Hi,'+names[i].title()+',Nice to meet you!')


ways = ['subway','bus','car','bicycle','run','walk']
for i in range(len(ways)):
    if ways[i] == 'subway':
        print("I like go to work by "+ways[i] + '.')
    if ways[i] == 'bicycle':
        print('The best way to work.')
    else:
        print("I dont like this way", ways[i])
