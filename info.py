import re, logging
from os import environ
from Script import script

def is_enabled(type, value):
    data = environ.get(type, str(value))
    if data.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif data.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        print(f'Error - {type} is invalid, exiting now')
        exit()

def is_valid_ip(ip):
    ip_pattern = r'\b(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\b'
    return re.match(ip_pattern, ip) is not None

# Bot information
API_ID = environ.get('API_ID', '23898744')
if len(API_ID) == 0:
    print('Error - API_ID is missing, exiting now')
    exit()
else:
    API_ID = int(API_ID)
API_HASH = environ.get('API_HASH', '0b13c810c80b548604650cbe3c3db0c3')
if len(API_HASH) == 0:
    print('Error - API_HASH is missing, exiting now')
    exit()
BOT_TOKEN = environ.get('BOT_TOKEN', '6627232964:AAHilF7xvfR9Xfrh2ZBHFkNjRPMURw3qht0')
if len(BOT_TOKEN) == 0:
    print('Error - BOT_TOKEN is missing, exiting now')
    exit()
PORT = int(environ.get('PORT', '8080'))

# Bot pics
PICS = (environ.get('PICS', 'https://graph.org/file/d02bb50008a48695bd658.jpg https://graph.org/file/b2021572ba9aa8d2c0cf2.jpg https://graph.org/file/e4b8568a59cb7095d185a.jpg https://graph.org/file/aea87e4842c7b56345603.jpg https://graph.org/file/54d6f666b81bd2523ef53.jpg https://graph.org/file/c086cdb386fb0bd8a41f5.jpg https://graph.org/file/3505557916c9b26728c1a.jpg https://graph.org/file/a793b1d49c3ee95cc309e.jpg https://graph.org/file/733fa5d50bfbc5b87d749.jpg https://graph.org/file/23cf6931a2aa9d6e09b1a.jpg https://graph.org/file/702040fb6dd8a2ed01402.jpg https://graph.org/file/7a42f50e54e0f15c55044.jpg https://graph.org/file/6e7782421e33b7f6e1c79.jpg https://graph.org/file/371d56eab691dab1c83b8.jpg')).split()

# Bot Admins
ADMINS = environ.get('ADMINS', '5698613889')
if len(ADMINS) == 0:
    print('Error - ADMINS is missing, exiting now')
    exit()
else:
    ADMINS = [int(admins) for admins in ADMINS.split()]

# Channels
INDEX_CHANNELS = [int(index_channels) if index_channels.startswith("-") else index_channels for index_channels in environ.get('INDEX_CHANNELS', '-1001856938140').split()]
if len(INDEX_CHANNELS) == 0:
    print('Info - INDEX_CHANNELS is empty')
AUTH_CHANNEL = [int(auth_channels) for auth_channels in environ.get('AUTH_CHANNEL', '-1001713712725').split()]
if len(AUTH_CHANNEL) == 0:
    print('Info - AUTH_CHANNEL is empty')
LOG_CHANNEL = environ.get('LOG_CHANNEL', '-1002022311143')
if len(LOG_CHANNEL) == 0:
    print('Error - LOG_CHANNEL is missing, exiting now')
    exit()
else:
    LOG_CHANNEL = int(LOG_CHANNEL)

# support group
SUPPORT_GROUP = environ.get('SUPPORT_GROUP', '-1001792853580')
if len(SUPPORT_GROUP) == 0:
    print('Error - SUPPORT_GROUP is missing, exiting now')
    exit()
else:
    SUPPORT_GROUP = int(SUPPORT_GROUP)

# for chatGPT
OPENAI_API = environ.get('OPENAI_API', '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')
if len(OPENAI_API) == 0:
    print('Info - OPENAI_API is empty')

# MongoDB information
DATABASE_URL = environ.get('DATABASE_URL', "mongodb+srv://Filmy:oiKn0AkUrgeBGDFq@rohidasgavit.pbz03z1.mongodb.net/?retryWrites=true&w=majority")
if len(DATABASE_URL) == 0:
    print('Error - DATABASE_URL is missing, exiting now')
    exit()
DATABASE_NAME = environ.get('DATABASE_NAME', "Telegram")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Files')

# Links
SUPPORT_LINK = environ.get('SUPPORT_LINK', 'https://t.me/MKV_FILES_ROHESH')
UPDATES_LINK = environ.get('UPDATES_LINK', 'https://t.me/Filmy_Rohesh')
FILMS_LINK = environ.get('FILMS_LINK', 'https://t.me/Movie_Searching_Pro')
TUTORIAL = environ.get("TUTORIAL", "https://t.me/Filmy_Rohesh")
VERIFY_TUTORIAL = environ.get("VERIFY_TUTORIAL", "https://t.me/Filmy_Rohesh")

# Bot settings
DELETE_TIME = int(environ.get('DELETE_TIME', 3600)) # Add time in seconds
CACHE_TIME = int(environ.get('CACHE_TIME', 300))
MAX_BTN = int(environ.get('MAX_BTN', 10))
LANGUAGES = [language.lower() for language in environ.get('LANGUAGES', 'english hindi telugu tamil kannada malayalam').split()]
IMDB_TEMPLATE = environ.get("IMDB_TEMPLATE", script.IMDB_TEMPLATE)
FILE_CAPTION = environ.get("FILE_CAPTION", script.FILE_CAPTION)
SHORTLINK_URL = environ.get("SHORTLINK_URL", "mdiskshortner.link")
SHORTLINK_API = environ.get("SHORTLINK_API", "36f1ae74ba1aa01e5bd73bdd0bc22aa915443501")
VERIFY_EXPIRE = int(environ.get('VERIFY_EXPIRE', 86400)) # Add time in seconds
WELCOME_TEXT = environ.get("WELCOME_TEXT", script.WELCOME_TEXT)
INDEX_EXTENSIONS = [extensions.lower() for extensions in environ.get('INDEX_EXTENSIONS', 'mp4 mkv').split()]

# boolean settings
IS_VERIFY = is_enabled('IS_VERIFY', True)
AUTO_DELETE = is_enabled('AUTO_DELETE', True)
WELCOME = is_enabled('WELCOME', True)
PROTECT_CONTENT = is_enabled('PROTECT_CONTENT', False)
LONG_IMDB_DESCRIPTION = is_enabled("LONG_IMDB_DESCRIPTION", False)
LINK_MODE = is_enabled("LINK_MODE", True)
AUTO_FILTER = is_enabled('AUTO_FILTER', True)
IMDB = is_enabled('IMDB', True)
SPELL_CHECK = is_enabled("SPELL_CHECK", True)
SHORTLINK = is_enabled('SHORTLINK', False)

# for stream
IS_STREAM = is_enabled('IS_STREAM', True)
BIN_CHANNEL = environ.get("BIN_CHANNEL", "-1002077669335")
if len(BIN_CHANNEL) == 0:
    print('Error - BIN_CHANNEL is missing, exiting now')
    exit()
else:
    BIN_CHANNEL = int(BIN_CHANNEL)
URL = environ.get("URL", "nobita-striming.onrender.com")
if len(URL) == 0:
    print('Error - URL is missing, exiting now')
    exit()
else:
    if URL.startswith(('https://', 'nobita-striming.onrender.com')):
        if not URL.endswith("/"):
            URL += '/'
    elif is_valid_ip(URL):
        URL = f'http://{URL}/'
    else:
        print('Error - URL is not valid, exiting now')
        exit()
