
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

#文件命名注意不要选selenium,会和模块名重合，导致无法正确导入selenium包
driver = webdriver.Firefox()
#是www.douban.com中嵌入的html页面，直接使用其中的src导向的链接不正确
driver.get("https://accounts.douban.com/passport/login_popup?login_source=anony")

# 模拟点击登录
driver.find_element_by_xpath("/html/body/div[1]/div[1]/ul[1]/li[2]").click()

driver.find_element_by_name("username").send_keys("1863614***6")
driver.find_element_by_name("password").send_keys("5******7")

driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[1]/div[5]/a").click()
# 等待20秒
time.sleep(20)


# 生成登陆后快照
driver.save_screenshot(u"douban.png")

driver.quit()

