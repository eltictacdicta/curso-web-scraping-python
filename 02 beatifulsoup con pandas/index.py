from bs4 import BeautifulSoup
import requests
import pandas as pd

root = 'https://subslikescript.com'
website = f'{root}/movies'
result = requests.get(website)
content = result.text
soup = BeautifulSoup(content, 'lxml')
#soup = BeautifulSoup(content, 'html.parser')

# print(soup.prettify())
box = soup.find('article', class_='main-article')

links = []
for link in box.find_all('a', href=True):
    links.append(link['href'])

titles=[]
transcripts=[]
for link in links:
    try:
        website = f'{root}/{link}'
        result = requests.get(website)
        content = result.text
        soup = BeautifulSoup(content, 'lxml')
        box = soup.find('article', class_='main-article')
        titles.append(box.find('h1').get_text())
        transcripts.append(box.find('div', class_='full-script').get_text(strip=True, separator=' '))
    except:
        print ("En esta iteración ha habido un error")



dict_transcripts = {'Titulos':titles, 'Transcripciones':transcripts}
df_transcripts = pd.DataFrame.from_dict(dict_transcripts)
df_transcripts.to_csv('transcripciones.csv', index=False)
#print(df_poblacion)