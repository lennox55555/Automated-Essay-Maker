import docxModule




def narrateDir(text, font1, fontSize, title, narrate, length):
    if narrate == 1 & length == 1:
        onePage(text, font1, fontSize, title)



def onePage(text, font1, fontSize, title):

    essay = "In today's society, almost every " + title + \
            " supporter is familiar with one of these words, inhumane and irrespective. Although the ideology regaurding "\
            + title + " is frequently changing, it is able to touch every social and economic class of our society. " \
                      "While this may pose a minor problem compared to other significant events currently ongoing in" \
                      " the world, in the future it may be a different case"
    docxModule.addPara(essay, font1, fontSize)
    return 1

def twoPage(text, font1, fontSize, title):
    return 2

def threePage(text, font1, fontSize, title):
    return 3

def fourPage(text, font1, fontSize, title):
    return 4

def fivePage(text, font1, fontSize, title):
    return 5

def sixPage(text, font1, fontSize, title):
    return 6

def sevenPage(text, font1, fontSize, title):
    return 7

def eightPage(text, font1, fontSize, title):
    return 8

def ninePage(text, font1, fontSize, title):
    return 9

def tenPage(text, font1, fontSize, title):
    return 10
