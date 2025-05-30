"""
This module defines various event classes that represent different types of events"""

class Event():
    id = int
    type = str
    actor = str
    payload = dict
    ref = str

    def __init__(self, id:int,type:str,actor:str,payload:dict,ref: str=None):
        self.id = id
        self.type = type
        self.actor = actor
        self.payload = payload
        self.ref = ref

class CreateEvent(Event):
    ref_type = str
    master_branch = str

    def __init__(self, id, type, actor, payload, ref = None):
        super().__init__(id, type, actor, payload, ref)
        self.ref_type = payload['ref_type']
        self.master_branch = payload['master_branch']
        
    def type_output(self):
        print(f'User created a {self.ref_type} with master branch {self.master_branch}.')

class DeleteEvent(Event):
    ref_type = str
    
    def __init__(self, id, type, actor, payload, ref = None):
        super().__init__(id, type, actor, payload, ref)
        self.ref_type = payload['ref_type']

    def type_output(self):
        print(f'User delete a {self.ref_type}')

class ForkEvent(Event):
    forkee = str

    def __init__(self, id, type, actor, payload, ref = None):
        super().__init__(id, type, actor, payload, ref)
        self.forkee = payload['forkee']['full_name']

    def type_output(self):
        print(f'User forked the repository: {self.forkee}')

class IssueCommentEvent(Event):
    comment_action = str
    issue = str

    def __init__(self, id, type, actor, payload, ref = None):
        super().__init__(id, type, actor, payload, ref)
        self.comment_action = payload['action']
        self.issue = payload['issue']['title']
    
    def type_output(self):
        print(f'User {self.comment_action} a comment on issue: {self.issue}')

class IssuesEvent(Event):
    action = str
    issue = str

    def __init__(self, id, type, actor, payload, ref = None):
        super().__init__(id, type, actor, payload, ref)
        self.action = payload['action']
        self.issue = payload['issue']['title']
    
    def type_output(self):
        print(f'User {self.action} an issue: {self.issue}')

class MemberEvent(Event):
    member_action = str
    member = str


    def __init__(self, id, type, actor, payload, ref = None):
        super().__init__(id, type, actor, payload, ref)
        self.member_action = payload['action']
        self.member = payload['member']['login']

    def type_output(self):
        if self.member_action == 'added':
            print(f'User added {self.member} as a member.')
        elif self.member_action == 'removed':
            print(f'User removed {self.member} from the members list.')

class PullRequestEvent(Event):
    action = str
    pull_request = str

    def __init__(self, id, type, actor, payload, ref = None):
        super().__init__(id, type, actor, payload, ref)
        self.action = payload['action']
        self.pull_request = payload['pull_request']['title']
    
    def type_output(self):
        print(f'User {self.action} a pull request: {self.pull_request}')

class PushEvent(Event):
    size = int

    def __init__(self, id, type, actor, payload,ref):
        super().__init__(id, type, actor, payload,ref)
        self.size = self.payload['size']

    def type_output(self):
        if self.size == 1:
            change = "change"
        else:
            change = "changes"
        print(f'User committed {self.size} {change} to {self.ref}')
    
class PullRequestReviewCommentEvent(Event):
    action = str
    repo = str

    def __init__(self, id, type, actor, payload, ref = None):
        super().__init__(id, type, actor, payload, ref)
        self.action = payload['action']
        self.repo = payload['repo']['name']
    
    def type_output(self):
        print(f'User {self.action} a review comment on the repository: {self.repo}')

class WatchEvent(Event):
    repo = str

    def __init__(self, id, type, actor, repo, ref = None):
        super().__init__(id, type, actor, repo, ref)
        self.repo = repo['name']

    def type_output(self):
        print(f'User starred {self.repo}')

