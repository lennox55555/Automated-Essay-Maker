import requests
import docxModule
import scrapeModule
import searchModule
import time



print("This program will write a research essay after several questions are answered \nPlease enter a noun that you would like to have the essay based on (A noun is a person, place, thing)")

title = input("--> ")
print("")

print("Would you like the essay to 1.talk greatly upon " + title + "or 2.down upon " + title + " (Please type in a 1 or 2)")
narrate = int(input("-->"))

print("In what time frame would you like this essay to be discussed in? (Ex: 1910) ")
year = int(input("-->"))

print("Enter desired font")
font1 = input("-->")
print("")

print("Enter font size")
fontSize = int(input("-->"))
print("")

print("Enter desired length of essay")
length = int(input("-->"))
print("")


docxModule.title(title)
searchModule.openWiki()
time.sleep(2.5)
searchModule.searchWiki(title)
time.sleep(2.5)
searchModule.selectWeb()
time.sleep(1.5)
url1 = searchModule.selectWeb()
sourceAlpha = requests.get(url1).text
scrapeModule.scrapeResearch(sourceAlpha, font1, fontSize, title, narrate, length)














