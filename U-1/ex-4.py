"""
Ejercicio 4 - Con el objetivo de estudiar la serie de tipo de cambio oficial y su volatilidad de forma visual.
Utilice una librería de web scraping y elija una dirección que posea esta información en una frecuencia diaria y
recolecte esa información (por ejemplo dolarhoy.com). Documente el proceso debidamente.
Opcional: Una vez obtenidos los datos requeridos realice una gráfica que muestre la serie y calcule los valores
promedio mensual de la serie. Su máximo valor y su mínimo. Presente los datos por pantalla en forma ordenada.
"""
import json
import matplotlib.pyplot as plt
import requests

url = 'https://mercados.ambito.com//dolar/informal/historico-general/2024-02-01/2024-03-01'
datos = requests.get(url)
data_list = json.loads(datos.text)

# Crear un diccionario con los datos
data_dict = {"Fecha": [], "Compra": [], "Venta": []}
for row in data_list[1:]:
    data_dict["Fecha"].append(row[0])
    data_dict["Venta"].append(float(row[2].replace(',', '.')))
plt.figure(figsize=(10, 6))
plt.hist(data_dict["Venta"], bins=10, alpha=0.5, label='Venta')
plt.title('Histograma de Venta')
plt.xlabel('Precio')
plt.ylabel('Frecuencia')
plt.legend(loc='upper right')
plt.grid(True)
plt.show()