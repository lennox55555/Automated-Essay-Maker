import docxModule
import scrapeModule

file = 'simple.html'

print("Enter an essay title")
title = input("--> ")
docxModule.title(title)

print("Is this a Research Essay or an Argumentative Essay")
topic = input("-->")

print("Enter desired font")
font = input("-->")
#docxModule.font(font)

print("Enter font size")
fontSize = input("-->")
#docxModule.fontSize(fontSize)

print("Enter desired line-spacing")
lineSpacing = input("-->")

scrapeModule.scrapeText(file)


