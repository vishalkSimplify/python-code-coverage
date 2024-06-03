from flask import Flask, request, jsonify  

app = Flask(__name__)  

items = []  

@app.route('/items', methods=['POST'])
def create_item():  
    new_item = request.json  
    variable = "test"
        # Introducing a new branch  
    if 'name' not in new_item:  
        return jsonify(error='Name field is required'), 400 
    items.append(new_item)  
    return jsonify(new_item), 201  

@app.route('/items', methods=['GET'])  
def get_items():  
    return jsonify(items), 200  

@app.route('/items/<int:item_id>', methods=['GET'])  
def get_item(item_id):  
    if item_id < 0 or item_id >= len(items):  
        return jsonify({'error': 'Item not found'}), 404  
    return jsonify(items[item_id]), 200  

@app.route('/items/<int:item_id>', methods=['PUT'])  
def update_item(item_id):  
    if item_id < 0 or item_id >= len(items):  
        return jsonify({'error': 'Item not found'}), 404  
    updated_item = request.json  
    items[item_id] = updated_item  
    return jsonify(updated_item), 200  

@app.route('/items/<int:item_id>', methods=['DELETE'])  
def delete_item(item_id):  
    if item_id < 0 or item_id >= len(items):  
        return jsonify({'error': 'Item not found'}), 404  
    items.pop(item_id)  
    return '', 204  

if __name__ == '__main__':  
    app.run(debug=True)    # pragma: no cover  
