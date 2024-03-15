"""
Ejercicio 2 - El Ministerio de Turismo y Deportes de la Nación permite explorar tableros de información en
línea tableros.yvera.tur.ar. Explore la página y utilizando una librería de web scraping extraiga los valores del
tablero de indicadores de Objetivos de Desarrollo Sostenible en una tabla y el texto limpio de la metodología de
los mismos
"""
import requests
from bs4 import BeautifulSoup

site_index = requests.get('https://tableros.yvera.tur.ar', verify=False)

if site_index.status_code == 200:
    html_parse = BeautifulSoup(site_index.text, 'lxml')
    div_contenedor = html_parse.find_all('div', class_='card bg-transparent m-0 border-0 collapse.show bs4cards-blahblahblah bs4cards-Todos bs4cards-Tablero')
    for div in div_contenedor:
        if 'Objetivos de Desarrollo Sostenible' in div.text:
            link_tablero = div.find('a')['href']
            break
print(link_tablero)
tablero = requests.get(link_tablero, verify=False)
if tablero.status_code == 200:
    tablero_parse = BeautifulSoup(tablero.text, 'lxml')
    div = tablero_parse.find( id='shiny-tab-summary')
    print(div.b.text)
    _p = div.find_all('p')
    for p in _p:
        if len(p.text) > 1:
            print(p.text)


