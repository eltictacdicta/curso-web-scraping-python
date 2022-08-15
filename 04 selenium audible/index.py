import pandas as pd
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
#driver = webdriver.Chrome(ChromeDriverManager().install())
web = "https://www.audible.es/search"

#opciones para trabajar en modo headless
options = Options()
options.headless = False
#options.add_argument('window-size=1920x1080')
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
driver.get(web)
driver.maximize_window()


#paginacion


container = driver.find_element_by_class_name('adbl-impression-container ')
products = container.find_elements_by_xpath('./li')

book_title = []
book_author = []
book_length = []

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


driver.quit()

df_books = pd.DataFrame({'title':book_title,'author':book_author,'length':book_length})
if options.headless:
    df_books.to_csv('books_headless.csv',index=False)
else:
    df_books.to_csv('books.csv',index=False)