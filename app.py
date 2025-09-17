from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/")
def inicio():
    return "Bienvenidos al Sistema de Productos"

@app.route("/acerca")
def acerca():
    return jsonify({
        "aplicacion": "Gestion de Productos",
        "version": 1.0,
        "autor": "Gustavo Ramiro Copajira"
    })


productos = [
    {"id": 1, "nombre": "Laptop", "precio": 5500},
    {"id": 2, "nombre": "Mouse", "precio": 150},
    {"id": 3, "nombre": "Teclado", "precio": 250}
]

#GET - devuelve todos los productos en formato json
@app.route("/productos",methods=['GET'])
def listar_productos():
    return jsonify(productos)

#GET - obtener un producto especifico
@app.route("/productos/<int:id>", methods=['GET'])
def obtener_producto(id):
    producto = None
    for p in productos:
        if p['id'] == id:
            producto = p
            break
    if producto:
        return jsonify(producto)
    return jsonify({'error':'Producto no Encontrado'}),404

#POST - Insertar un Nuevo Producto
@app.route("/productos",methods=['POST'])
def crear_producto():
    nuevo_producto={
        'id':len(productos)+1,
        'nombre':request.json.get('nombre'),
        'precio':request.json.get('precio')
    }
    productos.append(nuevo_producto)
    return jsonify({'mensaje':'Producto agregado Correctamente!!!'}), 201

#DELETE - Eliminar un producto
@app.route("/productos/<int:id>",methods=['DELETE'])
def eliminar_producto(id):
    global productos
    producto = next((p for p in productos if p["id"] == id), None)
    if producto is None:
        return jsonify({'error':'Producto no Encontrado'})
    productos = [ p for p in productos if p['id'] != id ]
    return jsonify({'mensaje':'Producto eliminado Correctamente !!!'}), 200


if __name__ == "__main__":
    app.run(debug=True)
