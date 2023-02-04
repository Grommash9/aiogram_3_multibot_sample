import json
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()
import os

cwd = Path().cwd()

BASE_URL = os.getenv("WEBHOOK_HOST", "https://example.com")
MAIN_BOT_TOKEN = os.getenv("MAIN_BOT_TOKEN")

WEB_SERVER_HOST = os.getenv('BOT_SERVER_HOST')
WEB_SERVER_PORT = os.getenv('BOT_SERVER_PORT')
MAIN_BOT_PATH = f"/aiogram_{cwd.name}/main"
OTHER_BOTS_PATH = f"/aiogram_{cwd.name}/child_bot/" + "{bot_token}"
REDIS_DSN = "redis://127.0.0.1:6379"

OTHER_BOTS_URL = f"{BASE_URL}{OTHER_BOTS_PATH}"

MYSQL = {
    'host': os.getenv('MYSQL_HOST'),
    'user': os.getenv('MYSQL_USER'),
    'password': os.getenv('MYSQL_PASSWORD'),
    'db': os.getenv('MYSQL_DB_NAME'),
    'port': int(os.getenv('MYSQL_PORT'))
    # 'unix_socket': '/var/run/mysqld/mysqld.sock'
}

#
# ROUTE_URL = os.getenv('ROUTE_URL')
# POLLING = os.getenv('POLLING')
# ADMINS_ID = json.loads(os.getenv('ADMINS_ID'))
# BOT_TOKEN = os.getenv('BOT_TOKEN')
# is_ssl = os.getenv('SSL')
#
# NOTIFY_USERS = json.loads(os.getenv('NOTIFY_USERS'))
#
# WEBHOOK_HOST = os.getenv('WEBHOOK_HOST')
# WEBHOOK_PATH = f'{cwd.name}'
# WEBHOOK_URL = f"{WEBHOOK_HOST}/{WEBHOOK_PATH}/"
#
# BOT_SERVER = {
#     'host': os.getenv('BOT_SERVER_HOST'),
#     'port': os.getenv('BOT_SERVER_PORT')
# }
#
# REDIS = {
#     'db': 2,
#     'prefix': cwd.name
# }
# # sad
#
#
