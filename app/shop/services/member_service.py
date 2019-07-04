from ...repository import Repository
from ...repository.mongo import MongoRepository
from app.shop.schemas.member_schema import MemberSchema
import uuid
from datetime import datetime
from app.utils.dump_data import DumpData

class MemberService(object):
    def __init__(self, repo_client=Repository(adapter=MongoRepository)):
        self.repo_client = repo_client
        self.dump_member = DumpData(schema=MemberSchema)
        
    def find_all_members(self):
        members = self.repo_client.find_all({})
        return {'members': self.dump_member.dump(members, isMany=True, fields_exclude=['password'])}
    
    def find_member(self, member_id):
        member = self.repo_client.find({'member_id': member_id})
        return self.dump_member.dump(member, fields_exclude=['password']).data
    
    def create_member_for(self, member):
        self.repo_client.create(self.dump_member.prepare_data(member))
        return self.dump_member.dump(member.data, fields_exclude=['password']).data
    
    def update_member_with(self, member_id, member):
        self.repo_client.update({'member_id': member_id}, self.dump_member.prepare_data(member, field='member_id', id=member_id))
        return self.dump_member.dump(member.data, fields_exclude=['password']).data
    
    def delete_member_for(self, member_id):
        records_affected = self.repo_client.delete({'member_id': member_id})
        return records_affected > 0
    