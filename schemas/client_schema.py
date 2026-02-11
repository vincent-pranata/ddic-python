from flask_rebar import ResponseSchema, RequestSchema
from marshmallow import fields

class ClientSchema(ResponseSchema):
    class Meta:
        ordered = True
    client_id = fields.Integer()
    name = fields.String()

class ClientCreateSchema(RequestSchema):
    name = fields.String(required=True)