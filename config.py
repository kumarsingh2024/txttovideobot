import os

API_ID = API_ID = 22867163

API_HASH = os.environ.get("API_HASH", "a633197e388c9235b4d0032d921c59dd")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "6976049011:AAHiDht1_3bcoSDA_YqC9yed1P_CsqO2a8s")

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
