import os

API_ID           = int(os.environ.get("API_ID", 0))
API_HASH         = os.environ.get("API_HASH", "")
BOT_TOKEN        = os.environ.get("BOT_TOKEN", "")
SESSION_STRING   = os.environ.get("SESSION_STRING", "")
ADMINS           = list(map(int, os.environ.get("ADMINS", "0").split()))
SPOTIFY_ID       = os.environ.get("SPOTIFY_CLIENT_ID", "")
SPOTIFY_SECRET   = os.environ.get("SPOTIFY_CLIENT_SECRET", "")
DEFAULT_LANGUAGE = os.environ.get("LANGUAGE", "en")
GENIUS_TOKEN     = os.environ.get("GENIUS_TOKEN", "")
