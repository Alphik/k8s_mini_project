from flask import Flask, request, jsonify
import json

app = Flask(__name__)

orders = {}



@app.route('/create_order', methods=['POST'])
def create_order():
    data = request.json
    order_id = data.get('id')
    order_details = data.get('details')

    if not order_id:
        return 'order_id required!', 400

    if not order_details:
        return 'order_details is required!' , 400

    if order_id in orders:
        return 'Order already exists', 400

    orders[order_id] = order_details
    return jsonify({"message": "Order created successfully"}), 201


@app.route('/payment/<order_id>', methods=['POST'])
def payment(order_id):
    data = json.loads(request.data)

    if not order_id:
        return 'order_id required!', 400

    if order_id not in orders:
        return 'order_id not found', 400
    
    return jsonify("message": "Payment processed for order"), 200
 

@app.route('/track/<order_id>', methods=['GET'])
def track_order(order_id):
    if not order_id:
        return 'order_id required!', 400

    if order_id in orders:
        return jsonify({"order_id": order_id, "details": orders[order_id]}), 200
    
    return "Order not found", 404

    app.run(host='0.0.0.0', port=5003)
