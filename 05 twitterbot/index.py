import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#from webdriver_manager.chrome import ChromeDriverManager
#driver = webdriver.Chrome(ChromeDriverManager().install())
driver = webdriver.Chrome(r".\chromedriver\chromedriver.exe")
web = "https://twitter.com"
driver.get(web)
driver.maximize_window()

time.sleep(8)
#acepto los terminos
try:
    driver.find_element_by_xpath('//*[@id="layers"]/div/div/div/div/div/div[2]/div[1]').click()
except ValueError:
    print(ValueError)
login = driver.find_element_by_xpath("//a[@href='/login']")
login.click()
time.sleep(2)
username = driver.find_element_by_xpath('//input[@autocomplete="username"]')
username.clear()
username.send_keys("universodecoracion@gmail.com")
username.send_keys(Keys.RETURN)
time.sleep(1)
password = driver.find_element_by_xpath('//input[@autocomplete="current-password"]')
password.send_keys("javier2u")
time.sleep(1)
password.send_keys(Keys.RETURN)


#driver.quit()
