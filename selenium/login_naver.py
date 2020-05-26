from selenium import webdriver

driver = webdriver.Chrome("./driver/chromedriver")
driver.implicitly_wait(3)
driver.get("https://nid.naver.com/nidlogin.login")

driver.find_element_by_name('id').send_keys('asdf')
driver.find_element_by_name('pw').send_keys('qwer')

driver.find_element_by_xpath('//*[@id="frmNIDLogin"]/fieldset/input').click()
