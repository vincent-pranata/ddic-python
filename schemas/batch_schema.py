from flask_rebar import ResponseSchema, RequestSchema
from marshmallow import fields

class BatchSchema(ResponseSchema):
    class Meta:
        ordered = True
    batch_id = fields.Integer()
    recipe_id = fields.Integer()
    work_order_id = fields.Integer()
    qty = fields.Float()
    target_date = fields.DateTime()

class BatchCreateSchema(RequestSchema):
    recipe_id = fields.Integer(required=True)
    work_order_id = fields.Integer(required=True)
    qty = fields.Float(required=True)
    target_date = fields.DateTime(required=True)