import docxModule
from bs4 import BeautifulSoup
import format


def scrapeResearch(sourceAlpha, font1, fontSize):
    # sourceA
    soupA = BeautifulSoup(sourceAlpha, 'lxml')
    tags = soupA.find_all('p')
    for txt in tags:
        innerText = txt.text
        docxModule.addPara(innerText, font1, fontSize)
    format.test(tags)


def scrapeArgue(sourceAlpha, sourceBravo, font1, fontSize):
    # sourceA
    soupA = BeautifulSoup(sourceAlpha, 'lxml')
    tags = soupA.find_all('p')
    for txt in tags:
        innerText = txt.text
        docxModule.addPara(innerText, font1, fontSize)

    #sourceB
    soupB = BeautifulSoup(sourceBravo, 'lxml')
    tags1 = soupB.find_all('p')
    for txt1 in tags1:
        innerText1 = txt1.text
        docxModule.addPara(innerText1, font1, fontSize)






