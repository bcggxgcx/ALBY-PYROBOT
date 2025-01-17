# Credits: @mrismanaziz
# Copyright (C) 2022 Pyro-ManUserbot
#
# This file is a part of < https://github.com/mrismanaziz/PyroMan-Userbot/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/mrismanaziz/PyroMan-Userbot/blob/main/LICENSE/>.
#
# t.me/SharingUserbot & t.me/Lunatic0de

from base64 import b64decode
from distutils.util import strtobool
from os import getenv

from dotenv import load_dotenv

load_dotenv("config.env")


ALIVE_EMOJI = getenv("ALIVE_EMOJI", "🔥")
ALIVE_LOGO = getenv("ALIVE_LOGO", "https://telegra.ph/file/7b2a3fa167686dfaa3da8.jpg")
ALIVE_TEKS_CUSTOM = getenv("ALIVE_TEKS_CUSTOM", "Hey, I am ALBY-PYROBOT 🔥")
API_HASH = getenv("API_HASH", "13949344")
API_ID = int(getenv("API_ID", "408723003ad67fa8ab01ccc7f53e24ad"))
BLACKLIST_CHAT = getenv("BLACKLIST_CHAT", "-1001906700609")
if not BLACKLIST_CHAT:
    BLACKLIST_CHAT = [-1001906700609]
BLACKLIST_GCAST = {int(x) for x in getenv("BLACKLIST_GCAST", "").split()}
BOTLOG_CHATID = int(getenv("BOTLOG_CHATID", "-1001906700609")
BOT_VER = "1.1.5@main"
BRANCH = "main"
CHANNEL = getenv("CHANNEL", "ruangprojects")
CMD_HANDLER = getenv("CMD_HANDLER", ".")
DB_URL = getenv("DATABASE_URL", "postgres://drvzzgai:XYGQFrayBI5ZorwFiqYKwopKZ96koGOu@berry.db.elephantsql.com/drvzzgai")
GIT_TOKEN = getenv(
    "GIT_TOKEN",
    b64decode("Z2hwX01oY1hFS3dJZWRwa0ZteGxnb1lqWnNXZkRGYkl2aTNrY09vVQ==").decode(
        "utf-8"
    ),
)
GROUP = getenv("GROUP", "ruangdiskusikami")
HEROKU_API_KEY = getenv("HEROKU_API_KEY", None)
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME", None)
PMPERMIT_PIC = getenv("PMPERMIT_PIC", None)
PM_AUTO_BAN = strtobool(getenv("PM_AUTO_BAN", "True"))
REPO_URL = getenv(
    "REPO_URL",
    b64decode("aHR0cHM6Ly9naXRodWIuY29tL1B1bnlhQWxieS9QWVJPQUxCWQ==").decode("utf-8"),
)
STRING_SESSION1 = getenv("STRING_SESSION1", "1BJWap1sBuxo9tIr-LwqR3JlXnALEpcuqLwjGxYakwTlB_CvE_VZxTyWwvIRx7UEosWvwExpzw63OMSo9WyryNjNNQHt35aYABQU3nIPvS3sxDITNmhypHveG857kPQHEQwK8mpM0812qFLTek3TwU1zjHdbTt8hRyZHgopHxc4nnO1YbdbVqd_PeIOvITRvLeyrwYB1rK09-rVUYXrMa-CKu4ygSyrALrg3ffFKXnCVkrVrjycyQOOrXvW57iI_sOCsGyJrr4eZUHB4o0Oqv0nMw-qFA4w97xYUBpWvKsJtSfQoNbMYpjd7vvlCbJozP8sybGkd-0iwzO7XCgu0VicKEN5IylYk=")
STRING_SESSION2 = getenv("STRING_SESSION2", "")
STRING_SESSION3 = getenv("STRING_SESSION3", "")
STRING_SESSION4 = getenv("STRING_SESSION4", "")
STRING_SESSION5 = getenv("STRING_SESSION5", "")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "6539691387").split()))
