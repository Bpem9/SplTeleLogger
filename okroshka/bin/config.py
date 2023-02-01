import os
from dotenv import load_dotenv

load_dotenv()
API_ID = os.getenv('API_ID')
API_HASH = os.getenv('API_HASH')
# TEST_CHANNEL_ID = os.getenv('TEST_CHANNEL_ID')
TEST_CHANNEL_NAME = os.getenv('TEST_CHANNEL_NAME')
# TEST_CHAT_NAME = os.getenv('TEST_CHAT_NAME')
MAX_LOGFILE_LINES = 20
USER_PHONE = os.getenv('USER_PHONE')
SESSION_STRING = os.getenv('SESSION_STRING')