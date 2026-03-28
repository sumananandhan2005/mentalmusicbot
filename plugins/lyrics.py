import requests
from pyrogram import filters
from config import GENIUS_TOKEN

def register_lyrics(app):

    @app.on_message(filters.command("lyrics") & filters.group)
    async def lyrics(client, msg):
        query = " ".join(msg.command[1:])
        if not query:
            return await msg.reply("Usage: /lyrics <song name>")
        status = await msg.reply("Looking up lyrics...")
        try:
            headers = {"Authorization": f"Bearer {GENIUS_TOKEN}"}
            r = requests.get(
                "https://api.genius.com/search",
                params={"q": query},
                headers=headers
            )
            hits = r.json().get("response", {}).get("hits", [])
            if not hits:
                return await status.edit("Lyrics not found.")
            song = hits[0]["result"]
            await status.edit(
                f"**{song['full_title']}**\n\nFull lyrics: {song['url']}"
            )
        except Exception:
            await status.edit("Something went wrong fetching lyrics.")
