from selenium import webdriver


driver = webdriver.Chrome()
driver.get('https://www.baidu.com')
driver.refresh() #刷新当前页面

print(driver.title)

driver.quit()
