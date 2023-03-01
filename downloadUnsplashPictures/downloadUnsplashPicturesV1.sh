import requests
from bs4 import BeautifulSoup
import os

# URL de la búsqueda de imágenes
url = 'https://unsplash.com/s/photos/penguins'

# Realizar una solicitud GET a la URL y obtener el contenido HTML de la página
response = requests.get(url)
html = response.content

# Analizar el HTML utilizando BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')

# Encontrar todas las etiquetas 'img' en el HTML
img_tags = soup.find_all('img')

# Crear un directorio para guardar las imágenes descargadas
if not os.path.exists('penguins'):
    os.makedirs('penguins')

# Iterar sobre todas las etiquetas 'img' encontradas y descargar las imágenes
for img_tag in img_tags:
    img_url = img_tag['src']
    if 'images.unsplash.com/photo' in img_url:
        response = requests.get(img_url)
        filename = img_url.split('/')[-1]
        with open(os.path.join('penguins', filename), 'wb') as f:
            f.write(response.content)
            print(f"Imagen descargada: {filename}")

