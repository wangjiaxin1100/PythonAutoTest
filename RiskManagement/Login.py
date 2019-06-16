from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import unittest

class TestMethod(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        Open_Browser  = driver = webdriver.Chrome()
        print('类执行之前')

    @classmethod
    def tearDownClass(cls):
        print('类结束之后')

    def setUp(self):
        print("测试方法开始啦")
        Open_adress = driver.get("http://10.10.108.20:7001/abfx/login.action")
        Set_Window_Size = driver.set_window_size(1920, 1080)
        User_Name = driver.find_element_by_id("j_username").send_keys("cx_admin")
        Password = driver.find_element_by_name("j_password").send_keys("111111")
        Captcha = driver.find_element_by_name("j_captcha").send_keys("1111")
        IbtonEnter = driver.find_element_by_id("IbtnEnter").click()

    # 每一个测试方法结束后执行的方法
    def tearDown(self):
        print("测试方法结束啦")
# driver = webdriver.Chrome()
# driver.get("http://10.10.108.20:7001/abfx/login.action")
# driver.set_window_size(1920, 1080)
# driver.find_element_by_id("j_username").send_keys("cx_admin")
# driver.find_element_by_name("j_password").send_keys("111111")
# driver.find_element_by_name("j_captcha").send_keys("1111")
# driver.find_element_by_id("IbtnEnter").click()
# mouse_move_sarmra = driver.find_element_by_xpath('//*[@id="menu"]/a[6]')
# ActionChains(driver).move_to_element(mouse_move_sarmra).perform()
# mouse_move_sarmra_manage = driver.find_element_by_xpath('//*[@id="ext-gen4"]/div[8]/ul/li[1]/div/a')
# ActionChains(driver).move_to_element(mouse_move_sarmra_manage).perform()
# mouse_move_sarmra_manage_plan = driver.find_element_by_xpath('//*[@id="ext-gen4"]/div[8]/ul/li[1]/div/a/div/ul/li[1]/a').click()
