import pandas as pd
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9999") #con esto y una configuración espacial del navegador siempre habro twitter logeado
driver = webdriver.Chrome(r"..\chromedriver\chromedriver.exe", options=chrome_options)

driver.get("https://twitter.com/search?q=%23python&src=typed_query")
try:
    driver.maximize_window()
except:
    try:
        driver.driver.manage().window().maximize()
    except:
        pass
time.sleep(4)
scrolling = True
users=[]
tweets=[]
while scrolling:
    articles = driver.find_elements_by_xpath('//article[@data-testid="tweet"]')
    for article in articles[-15:]:
        try:
            tweet = article.find_element_by_xpath('.//div[@lang="es"]').text
        except:
            tweet = False
        if tweet:
            try:
                user=article.find_element_by_xpath('.//span[ contains (text(), "@")]').text
                tweet= tweet=" ".join(tweet.split())
                if tweet not in tweets:
                    print (tweet)
                    users.append(user)
                    tweets.append(tweet)

            except ValueError:
                print(ValueError)
            #print ('algo a salido mal')
    #vamos haciendo scroll hasta que se termine el scroll o llege a 50 items
    last_height = driver.execute_script("return document.body.scrollHeight")
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(4)
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height :
        print("Ha llegado al final del scroll")
        scrolling = False
    else:
        last_height = new_height
    if len(users) > 50:
        print("Mas de 50 items")
        scrolling = False
tweets_dl = []
driver.get("https://www.deepl.com/en/translator")
for tweet in tweets:
    fuente = driver.find_element_by_xpath('//textarea[@aria-labelledby="translation-source-heading"]')
    fuente.clear()
    time.sleep(5)
    fuente.send_keys(tweet)
    time.sleep(5)
    try:
        destino = driver.find_element_by_id('target-dummydiv')
        tweets_dl.append(destino.get_attribute('innerHTML'))
    except ValueError:
        tweets_dl.append("")
        destino = "no ha encontrado nada"



df_tweets = pd.DataFrame({"usuarios":users,"tweets":tweets_dl})
df_tweets.to_csv("tweets-autoscroll-dl.csv",index=False)