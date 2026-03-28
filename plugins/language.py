from pyrogram import filters
from helpers.language import set_lang

SUPPORTED = {"en": "English", "ta": "Tamil"}

def register_language(app):

    @app.on_message(filters.command("setlang") & filters.group)
    async def setlang(client, msg):
        args = msg.command
        if len(args) < 2 or args[1] not in SUPPORTED:
            langs = ", ".join(f"`{k}` ({v})" for k, v in SUPPORTED.items())
            return await msg.reply(f"Available: {langs}\nUsage: /setlang en")
        set_lang(msg.chat.id, args[1])
        await msg.reply(f"Language set to {SUPPORTED[args[1]]}!")
