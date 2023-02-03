
from telethon.sessions import StringSession

from config import *
from format import LogObj
import logging
from telethon import TelegramClient

client = TelegramClient(StringSession(SESSION_STRING), API_ID, API_HASH, catch_up=True)

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)


async def get_changes():
    """
    Receives events from TEST_CHANNEL_NAME telegram chat, and passes the condition string,
    depending on type of event. The LogCollector class from filemanager.py supposed to
    handle writing the Log file but as long as logs from standard print output
    are enough for splunk to collect, the LogCollector will be switched off
    """
    message_events = await client.get_messages(TEST_CHANNEL_NAME)
    admin_events = await client.get_admin_log(TEST_CHANNEL_NAME)
    for event in message_events:
        if hasattr(event, 'message'):
            log_obj = await LogObj.get_log(event, 'message')
        else:
            log_obj = await LogObj.get_log(event, 'chat')
        print(str(log_obj))
    for event2 in admin_events:
        log_obj = await LogObj.get_log(event2, 'admin')
        print(str(log_obj))


if __name__ == '__main__':
    with client:
        client.loop.run_until_complete(get_changes())
