import pyttsx3
import PyPDF2
from tkinter.filedialog import *

book = askopenfilename()
pdf_reader = PyPDF2.PdfFileReader(book)
pages = pdf_reader.numPages


