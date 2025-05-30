import events as Evt

"""
This module contains the function get_user_activity which processes GitHub user activity data."""

def get_user_activity(api_data):
    for i in api_data:
        event_id = i['id']
        event_type = i['type']
        event_actor = i['actor']
        event_payload = i['payload']
        
        if event_type == "PushEvent":
            event_ref = event_payload['ref']
            github_event = Evt.PushEvent(event_id, event_type, event_actor, event_payload,event_ref)
            github_event.type_output()
        
        if event_type == "IssueCommentEvent":
            github_event = Evt.IssueCommentEvent(event_id, event_type, event_actor, event_payload)
            github_event.type_output()
        
        if event_type == "IssuesEvent":
            github_event = Evt.IssuesEvent(event_id, event_type, event_actor, event_payload)
            github_event.type_output()
        
        if event_type == "MemberEvent":
            github_event = Evt.MemberEvent(event_id, event_type, event_actor, event_payload)
            github_event.type_output()
        
        if event_type == "PullRequestEvent":
            github_event = Evt.PullRequestEvent(event_id, event_type, event_actor, event_payload)
            github_event.type_output()
        
        if event_type == "WatchEvent":
            github_event = Evt.WatchEvent(event_id, event_type, event_actor, i['repo'])
            github_event.type_output()

        if event_type == "PullRequestReviewCommentEvent":
            github_event = Evt.PullRequestReviewCommentEvent(event_id, event_type, event_actor, event_payload)
            github_event.type_output()

        if event_type == "ForkEvent":
            github_event = Evt.ForkEvent(event_id, event_type, event_actor, event_payload)
            github_event.type_output()
        
        if event_type == "CreateEvent":
            github_event = Evt.CreateEvent(event_id, event_type, event_actor, event_payload)
            github_event.type_output()
        
        if event_type == "DeleteEvent":
            github_event = Evt.DeleteEvent(event_id, event_type, event_actor, event_payload)
            github_event.type_output()
        



