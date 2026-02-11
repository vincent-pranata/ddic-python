from flask_rebar import ResponseSchema, RequestSchema
from marshmallow import fields

class PreOrderSchema(ResponseSchema):
    class Meta:
        ordered = True
    preorder_id = fields.Integer()
    code = fields.String()
    name = fields.String()
    qty = fields.Integer()
    create_date = fields.String()
    status = fields.String()

class PreOrderCompleteSchema(RequestSchema):
    preorder_id = fields.Integer(required=True)

class PreOrderCreateSchema(RequestSchema):
    code = fields.String(required=True)
    client_id = fields.String(required=True)
    recipe_id = fields.String(required=True)
    qty = fields.String(required=True)
    create_date = fields.String(required=True)
    status = fields.String(required=True)

