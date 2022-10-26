import requests
from bs4 import BeautifulSoup
import pandas as pd
url = 'https://www.unair.ac.id/news/'

tautan = []
#Nomor 1
response = requests.get(url)
rawhtml = response.text
soup = BeautifulSoup(rawhtml, 'html.parser')
for i in soup.find_all('a'):
    link_web = i.get('href')
    tautan.append(link_web)

doc = pd.DataFrame({'Link': tautan,})

doc.to_csv('URL_UNAIR_news.csv')




