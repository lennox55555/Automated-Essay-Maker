import docxModule
from bs4 import BeautifulSoup
import requests



def scrapeResearch(sourceAlpha):
    # sourceA
    soupA = BeautifulSoup(sourceAlpha, 'lxml')
    tags = soupA.find_all('p')
    for txt in tags:
        innerText = txt.text
        docxModule.addPara(innerText)
    print(tags)



def scrapeArgue(sourceAlpha, sourceBravo):
    # sourceA
    soupA = BeautifulSoup(sourceAlpha, 'lxml')
    tags = soupA.find_all('p')
    for txt in tags:
        innerText = txt.text
        docxModule.addPara(innerText)
    print(tags)
    #sourceB
    soupB = BeautifulSoup(sourceBravo, 'lxml')
    tags1 = soupB.find_all('p')
    for txt1 in tags1:
        innerText1 = txt1.text
        docxModule.addPara(innerText1)
    print(tags1)





