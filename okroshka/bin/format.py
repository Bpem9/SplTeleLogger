
from loggers import *


class LogObj:
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def __str__(self):
        """
        Returns formatted string view of the log if use str(instance: LogObj)
        """
        for key, value in self.__dict__.items():
            if key == 'date':
                string = f'{value}'
            else:
                string += f', {key}="{value}"'
        return string

    @staticmethod
    async def get_log(event, condition):
        """
        Factory method encapsulates logs creating using different handlers:
        MessageLog, AdminLog, ChatLog, UntrackedLog.
        Returns LogObj with specific parameters for different actions
        (date, incident name, Event object (event), user).
        """
        if condition == 'admin':
            logger = AdminLog(event)
        if condition == 'message':
            logger = MessageLog(event)
        if condition == 'chat':
            logger = ChatLog(event)
        if condition == 'untracked':
            logger = UntrackedLog(event)
        event_dict = await logger.get_log()
        return LogObj(**event_dict)


