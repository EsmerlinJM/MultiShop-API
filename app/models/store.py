import datetime as dt
import uuid

class Store(object):
    def __init__(self, name, member):
        self.store_id = uuid.uuid1()
        self.name = name
        self.member = member
        self.created_at = dt.datetime.now()
        
        