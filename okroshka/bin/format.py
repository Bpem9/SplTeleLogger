

from telethon.tl.types import ChannelParticipantAdmin
from loggers import *



class LogObj:
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def __str__(self):
        """
        Возвращает строковое представление лога в заданном формате, при обращении через str(instance: LogObj)
        """
        string = ''
        for key, value in self.__dict__.items():
            string += f' {key}={value}'
        return string

    @classmethod
    async def _get_admin_log(cls, event):
        """
        If event condition in tracked - returns admin LogObj, else untracked LogObj
        """
        logger = AdminLog(event)
        # if event.changed_admin:
        event_dict = await logger.get_log()
        # else:
        #     logger = UntrackedLog(event)
        #     event_dict = logger.event_dict
        return LogObj(**event_dict)

    @classmethod
    async def _get_message_log(cls, event):
        logger = MessageLog(event)
        event_dict = await logger.get_log()
        return LogObj(**event_dict)

    @classmethod
    async def _get_chat_log(cls, event):
        logger = ChatLog(event)
        event_dict = await logger.get_log()
        return LogObj(**event_dict)

    @classmethod
    async def _get_untracked_log(cls, event):
        logger = UntrackedLog(event)
        event_dict = await logger.get_log()
        return LogObj(**event_dict)

    @staticmethod
    async def get_log(event, condition):
        """
        Фабричный метод возвращает объект Лог с параметрами (событие, объект события (event), пользователь, дата).
        Инкупсулирует создание логов из событий разных обработчиков:
        получение сообщения(NewMessage) и общие события чата(ChatAction)
        """
        if condition == 'admin':
            obj = await LogObj._get_admin_log(event)
        if condition == 'message':
            obj = await LogObj._get_message_log(event)
        if condition == 'chat':
            obj = await LogObj._get_chat_log(event)
        if condition == 'untracked':
            obj = await LogObj._get_untracked_log(event)
        # incident = None
        # if hasattr(event, 'message'):
        #     date = event.date.strftime('%d.%m.%Y/%H:%M:%S')
        #     user = await event.get_sender()
        #     incident = 'New_message'
        # else:
        #
        #     date = event.action_message.date.strftime('%d.%m.%Y/%H:%M:%S')
        #     user = await event.get_user()
        #     if event.new_title is True:
        #         incident = 'New_title'
        #     if event.user_left is True:
        #         incident = 'User_left'
        #     if event.user_joined is True:
        #         incident = 'User_joined'
        #     if event.user_kicked is True:
        #         incident = 'User_kicked_by_admin'
        #     if event.user_added is True:
        #         incident = 'User_added_by_admin'
        # if not incident:
        #     incident = 'Untracked_incident'
        return obj

