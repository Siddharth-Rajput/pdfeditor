from PyPDF2 import PdfFileReader, PdfFileWriter

input_dir = "5.pdf"
output_dir = "5rot.pdf"

pdf_in = open(input_dir, 'rb')
pdf_reader = PdfFileReader(pdf_in)
pdf_writer = PdfFileWriter()
for pagenum in range(pdf_reader.numPages):
    page = pdf_reader.getPage(pagenum)
    page.rotateClockwise(90)
    pdf_writer.addPage(page)
pdf_out = open(output_dir, 'wb')
pdf_writer.write(pdf_out)
pdf_out.close()
pdf_in.close()
