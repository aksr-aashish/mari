import html
import random
import time

from telegram import ParseMode, Update, ChatPermissions
from telegram.ext import CallbackContext, run_async
from telegram.error import BadRequest

import AsunaRobot.modules.memes_strings as memes_strings
from AsunaRobot import dispatcher
from AsunaRobot.modules.disable import DisableAbleCommandHandler
from AsunaRobot.modules.helper_funcs.chat_status import (is_user_admin)
from AsunaRobot.modules.helper_funcs.extraction import extract_user

@run_async
def imgquotes(update: Update, context: CallbackContext):
    message = update.effective_message
    name = message.reply_to_message.from_user.first_name if message.reply_to_message else message.from_user.first_name
    reply_photo = message.reply_to_message.reply_photo if message.reply_to_message else message.reply_photo
    reply_photo(
        random.choice(memes_strings.MEMES_IMG))

__help__ = """
 • `/imgquotes`*:* for anime images quotes.

 
"""
IMGQUOTES_HANDLER = DisableAbleCommandHandler("imgquotes",imgquotes)

dispatcher.add_handler(IMGQUOTES_HANDLER)

__mod_name__ = "Imgquotes"
__command_list__ = [
    "imgquotes"
]
__handlers__ = [
    IMGQUOTES_HANDLER
]
