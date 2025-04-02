from pyrogram.raw import functions, types
from pyrogram import Client, idle
from config import Config

bot = Client(
    "bot",
    bot_token=Config.BOT_TOKEN,
    api_id=Config.23556070,
    api_hash=Config.83179ee32ab99592bf173238a72ca7f4,
    workers=50,
    plugins=dict(root="plugins")
)
bot.start()
print("Bot Started ⚡")
idle()
bot.stop()
