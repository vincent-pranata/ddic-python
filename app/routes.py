from flask import jsonify, request, redirect, session, url_for
import requests,os,json
from app import app, mainEngine

@app.route('/')
def index():
    data = mainEngine.getAllClients()
    return jsonify(data)

@app.route('/clients', methods = ['GET'])
def clients():
    data = mainEngine.getAllClients()
    return jsonify(data)

@app.route('/create_client', methods = ['POST'])
def create_clients():
    client_name = request.json['client_name']
    data = mainEngine.insertClient(client_name)
    return jsonify(data)
    
@app.route('/users', methods = ['GET'])
def users():
    data = mainEngine.getAllUsers()
    return jsonify(data)

@app.route('/create_user', methods = ['POST'])
def create_users():
    username = request.json['username']
    password = request.json['password']
    role = request.json['role']
    data = mainEngine.insertUser(username, password, role)
    return jsonify(data)
    
@app.route('/client/<client_id>/inventory', methods = ['GET'])
def client_inventory(client_id):
    data = mainEngine.getClientInventory(client_id)
    return jsonify(data)

@app.route('/client/<client_id>/create_inventory', methods = ['POST'])
def create_inventory(client_id):
    code = request.json['code']
    name = request.json['name']
    qty = request.json['qty']
    uom = request.json['uom']
    entry_date = request.json['entry_date']
    exp_date = request.json['exp_date']
    operator = request.json['operator']
    data = mainEngine.insertInventory(code, client_id, name, qty, uom, entry_date, exp_date, operator)
    return jsonify(data)

@app.route('/client/inventory/<inventory_id>/record', methods = ['GET'])
def inventory_record(inventory_id):
    data = mainEngine.getInventoryRecord(inventory_id)
    return jsonify(data)

@app.route('/client/<client_id>/recipe', methods = ['GET'])
def client_recipe(client_id):
    data = mainEngine.getClientRecipe(client_id)
    return jsonify(data)


@app.route('/client/<client_id>/create_recipe', methods = ['POST'])
def create_recipe(client_id):
    name = request.json['name']
    can = request.json['can']
    volume = request.json['volume']
    sterilisation = request.json['sterilisation']
    data = mainEngine.insertRecipe(client_id, name, can, volume, sterilisation)
    return jsonify(data)

# @app.route('/logout')
# def index():
#     data = {
#         'message': 'Hello from Python Backend!',
#         'timestamp': '2025-12-22T16:21:00Z', # Example dynamic data
#         'status': 'success'
#     }
#     return jsonify(data)

