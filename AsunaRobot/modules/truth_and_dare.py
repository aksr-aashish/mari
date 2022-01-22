import html
import random
import requests

import AsunaRobot.modules.truth_and_dare_string as fun
from AsunaRobot import dispatcher
from AsunaRobot import telethn
from AsunaRobot.modules.helper_funcs.chat_status import is_user_admin
from AsunaRobot.modules.helper_funcs.extraction import extract_user
from telegram import ParseMode, Update
from AsunaRobot.modules.helper_funcs.alternate import typing_action
from AsunaRobot import ubot2 as ubot
from telethon.tl.types import InputMessagesFilterPhotos
from AsunaRobot.modules.disable import DisableAbleCommandHandler
from telegram.ext import CallbackContext, run_async
from AsunaRobot.events import register as komi
from AsunaRobot.modules.helper_funcs.chat_status import (is_user_admin)
from AsunaRobot.modules.helper_funcs.extraction import extract_user




def truth(update: Update, context: CallbackContext):
    update.effective_message.reply_text(random.choice(fun.TRUTH))


def dare(update: Update, context: CallbackContext):
    update.effective_message.reply_text(random.choice(fun.DARE))
    

def sigma(update: Update, context: CallbackContext):
    update.effective_message.reply_video(random.choice(fun.SIGMA))

@typing_action
def simp(update, context):
    # reply to correct message
    reply_text = (
        update.effective_message.reply_to_message.reply_text
        if update.effective_message.reply_to_message
        else update.effective_message.reply_text
    )
    reply_text(random.choice(fun.SIMP))
    

def meme(update: Update, context: CallbackContext):
    msg = update.effective_message
    meme = requests.get("https://meme-api.herokuapp.com/gimme/Animemes/").json()
    image = meme.get("url")
    caption = meme.get("title")
    if not image:
        msg.reply_text("No URL was received from the API!")
        return
    msg.reply_photo(
                photo=image, caption=caption)
    
    
@komi(pattern="^/kmeme ?(.*)")
async def memes(event):
    pics = []
    async for i in ubot.iter_messages(
        "@komimemes", filter=InputMessagesFilterPhotos
        ):
        pics.append(i)

    komimeme = random.choice(pics)
    await event.reply(komimeme)

    

    
TRUTH_HANDLER = DisableAbleCommandHandler("truth", truth, run_async=True)
DARE_HANDLER = DisableAbleCommandHandler("dare", dare, run_async=True)
SIGMA_HANDLER = DisableAbleCommandHandler("sigma", sigma, run_async=True)
SIMP_HANDLER = DisableAbleCommandHandler("simp", simp, run_async=True)
MEME_HANDLER = DisableAbleCommandHandler("meme", meme, run_async=True)

dispatcher.add_handler(TRUTH_HANDLER)
dispatcher.add_handler(DARE_HANDLER)
dispatcher.add_handler(SIMP_HANDLER)
dispatcher.add_handler(SIGMA_HANDLER)
dispatcher.add_handler(MEME_HANDLER)



__mod_name__ = "「FUN RULES」"

__help__ = """
 - `/truth` : for a truth
 - `/dare` : for a dare
"""
