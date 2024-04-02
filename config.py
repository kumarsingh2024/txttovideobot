import os

API_ID = API_ID = Your api id

API_HASH = os.environ.get("API_HASH", "Your api hash")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "Your bot token")

PASS_DB = int(os.environ.get("PASS_DB", "100"))

OWNER = int(os.environ.get("OWNER", Your user id ))

LOG = -1002008011161            #don't change it otherwise you face error while deploying.
try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "Your user id").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
ADMINS.append(OWNER)
