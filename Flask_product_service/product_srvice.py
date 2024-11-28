from flask import Flask, request, jsonify
import json

app = Flask(__name__)

products = {}


@app.route('/', methods=['GET'])
def home_page():

    return '/add -> for adding a new product \n /login -> for login', 201


@app.route('/add', methods=['POST'])
def add_product():
    data = request.json
    product_id = data.get('id')
    product_name = data.get('name')

    if not product_id:
        return 'id required!', 400
    
    if product_id in products:
        return "Product id already exists", 400

    if not product_name:
        return 'product name is required!' , 400

    if product_name in products:
        return 'product already exists!', 400

    products[product_id] = product_name
    return jsonify({"message": "Product added successfully"}), 201


@app.route('/delete/<product_id>', methods=['DELETE'])
def delete_product(product_id):
    data = json.loads(request.data)
    if product_id in products:
        del products[product_id]
        return jsonify({"message": "Product deleted successfully"}), 200
    return jsonify({"message": "Product not found"}), 404


@app.route('/view', methods=['GET'])
def view_products():
    return jsonify(products), 200


app.run(port=5002,host='0.0.0.0')
