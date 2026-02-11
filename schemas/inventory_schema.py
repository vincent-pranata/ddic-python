from flask_rebar import ResponseSchema, RequestSchema
from marshmallow import fields

class InventorySchema(ResponseSchema):
    class Meta:
        ordered = True
    
    inventory_id = fields.Integer()
    code = fields.String()
    client_id = fields.Integer()
    name = fields.String()
    qty = fields.Float()
    uom = fields.String()
    entry_date = fields.String()
    exp_date = fields.String()

class InventoryCreateSchema(RequestSchema):
    code = fields.String(required=True)
    name = fields.String(required=True) 
    qty = fields.Float(required=True)
    uom = fields.String(required=True)
    entry_date = fields.String(required=True)
    exp_date = fields.String(required=True)