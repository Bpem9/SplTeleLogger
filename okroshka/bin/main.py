
from telethon.sessions import StringSession

from config import *
from format import LogObj
import logging
import os
from telethon import TelegramClient


client = TelegramClient(StringSession(SESSION_STRING), API_ID, API_HASH, sequential_updates=True)

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)




# @client.on(events.NewMessage(chats=TEST_CHANNEL_NAME))
# async def chat_message_handler(event):
#     """Обрабатывает сообщения в чате"""
#     log = await LogObj.get_log(event)
#     print(str(log))
#     await LogCollector.log_create(str(log))
#
#
# @client.on(events.ChatAction(chats=TEST_CHANNEL_NAME))
# async def handler(event):
#     """Обрабатывает события чата (Добавление/удаление пользователей и т.д.)"""
#     log = await LogObj.get_log(event)
#     # print(dir(event.get_user()))
#     # print(str(log))
#     await LogCollector.log_create(str(log))


async def get_changes():
    await client.start()
    message_events = await client.get_messages(TEST_CHANNEL_NAME)
    admin_events = await client.get_admin_log(TEST_CHANNEL_NAME)
    for event in message_events:
        if hasattr(event, 'message'):
            log_obj = await LogObj.get_log(event, 'message')
        else:
            log_obj = await LogObj.get_log(event, 'chat')
        print(str(log_obj))
    for event in admin_events:
        log_obj = await LogObj.get_log(event, 'admin')
        print(str(log_obj))


if __name__ == '__main__':
    # with client:
        # client.run_until_disconnected()
        # client.loop.run_until_complete(authen())
        client.loop.run_until_complete(get_changes())


