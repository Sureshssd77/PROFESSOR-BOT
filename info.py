import re, time
from os import environ
from Script import script 
from pyrogram import Client
from pymongo import MongoClient

id_pattern = re.compile(r'^.\d+$')

def is_enabled(value, default):
    if value.strip().lower() in ["on", "true", "yes", "1", "enable", "y"]: return True
    elif value.strip().lower() in ["off", "false", "no", "0", "disable", "n"]: return False
    else: return default

# API Credentials और Bot details (जो आपने दी थी)
API_ID = 22506926  # API ID यहाँ डाला गया है
API_HASH = '34fe7b7d19572aae39c6db80e151d9f7'  # API HASH यहाँ डाला गया है
BOT_TOKEN = '8004078816:AAFpANlxyG1emrSLYYuJXgEecNGJIvme78c'  # BOT TOKEN यहाँ डाला गया है

# MongoDB details
DATABASE_URL = "mongodb+srv://dilipdewasi7759:<NMzFkZqWZdi1GDG4>@ssdmovies.2nqad.mongodb.net/?retryWrites=true&w=majority&appName=ssdmovies"
DATABASE_NAME = "Cluster0"
FILE_DB_URL = DATABASE_URL
FILE_DB_NAME = DATABASE_NAME
COLLECTION_NAME = 'Telegram_files'

# Admins, Channels & Users
CACHE_TIME = 300
ADMINS = [6151975257]  # Admin ID यहाँ डाला गया है
CHANNELS = [-1002144001843]  # Channel ID यहाँ डाला गया है
AUTH_USERS = [6151975257]  # Auth Users
AUTH_CHANNEL = None
AUTH_GROUPS = None

# Welcome image and message
WELCOM_PIC = "https://graph.org/file/1118970f6a47013b7ec47-1903a973000f540eca.jpg"
WELCOM_TEXT = script.WELCOM_TEXT

# Bot settings
WEB_SUPPORT = True
PICS = [
    'https://graph.org/file/01ddfcb1e8203879a63d7.jpg',
    'https://graph.org/file/d69995d9846fd4ad632b8.jpg',
    'https://graph.org/file/a125497b6b85a1d774394.jpg'
]
UPTIME = time.time()

# Filters Configuration 
MAX_RIST_BTNS = 10
START_MESSAGE = script.START_TXT
BUTTON_LOCK_TEXT = script.BUTTON_LOCK_TEXT
FORCE_SUB_TEXT = script.FORCE_SUB_TEXT

# Others
IMDB_DELET_TIME = 300
LOG_CHANNEL = -1002429570370  # Log Channel ID यहाँ डाला गया है
SUPPORT_CHAT = 'MKN_BOTZ_DISCUSSION_GROUP'

# Pyrogram client setup
app = Client("my_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

# MongoDB client setup
client = MongoClient(DATABASE_URL)
db = client[DATABASE_NAME]
collection = db[COLLECTION_NAME]

@app.on_message()
async def handle_message(client, message):
    if message.text == "/start":
        await message.reply(WELCOM_TEXT, photo=WELCOM_PIC)

@app.on_message()
async def handle_document(client, message):
    if message.document:
        file_info = {
            "file_name": message.document.file_name,
            "file_id": message.document.file_id,
            "user_id": message.from_user.id
        }
        collection.insert_one(file_info)
        await message.reply(f"File {message.document.file_name} saved!")

# Run the bot
app.run()
