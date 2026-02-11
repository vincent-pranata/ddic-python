from flask_rebar import ResponseSchema, RequestSchema
from marshmallow import fields

class BatchRecordSchema(ResponseSchema):
    class Meta:
        ordered = True
    id = fields.Integer()
    batch_id = fields.Integer()
    qty = fields.Float()
    division = fields.String()
    log_date = fields.DateTime()
    notes = fields.String()
    operator = fields.String()

class BatchRecordCreateSchema(RequestSchema):
    batch_id = fields.Integer(required=True)
    qty = fields.Float(required=True)
    division = fields.String(required=True)
    log_date = fields.DateTime(required=True)
    notes = fields.String()
    operator = fields.String(required=True)