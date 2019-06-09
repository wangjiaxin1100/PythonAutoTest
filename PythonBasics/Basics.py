# %s字符串 %d数字 %r任意

# n = input("Enter any content:")
# print ("Your input is %r"%n)

age = 29
print ("You are %d !"%age)

'''
分支循环
'''

a = 2
b = 3
if a > b:
    print ('a max!')
else:
    print ('b max!')

# 使用in判断字符是否包含
hi = 'hello world'
if 'hell' in hi:
    print ('contain')
else:
    print ('Not Contain')

results = 72
if results >= 90:
    print ('优秀')
elif results >= 70:
    print ('良好')
elif results >= 60:
    print ('合格')
else:
    print ('不合格')

# 对字符串遍历
for i in "hello world":
    print (i)

# 对列表遍历
fruits = ['banana','apple','mango']
for fruit in fruits:
    print (fruit)

# 利用range()函数来进行一定次数循环
for i in range(5):
    print (i)

# range(start,end[step])开始结束及步长
for i in range(1,10,2):
    print (i)