from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.get("http://10.10.108.20:7001/abfx/login.action")
driver.set_window_size(1920, 1080)
driver.find_element_by_id("j_username").send_keys("cx_admin")
driver.find_element_by_name("j_password").send_keys("111111")
driver.find_element_by_name("j_captcha").send_keys("1111")
driver.find_element_by_id("IbtnEnter").click()
mouse_move_sarmra = driver.find_element_by_xpath('//*[@id="menu"]/a[6]')
ActionChains(driver).move_to_element(mouse_move_sarmra).perform()
mouse_move_sarmra_manage = driver.find_element_by_xpath('//*[@id="ext-gen4"]/div[8]/ul/li[1]/div/a')
ActionChains(driver).move_to_element(mouse_move_sarmra_manage).perform()
mouse_move_sarmra_manage_plan = driver.find_element_by_xpath('//*[@id="ext-gen4"]/div[8]/ul/li[1]/div/a/div/ul/li[1]/a').click()
