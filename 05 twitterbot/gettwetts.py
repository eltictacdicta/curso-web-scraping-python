import pandas as pd
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9999") #con esto y una configuración espacial del navegador siempre habro twitter logeado
driver = webdriver.Chrome(r"..\chromedriver\chromedriver.exe", options=chrome_options)

driver.get("https://twitter.com/search?q=%23Python&src=typeahead_click&f=top")
try:
    driver.maximize_window()
except:
    try:
        driver.driver.manage().window().maximize()
    except:
        pass

time.sleep(4)
articles = driver.find_elements_by_xpath('//article[@data-testid="tweet"]')
users=[]
tweets=[]
for article in articles:
    try:
        tweet=article.find_element_by_xpath('.//div[@lang]').text
        tweet=" ".join(tweet.split())
        tweets.append(tweet)
    except:
        tweets.append('')


    try:
        users.append(article.find_element_by_xpath('.//span[ contains (text(), "@")]').text)
    except:
        users.append('')

df_tweets = pd.DataFrame({"usuarios":users,"tweets":tweets})
df_tweets.to_csv("tweets.csv",index=False)