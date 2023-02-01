

from abc import ABC, abstractmethod
from telethon.tl.types import ChannelParticipantAdmin

class LogFactory(ABC):
    @abstractmethod
    async def get_log(self):
        """ Returns LogObg depending on event type"""
        pass


class AdminLog(LogFactory):
    def __init__(self, event):
        self.event = event
        self.event_dict = {
            'date': event.date.strftime('%d.%m.%Y/%H:%M:%S'),
            'user_id': event.new.user_id if hasattr(event.new, 'user_id') else '-',
            'responsible': event.user_id
        }

    async def get_log(self):
        if isinstance(self.event.new, ChannelParticipantAdmin):
            self.event_dict.update({'incident': 'User_recieved_admin_premissions'})
        else:
            self.event_dict.update({'incident': 'Admin_rights_removed_from_the_user'})
        return self.event_dict


class UntrackedLog(LogFactory):
    def __init__(self, event):
        self.event = event
        self.event_dict = {
            'date': self.event.date.strftime('%d.%m.%Y/%H:%M:%S'),
            'event': 'Untracked_event'
        }
    async def get_log(self):

        return self.event_dict

class ChatLog(LogFactory):
    def __init__(self, event):
        self.event = event
        self.event_dict = {
            'date': self.event.action_message.date.strftime('%d.%m.%Y/%H:%M:%S'),
            'user_id': self.event.get_user(),
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
    def __init__(self, event):
        user = event.sender.id
        self.event = event
        self.event_dict = {
            'date': self.event.date.strftime('%d.%m.%Y/%H:%M:%S'),
            'user_id': user,
            'incident': 'New_message',
        }

    async def get_log(self):
        return self.event_dict


