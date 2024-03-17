"""
Realizar en Colab un script Python que haga los siguientes pasos:
i. Obtener el HTML de la página https://es.wikipedia.org/wiki/Argentina
ii. Con BeautifulSoup, Obtener el texto contenido en el
iii. Aplicar RecursiveCharacterTextSplitter con los parámetros el texto de wikipedia.
iv. Aplicar RecursiveCharacterTextSplitter con los parámetros en el texto de wikipedia.
v. Aplicar CharacterTextSplitter() en el texto de wikipedia.
cuyo
vi. En cada caso, graficar el histograma de como se distribuyen los tamaños de los segmentos
(chunks) y sacar conclusiones.
"""

import requests
from bs4 import BeautifulSoup
from langchain.text_splitter import RecursiveCharacterTextSplitter, CharacterTextSplitter
import matplotlib.pyplot as plt

url = 'https://es.wikipedia.org/wiki/Argentina'
response = requests.get(url, verify=False)
text = ''
if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'lxml')
    div_text = soup.find('div', id="mw-content-text")
    text = div_text.text

print('Recursivo Text Split chunk size 300')
text_splitter = RecursiveCharacterTextSplitter(chunk_size=300)
texts = text_splitter.split_text(text)
sizes = [len(segment) for segment in texts]

plt.figure(figsize=(10, 6))
plt.hist(sizes, bins=30, color='green', edgecolor='black')
plt.title('Distribución de tamaños de segmentos de texto (RecursivoTextSplit chunk size 300 )')
plt.xlabel('Tamaño del segmento')
plt.ylabel('Frecuencia')
plt.grid(True)
plt.show()


print('RecursivoTextSplit chunk size 300 con sepradores')
text_splitter = RecursiveCharacterTextSplitter(chunk_size=300, separators=['\n\n', '\n'])
texts = text_splitter.split_text(text)
sizes = [len(segment) for segment in texts]

plt.figure(figsize=(10, 6))
plt.hist(sizes, bins=30, color='blue', edgecolor='black')
plt.title('Distribución de tamaños de segmentos de texto (RecursivoTextSplit chunk size 300 con sepradores)')
plt.xlabel('Tamaño del segmento')
plt.ylabel('Frecuencia')
plt.grid(True)
plt.show()

print('CharacterTextSplitter')
text_splitter = CharacterTextSplitter(separator=".\n", chunk_size=300)
splitted_text = text_splitter.split_text(text)
sizes = [len(segment) for segment in splitted_text]

plt.figure(figsize=(10, 6))
plt.hist(sizes, bins=30, color='green', edgecolor='black')
plt.title('Distribución de tamaños de segmentos de texto (CharacterTextSplitter)')
plt.xlabel('Tamaño del segmento')
plt.ylabel('Frecuencia')
plt.grid(True)
plt.show()