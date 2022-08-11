from bs4 import BeautifulSoup
import requests

website = 'https://subslikescript.com/movie/Titanic-46435'
result = requests.get(website)
content = result.text

#soup = BeautifulSoup(content, 'lxml')
soup = BeautifulSoup(content, 'html.parser')

# print(soup.prettify())


box = soup.find('article', class_='main-article')

title = box.find('h1').get_text()

transcript = box.find('div', class_='full-script').get_text(strip=True, separator=' ')
print(title)
print(transcript)