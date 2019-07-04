import os
from pymongo import MongoClient

COLLECTION_NAME = 'shop'

class MongoRepository(object):
    def __init__(self):
        mongo_url = 'mongodb://mongo_user:mongo_secret@0.0.0.0:27017/'
        self.db = MongoClient(mongo_url).shop

    def find_all(self, selector):
        return self.db.shop.find(selector)

    def find(self, selector):
        return self.db.shop.find_one(selector)

    def create(self, shop):
        return self.db.shop.insert_one(shop)

    def update(self, selector, shop):
        return self.db.shop.replace_one(selector, shop).modified_count

    def delete(self, selector):
        return self.db.shop.delete_one(selector).deleted_count
