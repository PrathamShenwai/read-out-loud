import pyttsx3
import PyPDF2
book = open('story.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages
print(pages)
speaker = pyttsx3.init()
speaker.setProperty("rate", 130)
for num in range(5, pages):
    page = pdfReader.getPage(5)
    text = page.extractText()
    speaker.say(text)
    speaker.runAndWait()

