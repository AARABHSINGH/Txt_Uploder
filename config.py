import os

API_ID = API_ID = 26910519

API_HASH = os.environ.get("API_HASH", "0b14672454a94495a50c9381ba107e30")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "7406435671:AAEPYbdAMO_PDTfUYk5b2QHbhDth9QF96ug")
PASS_DB = int(os.environ.get("PASS_DB", "721"))

OWNER = int(os.environ.get("OWNER", 7036285759))

LOG = -1002148302049
try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "7036285759").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
ADMINS.append(OWNER)


