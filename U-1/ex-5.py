"""
Ejercicio 5 - Obtener los libros en formato pdf de la página del autor argentino
Hernán Casciari de la editorial Orsai,
estos textos son de libre utilización. Pasar a un archivo pkl el texto de los libros en pdf.
"""

import PyPDF2
import gdown
import pickle


def download_pdf(_id, ruta):
    url = f'https://drive.google.com/uc?id={_id}'
    ruta_destino = ruta
    gdown.download(url, ruta_destino, quiet=False)


def get_text(ruta):
    with open(ruta, 'rb') as archivo:
        lector = PyPDF2.PdfReader(archivo)
        texto = ''
        for i in range(len(lector.pages)):
            pagina = lector.pages[i]
            texto += pagina.extract_text()
    return texto


def create_pkl(filename, text):
    with open(filename, "wb") as archivo:
        pickle.dump(text, archivo)


download_pdf('12YTjoI7XgHER5bTGHXoNuyJkjq6KkFRl', 'libro.pdf')
texto_pdf = get_text('libro.pdf')
create_pkl('texto_pdf.pkl', texto_pdf)
