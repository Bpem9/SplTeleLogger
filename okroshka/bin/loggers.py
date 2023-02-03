

from abc import ABC, abstractmethod


class LogFactory(ABC):
    @abstractmethod
    async def get_log(self):
        """
        Returns attribute dictionary for LogObj depending on event type
        """
        pass


class AdminLog(LogFactory):
    """
    Returns attributes in case of AdminLog events
    """
    def __init__(self, event):
        self.event = event
        self.event_dict = {
            'date': event.date.strftime('%d.%m.%Y/%H:%M:%S'),
            'responsible_user': event.user_id,
        }

    async def get_log(self):
        if self.event.changed_title:
            self.event_dict.update({'incident': f'Title_changed_from:_{self.event.old}_to:_{self.event.new}'})
        elif self.event.changed_admin:
            if hasattr(self.event.new, 'admin_rights'):
                self.event_dict.update({
                    'incident': 'User_received_admin_permissions',
                    'target_user': self.event.new.user_id,
                })
            else:
                self.event_dict.update({
                    'incident': 'Admin_rights_removed_from_the_user',
                    'target_user': self.event.old.user_id,
                })
        elif self.event.joined_by_invite:
            self.event_dict.update({
                'incident': 'User_joined_by_invite',
                'responsible_user': self.event.user_id,
                'target_user': self.event,
            })
        elif self.event.changed_username:
            self.event_dict.update({
                'incident': f'Changed_username_from:_{self.event.old}_to:_{self.event.new}',
                'target_user': self.event.new,
            })
        else:
            self.event_dict.update({
                'incident': f'Untracked_admin_incident',
                'responsible_user': self.event.user_id,
            })
        return self.event_dict


class ChatLog(LogFactory):
    """
    Returns attributes in case of Chat events
    """
    def __init__(self, event):
        self.event = event
        self.event_dict = {
            'date': event.action_message.date.strftime('%d.%m.%Y/%H:%M:%S'),
            'user_id': event.get_user(),
        }

    async def get_log(self):
        if self.event.changed_title:
            self.event_dict.update({'incident': 'New_title', 'new_title': self.event.new})
        if self.event.user_added:
            self.event_dict.update({'incident': 'User_added_by_admin'})
        if self.event.user_left:
            self.event_dict.update({'incident': 'User_left'})
        if self.event.user_kicked:
            self.event_dict.update({'incident': 'User_kicked_by_admin'})
        return self.event_dict


class MessageLog(LogFactory):
    """
    Returns attributes in case of Message events
    """
    def __init__(self, event):
        self.event = event
        self.event_dict = {
            'date': event.date.strftime('%d.%m.%Y/%H:%M:%S'),
            'responsible_user': event.sender.id,
            'incident': 'New_message',
            'message': event.message
        }

    async def get_log(self):
        return self.event_dict


class UntrackedLog(LogFactory):
    """
    Returns attributes in case of Untracked events
    """
    def __init__(self, event):
        self.event = event
        self.event_dict = {
            'date': event.date.strftime('%d.%m.%Y/%H:%M:%S'),
            'event': 'Untracked_event'
        }

    async def get_log(self):
        return self.event_dict



