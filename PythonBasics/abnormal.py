try:
    open("abc.txt",'r')
except Exception:
    print("异常了！")

try :
    print(aa)
except BaseException:
    print("Name异常了！")

try :
    open("abc.txt",'r')
    print(aa)
except BaseException as msg:
    print(msg)

# try except else搭配使用
try:
    aa = "异常测试："
    print(aa)
except Exception as msg:
    print(msg)
else:
    print("没有异常！")
finally:
    print("不管是否异常，我都会执行。")


from random import randint
number = randint(1,9)
if number % 2 == 0:
    raise NameError("%d is even" %number)
else:
    raise NameError("%d is odd" %number)