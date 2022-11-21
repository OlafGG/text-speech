import pyttsx3
import pikepdf
from PyPDF2 import PdfFileReader
from gtts import gTTS

def decr(path): 
    """Traemos el archivo PDF"""
    with pikepdf.open(path) as pdf: 
        pdf.save(f"decrypted_{path}")

    print("Decryption complete!")

#decr('pruebapdf1.pdf')

def pdfToTxt(path):
    """Tomamos el archivo pdf para crear el texto"""
    pdf = PdfFileReader(path)
    num_pages = pdf.getNumPages() #Lo partimos en paginas
    text = ""

    for i in range(num_pages):
        txt = pdf.getPage(i).extractText() #tomamos el texto de la paginas
        text += txt
    return text #Devolvemos el texto

path =  "pdf/pruebapdf1.pdf" #Variable para llamar al pdf
#print(pdfToTxt(path))

def txtToAud(txt):
    """Mostrar como suena el audio"""
    engine = pyttsx3.init()
    engine.setProperty('rate', 135)
    engine.say(txt)

    engine.runAndWait()



txt = pdfToTxt(path)
#txtToAud(txt)

def saveAudio(txt):
    """Se guarda el audio"""

    tts = gTTS(text=txt, lang='es')
    tts.save("audio/audio.mp3")
    print('Audio guardado!')

saveAudio(txt)
