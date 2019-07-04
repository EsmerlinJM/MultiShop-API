import datetime as dt
import uuid

class Member(object):
    def __init__(self, username, email, created_at):
        self.member_id = uuid.uuid1()
        self.username = username
        self.email = email
        self.created_at = dt.datetime.now()