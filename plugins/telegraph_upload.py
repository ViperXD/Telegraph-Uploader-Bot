import os
from telegraph import upload_file
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton 
from pyrogram.errors import UserNotParticipant, UserBannedInChannel
from translation import Translation 
from vars import Config

@Client.on_message(filters.media & filters.private)
async def getmedia(client, message):
    if Config.UPDATE_CHANNEL:
        try:
          user = await bot.get_chat_member(Config.UPDATE_CHANNEL, update.chat.id)
          if user.status == "kicked":
            await update.reply_text(text=Translation.BANNED_USER_TEXT)
            return
        except UserNotParticipant:
          await update.reply_text(text=Translation.FORCE_SUBSCRIBE_TEXT, reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(text="😎 Join Channel 😎", url=f"https://telegram.me/{Config.UPDATE_CHANNEL}")]]))
          return
        except Exception:
          await update.reply_text(text=Translation.SOMETHING_WRONG)
          return
        if update.from_user.id in Config.ADL_BOT_RQ:
          if update.from_user.id not in Config.AUTH_USERS:
            current_time = time.time()
            previous_time = Config.ADL_BOT_RQ[str(update.from_user.id)]
            process_max_timeout = round(Config.PROCESS_MAX_TIMEOUT/60)
            present_time = round(Config.PROCESS_MAX_TIMEOUT-(current_time - previous_time))
            Config.ADL_BOT_RQ[str(update.from_user.id)] = time.time()
            if round(current_time - previous_time) < Config.PROCESS_MAX_TIMEOUT:
                await bot.send_message(text=Translation.FREE_USER_LIMIT_Q_SZE.format(process_max_timeout, present_time), quote=True)
                return
        else:
            Config.ADL_BOT_RQ[str(update.from_user.id)] = time.time()
    medianame = "FNPROJECTS/FnTelegraphBot"
    dwn = await client.send_message(chat_id = message.chat.id, text=Translation.DOWNLOAD_TEXT, parse_mode="html", disable_web_page_preview=True, reply_to_message_id=message.message_id)
    await client.download_media(message=message, file_name=medianame)
    await dwn.edit_text(text=Translation.UPLOADING_TEXT)
    try:
        response = upload_file(medianame)
    except Exception as error:
        await dwn.edit_text(text=Translation.SOMETHING_WRONG, reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("❔ More Help ❔", callback_data="help")]]))
        return
    await dwn.edit_text(
        text=f"<b>Link :-</b> <code>https://telegra.ph{response[0]}</code>\n\n<b>Join :-</b> @FNPROJECTS",
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(text="Open Link", url=f"https://telegra.ph{response[0]}"), InlineKeyboardButton(text="Share Link", url=f"https://telegram.me/share/url?url=https://telegra.ph{response[0]}"), ],
                                           [InlineKeyboardButton(text="⚙ Join Channel ⚙", url="https://telegram.me/FNPROJECTS")]])
        )
    try:
        os.remove(medianame)
    except:
        pass
