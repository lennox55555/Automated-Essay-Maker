import docxModule
import re
from bs4 import BeautifulSoup
import format


def scrapeResearch(sourceAlpha, title, narrate, length):
    # sourceA
    soupA = BeautifulSoup(sourceAlpha, 'lxml')
    tags = soupA.find_all('p')
    for txt in tags:
        innerText =  "\"" + txt.text + "\""
        newText= re.sub('....]', '', innerText)
        format.narrateDir(newText, title, narrate, length)














