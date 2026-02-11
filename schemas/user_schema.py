from flask_rebar import ResponseSchema, RequestSchema
from marshmallow import fields

class UserSchema(ResponseSchema):
    class Meta:
        ordered = True
    user_id = fields.Integer()
    username = fields.String()
    password = fields.String()
    role = fields.String()
    
class UserCreateSchema(RequestSchema):
    username = fields.String(required=True)
    password = fields.String(required=True)
    role = fields.String(required=True)