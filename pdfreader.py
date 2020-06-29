import PyPDF2
import json
pdfFile = open('MCQ.pdf', 'rb')

pdfReader = PyPDF2.PdfFileReader(pdfFile)

print(pdfReader.numPages)
for i in range(226):
    pageObj = pdfReader.getPage(i)
    data=pageObj.extractText()
    data={}
    data={
     "Question":pageObj.extractText(),
     "Answer":pageObj.extractText(),
    }
    print(json.dumps(data))

pdfFile.close()
