import requests
import docxModule
import scrapeModule

sourceAlpha = requests.get('http://coreyms.com').text
sourceBravo = requests.get('http://coreyms.com').text

print("Enter an essay title")
title = input("--> ")
docxModule.title(title)
print("")

print("What type of essay are you wanting?\n1 = Research\n2 = Argumentative Essays\n3 = Descriptive\n4 = Narrative\n5 = Expository Essay")
topic = input("-->")
if (topic == "1"):
    scrapeModule.scrapeResearch(sourceAlpha)
elif (topic == "2"):
    scrapeModule.scrapeArgue(sourceAlpha, sourceBravo)
else:
    print("Unknown topic \nError Code A001\n ")

print("Enter desired font")
font = input("-->")
print("")
#docxModule.font(font)

print("Enter font size")
fontSize = input("-->")
print("")
#docxModule.fontSize(fontSize)

print("Enter desired line-spacing")
lineSpacing = input("-->")
print("")



#a = doc.paragraphs[0].text
#b = doc.paragraphs[1].text
#print(doc.paragraphs[1].runs[0].text)
#print(a + b)



