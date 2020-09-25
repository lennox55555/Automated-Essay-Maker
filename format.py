import docxModule


def narrateDir(text, title, narrate, length):
    if narrate == 1 & length == 1:
        onePage(text, title, length)



def onePage(text, title, length):
    if "good" in text:
        while length <= 1:
            essayIntro = "     In today's society, almost every " + title + \
            " supporter is familiar with one of these words, adaptable and courageous. Although the ideology regaurding "\
            + title + " is frequently changing, it is able to touch every social and economic class of our society. " \

            docxModule.addPara(essayIntro)
            essayBody = "     While this may pose a minor problem compared to other significant events currently ongoing in" + \
            " the world, in the future it may be a different case. " + title + " has exceeded expectations all" \
            " across the board, for example; " + text + " While this evidence may not constitute " + title + \
            " in the most viable way, it is certainly an accomplishment of many. "

            docxModule.addPara(essayBody)
            essayConclusion = "     To conclude " + title + " has impacted this world greatly. At times, the work of " + title + \
            " may go unseen, undocumented, and unappreciated but it is cruicial that we appraise the work that "\
            " has been put forth and realize that there is so much that man or machine can do."
            docxModule.addPara(essayConclusion)
            length + 1
            return 2

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
