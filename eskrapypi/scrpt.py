import requests  # Importamos la biblioteca Requests
from bs4 import BeautifulSoup  # Importamos la clase BeautifulSoup de la biblioteca Beautiful Soup

# Definimos la URL de la página que queremos raspar
url = 'https://www.example.com'

# Hacemos una solicitud HTTP para obtener el contenido HTML de la página
response = requests.get(url)

# Verificamos si la solicitud fue exitosa (código de estado 200)
if response.status_code == 200:
    html_content = response.text  # Guardamos el contenido HTML en una variable
    soup = BeautifulSoup(html_content, 'html.parser')  # Creamos un objeto BeautifulSoup

    # Encontramos todos los elementos <h2> que contienen los títulos de los artículos
    article_titles = soup.find_all('h2')

    # Imprimimos los títulos de los artículos
    for title in article_titles:
        print(title.text)
else:
    print('Error al obtener el contenido de la página.')
