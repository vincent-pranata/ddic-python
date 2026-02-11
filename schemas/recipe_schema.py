from flask_rebar import ResponseSchema, RequestSchema
from marshmallow import fields

class RecipeSchema(ResponseSchema):
    class Meta:
        ordered = True
    recipe_id = fields.Integer()
    client_id = fields.Integer()
    name = fields.String()
    can_type = fields.String()
    volume = fields.Float()
    sterilisation = fields.String()
    parameters = fields.Dict()
    materials = fields.Dict()

class RecipeDetailsSchema(ResponseSchema):
    class Meta:
        ordered = True
    recipe_id = fields.Integer()
    name = fields.String()

class RecipeParametersSchema(ResponseSchema):
    parameters = fields.Dict()

class RecipeMaterialsSchema(ResponseSchema):
    materials = fields.Dict()

class RecipeUpdateParametersSchema(RequestSchema):
    recipe_id = fields.Integer(required=True)
    parameters = fields.Dict(required=True)

class RecipeUpdateMaterialsSchema(RequestSchema):
    recipe_id = fields.Integer(required=True)
    materials = fields.Dict(required=True)

class RecipeCreateSchema(RequestSchema):
    name = fields.String(required=True)
    can_type = fields.String(required=True)
    volume = fields.Float(required=True)
    sterilisation = fields.String(required=True)
    parameters = fields.Dict(required=False)
    materials = fields.Dict(required=False)
