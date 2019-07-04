from marshmallow import Schema, fields, validate, pre_load

class MemberSchema(Schema):
    member_id = fields.UUID()
    username = fields.Str(required=True)
    email = fields.Email(required=True, validate=validate.Email(error='Not a valid email address'),)
    first_name = fields.Str(required=True)
    last_name = fields.Str(required=True)
    password = fields.Str(required=True)
    created_at = fields.DateTime()
    updated_at = fields.DateTime()
    
class StoreSchema(Schema):
    store_id = fields.UUID()
    member_id = fields.UUID()
    member_name = fields.Str()
    name = fields.Str(required=True)
    slug = fields.Str(required=True)
    site = fields.Str(required=True)
    member = fields.Nested(MemberSchema, key='member_id', exclude=('password', 'member_id'))
    created_at = fields.DateTime()
    
    @pre_load
    def slugify_name(self, in_data, **kwargs):
        in_data['slug'] = in_data['slug'].lower().strip().replace(' ', '-')
        return in_data
    
class ProductSchema(Schema):
    product_id = fields.UUID() 
    store_id = fields.UUID()
    name = fields.Str(required=True)
    short_desc = fields.Str(required=True)
    long_desc = fields.Str(required=True)
    store = fields.Nested(StoreSchema, key='store_id')
    
