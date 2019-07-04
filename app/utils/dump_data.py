from marshmallow import Schema
from datetime import datetime
import uuid

class DumpData(Schema):
    def __init__(self, schema=Schema):
        self.id = uuid.uuid1()
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        self.schema = schema
        
    def dump(self, data, isMany = False, fields_exclude=[]):
        return self.schema(exclude=fields_exclude).dump(data, many=isMany).data
    
    def prepare_data(self, response, field=None, id=None):
        raw_data = response.data
        if id is not None:
            raw_data[field] = id
            raw_data['updated_at'] = self.updated_at
        else:
            raw_data[field] = self.id
            raw_data['created_at'] = self.created_at
        return raw_data
        
        