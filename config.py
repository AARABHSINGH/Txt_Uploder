import os

API_ID = API_ID = 26910519

API_HASH = os.environ.get("API_HASH", "0b14672454a94495a50c9381ba107e30")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "7507692165:AAFDl3B_TIswjPMjFe4LcY9fPe8X7kPsr2w")
PASS_DB = int(os.environ.get("PASS_DB", "721"))

OWNER = int(os.environ.get("OWNER", 7036285759))

LOG = -1002248172181
try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "7036285759").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
ADMINS.append(OWNER)


