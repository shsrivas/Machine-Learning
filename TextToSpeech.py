
import PyPDF2
import pyttsx3

# path of the PDF file
p = open('whatyouthink.pdf.pdf', 'rb')

# creating a PdfFileReader object
reader = PyPDF2.PdfFileReader(p)

# reading the first page
start_page = reader.getPage(0)

# extracting the text from the PDF
text = start_page.extractText()

# reading the text
speak = pyttsx3.init()
speak.say(text)
speak.runAndWait()