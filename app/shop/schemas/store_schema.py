from marshmallow import Schema, fields, pre_load, validate
from app.shop.base_schema import BaseSchema
from .member_schema import MemberSchema
from app.models.store import Store

class StoreSchema(BaseSchema):
    __envelope__ = {
        'single': 'store',
        'many': 'stores',
    }
    # __model__ = Store
    
    store_id = fields.UUID()
    member_id = fields.UUID()
    member_name = fields.Str()
    name = fields.Str(required=True)
    slug = fields.Str(required=True)
    site = fields.Str(required=True)
    member = fields.Nested(MemberSchema, key='member_id', load_from='member', validate=validate.Length(min=1, error='Field may not be an empty list'),required=True)
    created_at = fields.DateTime()
    updated_at = fields.DateTime()
    
    @pre_load
    def slugify_name(self, in_data, **kwargs):
        in_data['slug'] = in_data['slug'].lower().strip().replace(' ', '-')
        return in_data