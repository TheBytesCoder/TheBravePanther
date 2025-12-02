#🇳‌🇮‌🇰‌🇭‌🇮‌🇱‌
# Add your details here and then deploy by clicking on HEROKU Deploy button
import os
from os import environ

API_ID = int(environ.get("API_ID", "29893064"))
API_HASH = environ.get("API_HASH", "953d0ab0b8a0753f93c851dd08185e33")
BOT_TOKEN = environ.get("BOT_TOKEN", "8316328627:AAGwXwZXysaFXdE18cV18naNCvpHOT-ZbWw")

OWNER = int(environ.get("OWNER", "7645438227"))
CREDIT = environ.get("CREDIT", "BЯΛVΣMΛП")
cookies_file_path = os.getenv("cookies_file_path", "youtube_cookies.txt")

TOTAL_USER = os.environ.get('TOTAL_USERS', '7645438227').split(',')
TOTAL_USERS = [int(user_id) for user_id in TOTAL_USER]

AUTH_USER = os.environ.get('AUTH_USERS', '7645438227').split(',')
AUTH_USERS = [int(user_id) for user_id in AUTH_USER]
if int(OWNER) not in AUTH_USERS:
    AUTH_USERS.append(int(OWNER))



