import time 
import pandas as pd
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
#driver = webdriver.Chrome(ChromeDriverManager().install())
web = "https://www.audible.es/adblbestsellers"

#opciones para trabajar en modo headless
options = Options()
options.headless = True
#options.add_argument('window-size=1920x1080')
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
driver.get(web)
driver.maximize_window()


#paginacion
pagination = driver.find_element_by_xpath("//ul[contains(@class,'pagingElements')]")
pages = pagination.find_elements_by_tag_name('li')
last_page = int(pages[-2].text)



current_page = 1
book_title = []
book_author = []
book_length = []

while current_page <= last_page:
    time.sleep(2)
    container = driver.find_element_by_class_name('adbl-impression-container ')
    products = container.find_elements_by_xpath('./li')

    for product in products:
        try:
            title=product.find_element_by_xpath('.//h3[contains(@class,bcheading)]').text
        except: 
            title=''
        book_title.append(title)
        print(title)
        try:
            book_author.append(product.find_element_by_xpath('.//li[contains(@class,"authorLabel")]').text)
        except:
            book_author.append('')
        try:
            book_length.append(product.find_element_by_xpath('.//li[contains(@class,"runtimeLabel")]').text)
        except:
            book_length.append('')

    current_page = current_page + 1
    
    try:
        driver.find_element_by_id('truste-consent-button').click()
    except:
        pass
    
    try:
        next_page = driver.find_element_by_xpath("//span[contains(@class,'nextButton')]")
        print(next_page.text)
    except:
        print('No encontró la data')
    try:
        next_page.click()
    except ValueError:
        print("No hizo click"+ValueError)


driver.quit()

df_books = pd.DataFrame({'title':book_title,'author':book_author,'length':book_length})
if options.headless:
    df_books.to_csv('books_headless.csv',index=False)
else:
    df_books.to_csv('books.csv',index=False)