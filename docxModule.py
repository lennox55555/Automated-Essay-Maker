import docx
from docx import Document
from docx.shared import Pt
import os
from docx.enum.style import WD_STYLE_TYPE
from docx.enum.text import WD_PARAGRAPH_ALIGNMENT



def title(title):
    doc = docx.Document('Document.docx')
    paragraph1 = doc.add_paragraph()
    style1 = doc.styles['Normal']
    font1 = style1.font
    font1.name = 'Times New Roman'
    font1.size = Pt(28)
    paragraph1.style = doc.styles['Normal']
    doc.add_paragraph(title)
    doc.save('Document.docx')
    return "1"

def newPara():
    doc = docx.Document('Document.docx')
    doc.add_paragraph(" \n ")
    doc.save("Document.docx")
    return "2"


def addPara(text, font1, fontSize):
    document = Document('Document.docx')
    paragraph = document.add_paragraph()
    style = document.styles['Normal']
    font = style.font
    font.name = font1
    font.size = Pt(fontSize)
    paragraph.style = document.styles['Normal']
    document.add_paragraph(text)
    document.save('Document.docx')
    return "1"


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
