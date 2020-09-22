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

def twoPage():
    return 2

def threePage():
    return 3

def fourPage():
    return 4

def fivePage():
    return 5

def sixPage():
    return 6

def sevenPage():
    return 7

def eightPage():
    return 8

def ninePage():
    return 9

def tenPage():
    return 10
