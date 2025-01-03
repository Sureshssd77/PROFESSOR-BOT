# bot.py

import re, time
from os import environ
from info import DATABASE_NAME, DATABASE_URL, IMDB, IMDB_TEMPLATE, MELCOW_NEW_USERS, P_TTI_SHOW_OFF, SINGLE_BUTTON, SPELL_CHECK_REPLY, PROTECT_CONTENT, MAX_RIST_BTNS, IMDB_DELET_TIME
from Script import script

id_pattern = re.compile(r'^.\d+$')

def is_enabled(value, default):
    if value.strip().lower() in ["on", "true", "yes", "1", "enable", "y"]: return True
    elif value.strip().lower() in ["off", "false", "no", "0", "disable", "n"]: return False
    else: return default

# PyroClient Setup 
API_ID = 22506926
API_HASH = "34fe7b7d19572aae39c6db80e151d9f7"
BOT_TOKEN = "8004078816:AAFpANlxyG1emrSLYYuJXgEecNGJIvme78c"

# Bot settings
WEB_SUPPORT = True # for web support on/off
PICS = "https://graph.org/file/01ddfcb1e8203879a63d7.jpg https://graph.org/file/d69995d9846fd4ad632b8.jpg".split()
UPTIME = time.time()

# Admins, Channels & Users
CACHE_TIME = 300
ADMINS = [6151975257]  # Admin ID
CHANNELS = [-1002144001843]  # Channel ID
auth_users = [6151975257]
AUTH_USERS = auth_users + ADMINS
AUTH_CHANNEL = None
AUTH_GROUPS = None

# MongoDB information
DATABASE_URL = "mongodb+srv://dilipdewasi7759:<NMzFkZqWZdi1GDG4>@ssdmovies.2nqad.mongodb.net/?retryWrites=true&w=majority&appName=ssdmovies"
FILE_DB_URL = DATABASE_URL
FILE_DB_NAME = DATABASE_NAME
COLLECTION_NAME = "Telegram_files"

# Filters Configuration 
MAX_RIST_BTNS = 10
START_MESSAGE = script.START_TXT
BUTTON_LOCK_TEXT = script.BUTTON_LOCK_TEXT
FORCE_SUB_TEXT = script.FORCE_SUB_TEXT

WELCOM_PIC = "https://graph.org/file/1118970f6a47013b7ec47-1903a973000f540eca.jpg"
WELCOM_TEXT = script.WELCOM_TEXT
PMFILTER = True
G_FILTER = True
BUTTON_LOCK = True
RemoveBG_API = ""

# Others
IMDB_DELET_TIME = 300
LOG_CHANNEL = -1002429570370  # Log Channel ID
SUPPORT_CHAT = 'MKN_BOTZ_DISCUSSION_GROUP'
P_TTI_SHOW_OFF = True
PM_IMDB = True
IMDB = True
SINGLE_BUTTON = True
CUSTOM_FILE_CAPTION = "{file_name}"
BATCH_FILE_CAPTION = None
IMDB_TEMPLATE = script.IMDB_TEMPLATE
LONG_IMDB_DESCRIPTION = False
SPELL_CHECK_REPLY = True
MAX_LIST_ELM = None
FILE_STORE_CHANNEL = [-1002144001843]  # File Store Channel
MELCOW_NEW_USERS = True
PROTECT_CONTENT = False
PUBLIC_FILE_STORE = True
LOG_MSG = "{} Iꜱ Rᴇsᴛᴀʀᴛᴇᴅ....✨\n\n🗓️ Dᴀᴛᴇ : {}\n⏰ Tɪᴍᴇ : {}\n\n🖥️ Rᴇᴏᴩ: {}\n🉐 Vᴇʀsɪᴏɴ: {}\n🧾 Lɪᴄᴇɴꜱᴇ: {}\n©️ Cᴏᴩʏʀɪɢʜᴛ: {}"
