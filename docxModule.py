import docx
from docx import Document, document
from docx.shared import Pt
from docx.enum.style import WD_STYLE_TYPE
from docx.enum.text import WD_PARAGRAPH_ALIGNMENT



def title(title):
    doc = docx.Document('Document.docx')
    doc.add_paragraph(title)
    font.size = Pt(12)
    font.name = 'Times New Roman'
    document = Document('Document.docx')
    paragraph = document.add_paragraph()
    paragraph.alignment = WD_PARAGRAPH_ALIGNMENT.CENTER
    doc.save('Document.docx')
    return "1"


def newPara():
    doc = docx.Document('Document.docx')
    doc.add_paragraph("")
    doc.save("Document.docx")
    return "2"


def addPara(text):
    doc = docx.Document('Document.docx')
    doc.add_paragraph(text)
    doc.save("Document.docx")
    return "3"


def fontSize():
    doc = docx.Document('Document.docx')
    font.size = Pt(12)
    doc.save("Document.docx")
    return "4"


def paraSpace():
    doc = docx.Document('Document.docx')
    doc.save("Document.docx")
    return "5"

def font(font):
    doc = docx.Document('Document.docx')
    font.name = "Times New Roman"
    doc.save("Document.docx")
    return "6"
