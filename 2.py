import requests
from bs4 import BeautifulSoup
import pandas as pd
from random import randint
from time import sleep

headline = []
taut = []

url = 'https://www.unair.ac.id/category/berita/page/'

for page in range(1,5):
    response = requests.get(url + str(page))

    page_html = BeautifulSoup(response.text, 'html.parser')
    berita = page_html.findAll('div', class_="elementor-post__card")

    for container in berita:
        name_raw = container.h3.a.text
        name = name_raw.replace('\n\t\t\t\t', '')
        headline.append(name)

        link = container.find('a', href=True)['href']
        taut.append(link)

nama_artikel = pd.DataFrame({'Berita': headline, 'Tautan': taut,})
print(nama_artikel)

nama_artikel.to_csv('Headline_Berita_UNAIR_News.csv')