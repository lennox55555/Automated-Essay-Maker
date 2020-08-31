import requests
import docxModule
import scrapeModule
import searchModule
import time



print("Enter an essay title")
title = input("--> ")
print("")

print("What type of essay are you wanting?\n1 = Research\n2 = Argumentative Essays")
topic = input("-->")

print("Enter desired font")
font1 = input("-->")
print("")

print("Enter font size")
fontSize = int(input("-->"))
print("")

print("Enter desired length of essay")
length = int(input("-->"))
print("")

if topic == "1":
    docxModule.title(title)
    searchModule.openWiki()
    time.sleep(2.5)
    searchModule.searchWiki(title)
    time.sleep(2.5)
    searchModule.selectWeb()
    time.sleep(1.5)
    url1 = searchModule.selectWeb()
    sourceAlpha = requests.get(url1).text
    scrapeModule.scrapeResearch(sourceAlpha, font1, fontSize, title)

elif topic == "2":
    print("Please enter the opposing side of the essay")
    opposing = input("-->")
    docxModule.title(title)
    searchModule.openWiki()
    time.sleep(2.5)
    searchModule.searchWiki(title)
    time.sleep(2.5)
    searchModule.selectWeb()
    time.sleep(1.5)
    url1 = searchModule.selectWeb()
    sourceAlpha = requests.get(url1).text
    #Source2
    searchModule.newTab()
    searchModule.openWiki()
    time.sleep(2.5)
    searchModule.searchWiki(opposing)
    time.sleep(2.5)
    searchModule.selectWeb()
    time.sleep(1.5)
    url2 = searchModule.selectWeb()
    sourceBravo = requests.get(url2).text
    print(url1)
    print(url2)
    docxModule.title(opposing)
    scrapeModule.scrapeArgue(sourceAlpha, sourceBravo, font1, fontSize)

else:
    print("Unknown topic \nError Code A001\n ")









