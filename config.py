import re
import sys
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

API_ID = int(getenv("API_ID", "7782147"))
API_HASH = getenv("API_HASH", "807b64fbb57797086097d274df3a934c")

BOT_TOKEN = getenv("BOT_TOKEN", "5806315236:AAGbkbK_bV4IT8ToMGYhm9jTe2SK9dzNMos")

MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://Aman:Aman@cluster0.gt2bc.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", "-1001811125658"))
MUSIC_BOT_NAME = getenv("MUSIC_BOT_NAME", "ιηƒℓє¢тιση")

OWNER_ID = list(map(int, getenv("OWNER_ID", "1820525265").split()))

HEROKU_API_KEY = getenv("HEROKU_API_KEY", None)
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME", None)

UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/AnonymousX1025/AnonXMusic")
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")
GIT_TOKEN = getenv("GIT_TOKEN", None)

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/TEAM_XTRON")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "https://t.me/TEAMXTRON")

SUPPORT_HEHE = SUPPORT_GROUP.split("me/")[1]

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", "180"))
SONG_DOWNLOAD_DURATION = int(getenv("SONG_DOWNLOAD_DURATION_LIMIT", "180"))

AUTO_LEAVING_ASSISTANT = getenv("AUTO_LEAVING_ASSISTANT", "False")
AUTO_LEAVE_ASSISTANT_TIME = int(
    getenv("ASSISTANT_LEAVE_TIME", "5400")
)

AUTO_DOWNLOADS_CLEAR = getenv("AUTO_DOWNLOADS_CLEAR", "True")

PRIVATE_BOT_MODE = getenv("PRIVATE_BOT_MODE", None)

YOUTUBE_DOWNLOAD_EDIT_SLEEP = int(getenv("YOUTUBE_EDIT_SLEEP", "5"))
TELEGRAM_DOWNLOAD_EDIT_SLEEP = int(getenv("TELEGRAM_EDIT_SLEEP", "3"))

SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "f4c4aea1021549dbaf6b252d792473c9")
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", "98afbf53886b413299758e98665e4293")

VIDEO_STREAM_LIMIT = int(getenv("VIDEO_STREAM_LIMIT", "5"))
SERVER_PLAYLIST_LIMIT = int(getenv("SERVER_PLAYLIST_LIMIT", "50"))
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", "50"))

CLEANMODE_DELETE_MINS = int(getenv("CLEANMODE_MINS", "12"))

TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", "104857600"))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", "1073741824"))
# https://www.gbmb.org/mb-to-bytes

STRING1 = getenv("STRING_SESSION", "BQBODuL_S4IeRWVD7dgLFldSoGjmAQVop4suqToqcA3jufOBM0Pn40X4_tI0LieCEAHxh40sbEiAtaDxmIMj69QutqhdWmY066WZHzVSfKrWby75w0dXktuKVwDDtkHtha3iWzzv77ZLLpl8kqDYG9ka8jzStHYPwol6GX1sUBNBC-mrFfVWYuwl2LOeNDEdFCpyhwPFnGB2KUY2d_bEx0qrBj0yHsbhqMwhKJ169sqzI6BHn7Gm9iAcjQGwNpdw58gOORtGN8ThbSOXcUb8aO90xh5_jtdY4Q7zQoy9rYPkpwUjomcaCqliCEfqZcVSBRpBF0fYDq8pwtsV6D_VtydXAAAAAVwqO-sA")
STRING2 = getenv("STRING_SESSION2", "BQBDOpiJfRWUR_jheQXzvUJ2an80IeX_8tEF6nR0Oy_76ywYzTeS3ssASpMj6i_iIko1dTSADKVa3np5e3zcZIKf9RjVQfCXS6ZtEqhTtAVpmZl32B2TlGra97pfB0KpTd0ohuo-eCJ4Aydt2Iswvnt-gsXmxWTv2SL3L13dtJQAjNwixR9KgLbKoBPlYL05DADUaIJmbowgPsIhbyFw0Pn_I1nexy-Vf4vQRr9n5ErVq4XBcYfHndXt2v7oDNI-AjmrsV1I4QCTSdEHW2j2Msa_VxX57cV6g330B84pYlPPrI-28UAduVXBVRM1s2TLfGZbWjLhFPNpl4v_iokXteeWAAAAAXM7rskA")
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)

BANNED_USERS = filters.user()
YTDOWNLOADER = 1
LOG = 2
LOG_FILE_NAME = "logs.txt"
adminlist = {}
lyrical = {}
chatstats = {}
userstats = {}
clean = {}
autoclean = []


START_IMG_URL = getenv("START_IMG_URL", "https://telegra.ph/file/dfeeb825bbe2cccacb8b7.jpg")

PING_IMG_URL = getenv(
    "PING_IMG_URL",
    "https://telegra.ph/file/dfeeb825bbe2cccacb8b7.jpg",
)

PLAYLIST_IMG_URL = "https://telegra.ph/file/dfeeb825bbe2cccacb8b7.jpg"

GLOBAL_IMG_URL = "https://telegra.ph/file/dfeeb825bbe2cccacb8b7.jpg"

STATS_IMG_URL = "https://telegra.ph/file/dfeeb825bbe2cccacb8b7.jpg"

TELEGRAM_AUDIO_URL = "https://telegra.ph/file/dfeeb825bbe2cccacb8b7.jpg"

TELEGRAM_VIDEO_URL = "https://telegra.ph/file/dfeeb825bbe2cccacb8b7.jpg"

STREAM_IMG_URL = "https://telegra.ph/file/dfeeb825bbe2cccacb8b7.jpg"

SOUNCLOUD_IMG_URL = "https://telegra.ph/file/dfeeb825bbe2cccacb8b7.jpg"

YOUTUBE_IMG_URL = "https://telegra.ph/file/dfeeb825bbe2cccacb8b7.jpg"

SPOTIFY_ARTIST_IMG_URL = "https://telegra.ph/file/dfeeb825bbe2cccacb8b7.jpg"

SPOTIFY_ALBUM_IMG_URL = "https://telegra.ph/file/dfeeb825bbe2cccacb8b7.jpg"

SPOTIFY_PLAYLIST_IMG_URL = "https://telegra.ph/file/dfeeb825bbe2cccacb8b7.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(
        int(x) * 60**i
        for i, x in enumerate(reversed(stringt.split(":")))
    )


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))
SONG_DOWNLOAD_DURATION_LIMIT = int(
    time_to_seconds(f"{SONG_DOWNLOAD_DURATION}:00")
)


if UPSTREAM_REPO:
    if not re.match("(?:http|https)://", UPSTREAM_REPO):
        print(
            "[ERROR] - Your UPSTREAM_REPO url is wrong. Please ensure that it starts with https://"
        )
        sys.exit()

if PING_IMG_URL:
    if PING_IMG_URL != "assets/Ping.jpeg":
        if not re.match("(?:http|https)://", PING_IMG_URL):
            PING_IMG_URL = "https://telegra.ph/file/dfeeb825bbe2cccacb8b7.jpg"

if START_IMG_URL:
    if START_IMG_URL != "assets/Ping.jpeg":
        if not re.match("(?:http|https)://", START_IMG_URL):
            START_IMG_URL = "https://telegra.ph/file/dfeeb825bbe2cccacb8b7.jpg"
