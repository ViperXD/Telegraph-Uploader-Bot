from pyrogram import Client
from vars import Config

plugins = dict(
        root="plugins"
    )
bot = Client(
    "Telegraph Uploader Bot",
    bot_token = Config.BOT_TOKEN,
    api_id = Config.API_ID,
    api_hash = Config.API_HASH,
    plugins = plugins
)
bot.run()
