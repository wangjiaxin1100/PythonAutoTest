from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

# 打开谷歌浏览器
driver = webdriver.Chrome()
# 输入访问地址
driver.get("http://10.10.108.20:7001/abfx/login.action")
# 窗口最大化
driver.maximize_window()
# 输入用户名
driver.find_element_by_id("j_username").send_keys("cx_admin")
# 输入密码
driver.find_element_by_name("j_password").send_keys("111111")
# 输入验证码
driver.find_element_by_name("j_captcha").send_keys("1111")
# 点击登录
driver.find_element_by_id("IbtnEnter").click()
# 使用ActionChains鼠标拖动至SARMRA
mouse_move_sarmra = driver.find_element_by_xpath('//*[@id="menu"]/a[6]')
ActionChains(driver).move_to_element(mouse_move_sarmra).perform()
# 使用ActionChains鼠标拖动至SARMRA评估管理
mouse_move_sarmra_manage = driver.find_element_by_xpath('//*[@id="ext-gen4"]/div[8]/ul/li[1]/div/a')
# 使用ActionChains鼠标拖动至SARMRA评估计划
ActionChains(driver).move_to_element(mouse_move_sarmra_manage).perform()
mouse_move_sarmra_manage_plan = driver.find_element_by_xpath('//*[@id="ext-gen4"]/div[8]/ul/li[1]/div/a/div/ul/li[1]/a').click()
time.sleep(2)
# 点击新增按钮
driver.find_element_by_id('ext-gen88').click()
# 输入计划名称
driver.find_element_by_id('ext-comp-1054').send_keys('20190615')
# 输入计划描述
driver.find_element_by_id('ext-comp-1055').send_keys('20190615')
time.sleep(2)
# 点击时间控件
driver.find_element_by_xpath('//*[@id="ass_end_dt_id"]').click()
time.sleep(2)
# 点击今天
driver.find_element_by_css_selector('#ext-gen240').click()
time.sleep(2)
#点击立即执行
driver.find_element_by_xpath('//table[@id="ext-comp-1061"]/tbody/tr[2]/td[2]/em/button').click()
time.sleep(10)
# 点击弹出框确定
driver.find_element_by_xpath('//*[@id="ext-gen256"]').click()
# 退出登录
driver.find_element_by_xpath('//*[@id="t_header_tb"]/table/tbody/tr[1]/td/a[2]').click()



