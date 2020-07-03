import docx
import os
from docx.shared import Inches, Cm
doc = docx.Document()
sections = doc.sections
for section in sections:
    section.top_margin = Cm(0.5)
    section.bottom_margin = Cm(0.5)
    section.left_margin = Cm(1)
    section.right_margin = Cm(1)

os.chdir("B:\pdf editor\Pictures\\5rot")
for i in range(1,115):
    doc.add_picture(str(i)+".jpg", width=docx.shared.Cm(19.6), height=docx.shared.Cm(13.8))
doc.save("B:\pdf editor\secondWords\\5final.docx")
