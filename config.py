import os

API_ID = API_ID = 27464924

API_HASH = os.environ.get("API_HASH", "f28d089001481597f045b70a0daa73e4")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "6513648341:AAEm5tbyQPWxU55QzJl2bVOJX6JvA-dy1yU")

PASS_DB = int(os.environ.get("PASS_DB", "100"))

OWNER = int(os.environ.get("OWNER", 1871785273))

LOG = -1002132785565
try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "1871785273").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
ADMINS.append(OWNER)
