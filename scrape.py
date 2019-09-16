import PyPDF2
from tabula import wrapper
import pandas as pd

def getUsefulPages(pageToDelete, infile):
  out = PyPDF2.PdfFileWriter()
  for i in range(infile.getNumPages()):
    if i not in pageToDelete:
      p = infile.getPage(i)
      out.addPage(p)
  with open('clean.pdf', 'wb') as f:
    out.write(f)

def getCleanPdf():
  filename = input("Enter the filename of the pdf")
  pdfFileObj = open(filename, 'rb')
  pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
  print(f'There are {pdfReader.numPages} pages')
  dels = input("Which first few pages are useless?")
  pageToDelete = range(0, dels)
  getUsefulPages(pageToDelete, pdfReader)
  pass

def main():
  getCleanPdf()
  # By now, the clean pdf is clean.pdf
  df = wrapper.read_pdf("clean.pdf")
  writer = pd.ExcelWriter('out.xlsx', engine='xlsxwriter')
  df.to_excel(writer, sheet_name='Sheet1')
  writer.save()

if __name__ == "__main__":
  main()
