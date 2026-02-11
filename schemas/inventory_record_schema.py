from flask_rebar import ResponseSchema, RequestSchema
from marshmallow import fields

class InventoryRecordSchema(ResponseSchema):
    class Meta:
        ordered = True
    id = fields.Integer()
    inventory_id = fields.Integer()
    qty = fields.Float()
    log_date = fields.String()
    notes = fields.String()
    operator = fields.String()

class InventoryRecordCreateSchema(RequestSchema):
    inventory_id = fields.Integer(required=True)
    qty = fields.Float(required=True)
    log_date = fields.String(required=True)
    notes = fields.String(required=True)
    operator = fields.String(required=True)