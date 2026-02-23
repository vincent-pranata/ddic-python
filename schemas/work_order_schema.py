from flask_rebar import ResponseSchema, RequestSchema
from marshmallow import fields

class WorkOrderSchema(ResponseSchema):
    class Meta:
        ordered = True
    workorder_id = fields.Integer()
    workorder_code = fields.String()
    preorder_code = fields.String()
    name = fields.String()
    cartoning = fields.Integer()
    start_date = fields.String()
    end_date = fields.String(required=False, allow_none=True)
    ship_date = fields.String(required=False, allow_none=True)
    operator = fields.String()

class WorkOrderCreateSchema(RequestSchema):
    preorder_id = fields.String(required=True)
    client_id = fields.String(required=True)
    code = fields.String(required=True)
    cartoning = fields.String(required=True)
    start_date = fields.String(required=True)
    operator = fields.String(required=True)
