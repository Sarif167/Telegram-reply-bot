from telethon import TelegramClient, events
from config import API_ID, API_HASH, SESSION_NAME, GROUP_IDS
import asyncio
import random

client = TelegramClient(SESSION_NAME, API_ID, API_HASH)

MIN_DELAY = 2
MAX_DELAY = 5

@client.on(events.NewMessage)
async def auto_reply(event):

    if event.chat_id not in GROUP_IDS:
        return

    sender = await event.get_sender()

    if sender.is_self:
        return

    text = event.raw_text.lower()

    await asyncio.sleep(random.randint(MIN_DELAY, MAX_DELAY))

    if "hi" in text:
        await event.reply("Hello 👋 Kaise ho?")
    elif "link" in text:
        await event.reply("Link ke liye admin se contact karo 😊")
    elif "admin" in text:
        await event.reply("Admin busy hai 😄")
    else:
        await event.reply("Message receive ho gaya ✅")

print("UserBot Running in Multiple Groups...")
client.start()
client.run_until_disconnected()
from aiohttp import web
import os
import asyncio

# ---- EXISTING BOT CODE RUN ----
async def start_bot():
    # yaha tumhara existing bot start code already hai
    # agar already run ho raha hai to isko empty chhod do
    pass


# ---- WEB SERVER ----
async def handle(request):
    return web.Response(text="Bot is running")

async def start_web():
    app = web.Application()
    app.router.add_get('/', handle)

    port = int(os.environ.get("PORT", 8000))
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, "0.0.0.0", port)
    await site.start()


# ---- MAIN RUNNER ----
async def main():
    await asyncio.gather(
        start_bot(),   # bot run karega
        start_web()    # web server run karega
    )

if __name__ == "__main__":
    asyncio.run(main())
    
