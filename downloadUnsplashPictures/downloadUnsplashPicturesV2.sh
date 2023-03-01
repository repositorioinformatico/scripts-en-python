import requests
from bs4 import BeautifulSoup
import os

# Especificamos la URL de Unsplash y el término de búsqueda
url = "https://unsplash.com/s/photos/penguins"
search_term = "penguins"

# Creamos una carpeta para guardar las imágenes
if not os.path.exists(search_term):
    os.makedirs(search_term)

# Realizamos la solicitud HTTP
response = requests.get(url)

# Parseamos el contenido HTML de la página usando Beautiful Soup
soup = BeautifulSoup(response.content, "html.parser")

# Encontramos todas las etiquetas <img> en la página
images = soup.find_all("img")

# Descargamos cada imagen en la carpeta que creamos
for i, image in enumerate(images):
    image_url = image["src"]
    response = requests.get(image_url)
    with open(os.path.join(search_term, f"{search_term}_{i}.jpg"), "wb") as f:
        f.write(response.content)
        print(f"Imagen {i+1} descargada")

