import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://twitter.com/login")
print(driver.title)
time.sleep(10)
#acepto los terminos
try:
    driver.find_element_by_xpath('//*[@id="layers"]/div/div/div/div/div/div[2]/div[1]').click()
except ValueError:
    print(ValueError)
search_bar = driver.find_element_by_name('text')
search_bar.clear()
search_bar.send_keys("universodecoracion@gmail.com")
search_bar.send_keys(Keys.RETURN)
time.sleep(5)

#driver.close()
