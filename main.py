import docxModule
import scrapeModule

print("Enter an essay topic")
topic = input("--> ")
docxModule.title(topic)
scrapeModule.test()

#a = doc.paragraphs[0].text
#b = doc.paragraphs[1].text
#print(doc.paragraphs[1].runs[0].text)
#print(a + b)



