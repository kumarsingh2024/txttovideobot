import os

API_ID = API_ID = 22867163

API_HASH = os.environ.get("API_HASH", "a633197e388c9235b4d0032d921c59dd")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "7014636983:AAELoi5MU1nTuS91Uh_RgZG2vBk_pHwAK4A")

PASS_DB = int(os.environ.get("PASS_DB", "100"))

OWNER = int(os.environ.get("OWNER", 5630726804 ))

LOG = -1002008011161            #don't change it otherwise you face error while deploying.
try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "5630726804").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
ADMINS.append(OWNER)
