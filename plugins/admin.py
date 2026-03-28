from pyrogram import filters
from config import ADMINS
from helpers.queue_manager import clear_queue, queue_list
from helpers.language import get_strings, get_lang

def register_admin(app, tgcall):

    def is_admin(user_id):
        return user_id in ADMINS

    @app.on_message(filters.command("skip") & filters.group)
    async def skip(client, msg):
        s = get_strings(get_lang(msg.chat.id))
        if not is_admin(msg.from_user.id):
            return await msg.reply(s["admins_only"])
        await tgcall.leave_call(msg.chat.id)
        from plugins.play import play_next
        await play_next(client, tgcall, msg.chat.id)
        await msg.reply(s["skip_done"])

    @app.on_message(filters.command("pause") & filters.group)
    async def pause(client, msg):
        s = get_strings(get_lang(msg.chat.id))
        if not is_admin(msg.from_user.id):
            return await msg.reply(s["admins_only"])
        await tgcall.pause_stream(msg.chat.id)
        await msg.reply(s["pause_done"])

    @app.on_message(filters.command("resume") & filters.group)
    async def resume(client, msg):
        s = get_strings(get_lang(msg.chat.id))
        if not is_admin(msg.from_user.id):
            return await msg.reply(s["admins_only"])
        await tgcall.resume_stream(msg.chat.id)
        await msg.reply(s["resume_done"])

    @app.on_message(filters.command("stop") & filters.group)
    async def stop(client, msg):
        s = get_strings(get_lang(msg.chat.id))
        if not is_admin(msg.from_user.id):
            return await msg.reply(s["admins_only"])
        clear_queue(msg.chat.id)
        await tgcall.leave_call(msg.chat.id)
        await msg.reply(s["stop_done"])

    @app.on_message(filters.command("queue") & filters.group)
    async def show_queue(client, msg):
        s = get_strings(get_lang(msg.chat.id))
        songs = queue_list(msg.chat.id)
        if not songs:
            return await msg.reply(s["queue_empty"])
        text = "📋 Upcoming:\n"
        for i, song in enumerate(songs, 1):
            text += f"{i}. {song['title']}\n"
        await msg.reply(text)
