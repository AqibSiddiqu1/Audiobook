import pyttsx3 
import PyPDF2

book= open('book.pdf','rb')

pdfreader=PyPDF2.PdfReader(book)

pages=len(pdfreader.pages)

for num in range(5,pages):

    page=pdfreader.pages[num]

    text=page.extract_text()

    speaker = pyttsx3.init()

    speaker.say(text)

    speaker.runAndWait() 



