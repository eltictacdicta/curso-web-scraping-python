
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
#con la siguiente opcion permito crear una instancia de chorme para poder usar selenium con el chrome abierto, lo unico que hay que ejecutar el chorme con el acceso directo de antes que hay en la reiz del proyecto y tener instalado chorme en la misma versión del test driver 
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9999")
driver = webdriver.Chrome(r"..\chromedriver\chromedriver.exe", options=chrome_options) #busco el ejecutable de chormedriver que esta en la carpeta superior

driver.get("https://twitter.com/search?q=%23Python&src=typeahead_click&f=top")