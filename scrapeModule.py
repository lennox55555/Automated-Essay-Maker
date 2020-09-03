import docxModule
from bs4 import BeautifulSoup
import format


def scrapeResearch(sourceAlpha, font1, fontSize, title, narrate, length):
    # sourceA
    soupA = BeautifulSoup(sourceAlpha, 'lxml')
    tags = soupA.find_all('p')
    for txt in tags:
        innerText =  "\"" + txt.text + "\""
        format.narrateDir(innerText, font1, fontSize, title, narrate, length)














