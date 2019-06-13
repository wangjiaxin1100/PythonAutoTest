from selenium import webdriver
# 引入 ActionChains 类
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.get("http://10.10.134.232:7001/login.jsp")
driver.set_window_size(1920, 1080)
driver.find_element_by_id("userId").send_keys("AB000046")
driver.find_element_by_id("password").send_keys("000000")
driver.find_element_by_css_selector(".loginBtn").click()
mouse_move = driver.find_element_by_link_text("切换风格")
ActionChains(driver).move_to_element(mouse_move).perform()
driver.find_element_by_xpath("//a[contains(text(),\'传统风格\')]").click()
driver.switch_to.frame(3)
driver.find_element_by_id("icon_arrow").click()