from server import keep_alive
keep_alive()

from pyrogram import Client
from pytgcalls import PyTgCalls
from config import API_ID, API_HASH, BOT_TOKEN
from plugins.play import register_play
from plugins.admin import register_admin
from plugins.lyrics import register_lyrics
from plugins.language import register_language

app    = Client("music_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)
tgcall = PyTgCalls(app)

register_play(app, tgcall)
register_admin(app, tgcall)
register_lyrics(app)
register_language(app)

tgcall.start()
app.run()
```

---
