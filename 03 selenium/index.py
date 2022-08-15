from time import sleep
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
import time
import pandas as pd


driver = webdriver.Chrome(ChromeDriverManager().install())
website= 'https://www.adamchoi.co.uk/teamgoals/detailed'
driver.get(website)

all_matches_button = driver.find_element_by_xpath('//label[@analytics-event="All matches"]')
all_matches_button.click()

dropdown = Select(driver.find_element_by_id('country'))
dropdown.select_by_visible_text('Spain')
dropdown = Select(driver.find_element_by_id('season'))
dropdown.select_by_visible_text('21/22')
time.sleep(3)

matches = driver.find_elements_by_tag_name('tr')

partidos = []
for match in matches:
    #print(match.text)
    partidos.append(match.text)

driver.quit()

df = pd.DataFrame({'partidos':partidos})
print(df)
df.to_csv('partidos.csv', index=False)