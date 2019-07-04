from ...repository import Repository
from ...repository.mongo import MongoRepository
from app.shop.schemas.store_schema import StoreSchema
import uuid
from datetime import datetime
from app.utils.dump_data import DumpData

class StoreService(object):
    def __init__(self, repo_client=Repository(adapter=MongoRepository)):
        self.repo_client = repo_client
        self.store_id = uuid.uuid1()
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        self.dump_store = DumpData(schema=StoreSchema)
        
    def find_all_stores(self):
        stores = self.repo_client.find_all({})
        return self.dump_store.dump(stores, isMany=True, fields_exclude=['member.password'])
        
    def create_store(self, store):
        self.repo_client.create(self.dump_store.prepare_data(store, field='store_id'))
        return self.dump_store.dump(store.data, fields_exclude=['member.password'])
    
    def dump(self, data):
        return StoreSchema(exclude=['_id']).dump(data).data
        
    def prepare_store(self, store):
        data = store.data
        data['store_id'] = self.store_id
        data['created_at'] = self.created_at
        return data
        
    