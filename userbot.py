import os
from flask import Flask
from telethon import TelegramClient

# ===== CONFIG =====
API_ID = int(os.getenv("API_ID", "123456"))
API_HASH = os.getenv("API_HASH", "your_api_hash")
SESSION = os.getenv("SESSION", "userbot")

# ===== TELEGRAM CLIENT =====
client = TelegramClient(SESSION, API_ID, API_HASH)

# ===== START BOT =====
async def start_bot():
    await client.start()
    print("✅ UserBot Running in Multiple Groups...")
    await client.run_until_disconnected()

# ===== FLASK SERVER =====
app = Flask(__name__)

@app.route("/")
def home():
    return "Bot is running ✅"

# ===== MAIN =====
if __name__ == "__main__":
    import threading

    threading.Thread(
        target=lambda: client.loop.run_until_complete(start_bot())
    ).start()

    port = int(os.environ.get("PORT", 8000))
    app.run(host="0.0.0.0", port=port)
