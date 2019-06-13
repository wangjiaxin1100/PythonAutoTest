# open("abc.txt",'r')

try :
    open("abc.txt",'r')
except FileNotFoundError:
    print("异常了！")

try :
    print(aa)
except NameError:
    print("Name异常了！")