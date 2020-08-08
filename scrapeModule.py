import docxModule
from bs4 import BeautifulSoup
import requests



def scrapeResearch(sourceAlpha):
    # sourceA
    soupA = BeautifulSoup(sourceAlpha, 'lxml')
    for articleA in soupA.find_all('article'):
        summaryA = articleA.find('div', class_='entry-content').p.text
        docxModule.newPara()
        docxModule.addPara(summaryA)


def scrapeArgue(sourceAlpha, sourceBravo):
    # sourceA
    soupA = BeautifulSoup(sourceAlpha, 'lxml')
    for articleA in soupA.find_all('article'):
        summaryA = articleA.find('div', class_='entry-content').p.text
        docxModule.newPara()
        docxModule.addPara(summaryA)
    #sourceB
    soupB = BeautifulSoup(sourceBravo, 'lxml')
    for articleB in soupB.find_all('article'):
        summaryB = articleB.find('div', class_='entry-content').p.text
        docxModule.newPara()
        docxModule.addPara(summaryB)


def scrapeExpo():
    print("add expository essay code")


def scrapeDescript():
    print("add descriptive essay code")

def scrapeNarrate():
    print("add narrative essay code")


