import docxModule
from bs4 import BeautifulSoup
import requests

def scrapeText(file):
    with open(file) as html_file:
        soup = BeautifulSoup(html_file, 'lxml')
    for article in soup.find_all('div', class_='article'):
        text = article.p.text
        docxModule.newPara()
        docxModule.addPara(text)
