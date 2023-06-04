import requests

# Realizar una solicitud GET a una API pública
response = requests.get('https://jsonplaceholder.typicode.com/posts')

# Mostrar los resultados
print(response.json())

# Intentar hacer una solicitud POST a la misma API
response = requests.post('https://jsonplaceholder.typicode.com/posts', json={'title': 'Título', 'body': 'Contenido'})

# Observar el resultado
print(response.json())
