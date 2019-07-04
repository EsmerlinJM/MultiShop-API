from marshmallow import Schema, fields, pre_load, post_load, post_dump, validate
from app.shop.base_schema import BaseSchema
from app.models.member import Member

class MemberSchema(Schema):
    # __envelope__ = {
    #     'single': None,
    #     'many': None,
    # }
    # __model__ = Member
    
    member_id = fields.UUID()
    username = fields.Str(required=True)
    email = fields.Email(required=True, validate=validate.Email(error='Not a valid email address'),)
    first_name = fields.Str(required=True)
    last_name = fields.Str(required=True)
    password = fields.Str(required=True)
    created_at = fields.DateTime()
    updated_at = fields.DateTime()