from pyrogram import Client, filters
from pytgcalls.types import MediaStream
from helpers.youtube import search_youtube
from helpers.spotify import resolve_spotify
from helpers.queue_manager import add_to_queue, get_queue, pop_queue
from helpers.language import get_strings, get_lang

async def play_next(client, tgcall, chat_id):
    song = pop_queue(chat_id)
    if not song:
        return
    s = get_strings(get_lang(chat_id))
    await tgcall.play(chat_id, MediaStream(song["url"]))
    await client.send_message(chat_id, s["play_now"].format(song["title"]))

def register_play(app, tgcall):

    @app.on_message(filters.command("play") & filters.group)
    async def play(client, msg):
        query = " ".join(msg.command[1:])
        s = get_strings(get_lang(msg.chat.id))
        if not query:
            return await msg.reply("Usage: /play <song name or link>")

        status = await msg.reply(s["play_searching"])
        try:
            if "spotify.com" in query:
                resolved = resolve_spotify(query)
                if isinstance(resolved, list):
                    for q in resolved:
                        url, title = search_youtube(q)
                        add_to_queue(msg.chat.id, url, title)
                    await status.edit(f"Added {len(resolved)} songs from Spotify playlist!")
                else:
                    url, title = search_youtube(resolved)
                    add_to_queue(msg.chat.id, url, title)
                    await status.edit(s["play_added"].format(title))
            else:
                url, title = search_youtube(query)
                add_to_queue(msg.chat.id, url, title)
                await status.edit(s["play_added"].format(title))
        except Exception:
            return await status.edit(s["not_found"])

        if len(get_queue(msg.chat.id)) == 1:
            await play_next(client, tgcall, msg.chat.id)

    @tgcall.on_stream_end()
    async def on_end(_, update):
        await play_next(app, tgcall, update.chat_id)
