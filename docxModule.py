import docx

def title(topic):
    doc = docx.Document('Document.docx')
    doc.add_paragraph(topic)
    doc.save("Document.docx")
    return "1"


def newPara():
    doc = docx.Document('Document.docx')
    doc.save("Document.docx")
    return "2"


def addPara():
    doc = docx.Document('Document.docx')
    doc.save("Document.docx")
    return "3"


def fontSize():
    doc = docx.Document('Document.docx')
    doc.save("Document.docx")
    return "4"


def paraSpace():
    doc = docx.Document('Document.docx')
    doc.save("Document.docx")
    return "5"



