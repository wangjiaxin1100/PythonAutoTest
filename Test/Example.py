import unittest


# 测试类必须要继承unittest.TestCase
class TestMethod(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('类执行之前')

    @classmethod
    def tearDownClass(cls):
        print('类结束之后')

    # 每一个测试方法开始要执行的方法
    def setUp(self):
        print("测试方法开始啦")

    # 每一个测试方法结束后执行的方法
    def tearDown(self):
        print("测试方法结束啦")

    # 测试方法必须要以test开头！！！
    def test01(self):
        print("这个是测试方法01")

    def test02(self):
        print("这个是测试方法02")


# if __name__ == "__main__":