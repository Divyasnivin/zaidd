## What's up Kangers

import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "BABO34px1XAcm4CErq7uGtBauQeSZXihVEJrvB-dq_ju1GjAZZzGWW08I-qBpkBTOlkYN9FQ4BAvAdAW8Lym6nj98rFS7v3CD2EIvYNvLJSk8nQU6gX58XPSibswF8ES5sfFMqan4aeqVmYADClsALwVFSMbd4OjOWPGYy4g3VUQoVRP9AY4uaSvn-3wHY55S0Xoq65xvOep0gwEkrfXOODOQZT-Y8npz5wecu-CFhgJ1zejJYUbtucTDUYwOUgOmCTRE_Q86PMJT7qNqTcxt42f0rr8qbf317qwu1IEBDD36vNTlMuTxKgxx3dv3hXe-nD92qtYgZT6TgOOudxV-8alAAAAACbwiEIA")
BOT_TOKEN = getenv("BOT_TOKEN", "5130396512:AAGZQTvxI92Z47beIoNGsV3WN4DkZyZvoH0")
BOT_NAME = getenv("BOT_NAME", "felix")
API_ID = int(getenv("API_ID", "19680685"))
API_HASH = getenv("API_HASH", "35c8346d7d35af39fcc9204493970277")
OWNER_NAME = getenv("OWNER_NAME", "هادي")
OWNER_USERNAME = getenv("OWNER_USERNAME", "jbbbbf")
ALIVE_NAME = getenv("ALIVE_NAME", "هادي")
BOT_USERNAME = getenv("BOT_USERNAME", "rnn0bot")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "abfm00")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "kkcet")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "kkcet")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5049024596").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/fc9d87ffd1c6f828eb7fc.png")
START_PIC = getenv("START_PIC", "https://telegra.ph/file/fc9d87ffd1c6f828eb7fc.png")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/Divyasnivin/zaidd")
IMG_1 = getenv("IMG_1", "https://telegra.ph/file/d6f92c979ad96b2031cba.png")
IMG_2 = getenv("IMG_2", "https://telegra.ph/file/6213d2673486beca02967.png")
IMG_3 = getenv("IMG_3", "https://telegra.ph/file/f02efde766160d3ff52d6.png")
IMG_4 = getenv("IMG_4", "https://telegra.ph/file/be5f551acb116292d15ec.png")
IMG_5 = getenv("IMG_5", "https://telegra.ph/file/c3401a572375b569138c3.png")
IMG_6 = getenv("IMG_6", "https://telegra.ph/file/c3401a572375b569138c3.png")
