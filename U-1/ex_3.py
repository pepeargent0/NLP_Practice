"""
Ejercicio 3 - Investigue cómo extraer información de vuelo en la página flybondi.com, haga un programa en python
para verificar si bajó el precio de un vuelo determinado
"""

def scrappear_sitio(driver, url):
    driver.get(url)
    driver.implicitly_wait(10)
    html_content = driver.page_source
    body = BeautifulSoup(html_content, 'lxml')
    div = body.find('div',
                    class_='jsx-3759278058 flex items-center justify-between pa3 ff--poppins b bt b--yellow bw1 br1 br--bottom')
    span = div.find('span', class_='jsx-2642904360')
    precio_1 = span.span.text.replace('.', '')
    precio_2 = span.find('sup', class_='jsx-2642904360 decimal-sup').text
    return float(precio_1 + '.' + precio_2)


from selenium import webdriver
from bs4 import BeautifulSoup
driver = webdriver.Chrome()
url = ('https://flybondi.com/ar/search/results?adults=1&children=0&currency=ARS&departureDate=2024-04-01&'
       'fromCityCode=BUE&infants=0&toCityCode=COR&utm_origin=search_bar')
precio_eleguido = scrappear_sitio(driver, url)
dia_elegido = 1
print('Fecha eleguida Precios')
print('Dia: ', dia_elegido)
print('Precio: ', precio_eleguido)
for dia in range(2, 31):
    if dia < 10:
        url = ('https://flybondi.com/ar/search/results?adults=1&children=0&currency=ARS&departureDate=2024-04-'+
               '0'+str(dia)+'&fromCityCode=BUE&infants=0&toCityCode=COR&utm_origin=search_bar')
    else:
        url = ('https://flybondi.com/ar/search/results?adults=1&children=0&currency=ARS&departureDate=2024-04-' +
                str(dia) + '&fromCityCode=BUE&infants=0&toCityCode=COR&utm_origin=search_bar')

    precio = scrappear_sitio(driver, url)
    if precio < precio_eleguido:
        dia_elegido = dia
        precio_eleguido = precio
print('Mejores Precios')
print('Dia : ', dia_elegido)
print('Tiene el mejor Precio: ', precio_eleguido)

driver.quit()
