from flask import Flask, jsonify, request

app = Flask(__name__)

# Datos de ejemplo
posts = []

# Ruta para obtener todas las publicaciones (método GET)
@app.route('/posts', methods=['GET'])
def get_posts():
    return jsonify(posts)

# Ruta para agregar una nueva publicación (método POST)
@app.route('/posts', methods=['POST'])
def add_post():
    new_post = request.get_json()
    posts.append(new_post)
    return jsonify(new_post), 201

# Ejecutar la aplicación
if __name__ == '__main__':
    app.run()
