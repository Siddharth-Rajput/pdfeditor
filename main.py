import PyPDF2

pdfFileObj = open('edit2strip.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

print(pdfReader.numPages)
#variables modified
pageObj = pdfReader.getPage(0)
print(pageObj.extractText())

pdfFileObj.close()
