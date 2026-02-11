from unittest import result
import json
from flask import Flask
from flask_rebar import Rebar

# Import Schemas
from schemas.user_schema import *
from schemas.client_schema import *
from schemas.recipe_schema import *
from schemas.inventory_record_schema import *
from schemas.inventory_schema import *
from schemas.pre_order_schema import *

# Import Services
from services.user_service import *
from services.client_service import *
from services.recipe_service import *
from services.inventory_record_service import *
from services.inventory_service import *
from services.pre_order_service import *

rebar = Rebar()
registry = rebar.create_handler_registry(prefix='/v1')

def create_tables():
    create_client_table()
    create_user_table()
    create_inventory_table()
    create_inventory_record_table()
    create_recipe_table()
    create_preorder_table()

# Client Endpoints
@registry.handles(
    rule='/clients', 
    method='GET', 
    response_body_schema=ClientSchema(many=True)
)
def list_clients():
    clients = get_all_clients()
    return clients

@registry.handles(
    rule='/create_client', 
    method='POST', 
    request_body_schema=ClientCreateSchema(),
    response_body_schema=ClientSchema()
)
def create_client():
    body = rebar.validated_body
    result = insert_client(body['name'])
    if result.get("error"):
        return 500
    
    return  201

# Inventory Endpoints
@registry.handles(
    rule='/client/<client_id>/inventory', 
    method='GET', 
    response_body_schema=InventorySchema(many=True)
)
def list_client_inventory(client_id):
    return get_client_inventory(client_id)

@registry.handles(
    rule='/client/<client_id>/create_inventory/<operator>', 
    method='POST', 
    request_body_schema=InventoryCreateSchema(),
    response_body_schema=InventorySchema()
)
def create_inventory(client_id, operator):
    body = rebar.validated_body
    result = insert_inventory(body['code'], client_id, body['name'], body['qty'], body['uom'], body['entry_date'], body['exp_date'])

    if result.get("error"):
        return 500
    record_result = insert_inventory_record(result['inventory_id'], body['qty'], body['entry_date'], "Barang masuk", operator)
    if record_result.get("error"):
        return 500
    return 201

# Inventory Record Endpoints
@registry.handles(
    rule='/client/inventory/<inventory_id>/record', 
    method='GET', 
    response_body_schema=InventoryRecordSchema(many=True)
)
def list_inventory_records(inventory_id):
    return get_inventory_record(inventory_id)

@registry.handles(
    rule='/client/inventory/<inventory_id>/create_record',
    method='POST', 
    request_body_schema=InventoryRecordCreateSchema(),
    response_body_schema=InventoryRecordSchema()
)
def create_inventory_record(inventory_id):
    body = rebar.validated_body
    result = insert_inventory_record(inventory_id, body['qty'], body['log_date'], body['notes'], body['operator'])
    if result.get("error"):
        return 500
    old_qty = get_inventory_qty(inventory_id)
    new_qty = old_qty['qty'] + body['qty']
    update_inventory = update_inventory_qty(inventory_id, new_qty)
    if update_inventory.get("error"):
        return 500
    return  201

# Recipe Endpoints
@registry.handles(
    rule='/client/<client_id>/recipe', 
    method='GET', 
    response_body_schema=RecipeSchema(many=True)
)
def list_client_recipes(client_id):
    return get_client_recipes(client_id)

@registry.handles(
    rule='/client/<client_id>/recipe-details', 
    method='GET', 
    response_body_schema=RecipeDetailsSchema(many=True)
)
def list_client_recipes_details(client_id):
    results = get_client_recipes_details(client_id)
    return results

@registry.handles(
    rule='/client/<client_id>/create_recipe', 
    method='POST', 
    request_body_schema=RecipeCreateSchema(),
    response_body_schema=RecipeSchema()
)
def create_recipe(client_id):
    body = rebar.validated_body
    result = insert_recipe(client_id, body['name'], body['can_type'], body['volume'], body['sterilisation'])
    if result.get("error"):
        return 500    
    return  201

@registry.handles(
    rule='/recipe/<recipe_id>/get_materials', 
    method='GET', 
    response_body_schema=RecipeMaterialsSchema(many=False)
)
def get_materials(recipe_id):
    result = get_recipe_materials(recipe_id)
    ret_val = json.loads(result['materials'])
    return {
        'materials': ret_val
    }

@registry.handles(
    rule='/recipe/update_materials', 
    method='POST', 
    request_body_schema=RecipeUpdateMaterialsSchema(),
    response_body_schema=RecipeSchema()
)
def edit_materials():
    body = rebar.validated_body
    json_data = json.dumps(body['materials'])
    result = update_materials(body['recipe_id'], json_data)
    if result.get("error"):
        return 500    
    return  201

@registry.handles(
    rule='/recipe/<recipe_id>/get_parameters', 
    method='GET', 
    response_body_schema=RecipeParametersSchema(many=False)
)
def get_parameters(recipe_id):
    result = get_recipe_parameters(recipe_id)
    ret_val = json.loads(result['parameters'])
    return {
        'parameters': ret_val
    }

@registry.handles(
    rule='/recipe/update_parameters', 
    method='POST', 
    request_body_schema=RecipeUpdateParametersSchema(),
    response_body_schema=RecipeSchema()
)
def edit_parameters():
    body = rebar.validated_body
    json_data = json.dumps(body['parameters'])
    result = update_parameters(body['recipe_id'], json_data)
    if result.get("error"):
        return 500    
    return  201

# Pre-Order Endpoints
@registry.handles(
    rule='/client/<client_id>/pre-orders', 
    method='GET', 
    response_body_schema=PreOrderSchema(many=True)
)
def list_preorders(client_id):
    results = get_client_preorders(client_id)
    return results

@registry.handles(
    rule='/client/create-pre-order', 
    method='POST', 
    request_body_schema=PreOrderCreateSchema(),
    response_body_schema=PreOrderSchema()
)
def create_preorder():
    body = rebar.validated_body
    result = insert_preorder(body['code'], body['client_id'], body['recipe_id'], body['qty'], body['create_date'], body['status'])
    if result.get("error"):
        return 500
    
    return  201

# User Endpoints
@registry.handles(
    rule='/users', 
    method='GET', 
    response_body_schema=UserSchema(many=True)
)
def list_users():
    return get_all_users()

@registry.handles(
    rule='/create_user', 
    method='POST', 
    request_body_schema=UserCreateSchema(),
    response_body_schema=UserSchema()
)
def create_user():
    body = rebar.validated_body
    result = insert_user(body['username'], body['password'], body['role'])
    if result.get("error"):
        return 500
    
    return  201

app = Flask(__name__)
app.json.sort_keys = False 
rebar.init_app(app)

if __name__ == '__main__':
    create_tables()
    app.run(debug=True)