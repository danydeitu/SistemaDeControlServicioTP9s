import json

# Crear un objeto Python
data = {
    'name': 'Daniel',
    'age': 38,
    'city': 'Buenos Aires'
}

# Convertir a una cadena JSON
json_data = json.dumps(data)

# Mostrar la cadena JSON
print(json_data)

# Convertir la cadena JSON a un objeto Python
parsed_data = json.loads(json_data)

# Mostrar los datos convertidos
print(parsed_data)
