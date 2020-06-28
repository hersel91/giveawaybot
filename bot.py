#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import sys
from datetime import datetime
# Import telegram library
from telegram.ext import (
    Updater,
    CommandHandler as CMH,
    MessageHandler as MH,
    CallbackQueryHandler as CQH)
# Import local files 
from config import Config
from core import commands

# if version < 3.6, stop bot.
LOGGER = logging.getLogger(__name__)
if sys.version_info[0] < 3 or sys.version_info[1] < 6:
    LOGGER.error("You MUST have a python version of at least 3.6! Multiple features depend on this. Bot quitting.")
    quit(1)

timestamp = datetime.strftime(datetime.today(), '%H:%M at %Y/%m/%d')
print("Start Bot {}".format(timestamp))


# This enables the logs
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

def error(update, context):
    logger.warning('Update "%s" Error is: "%s"', update, context.error)

# This is the function that initializes the bot
def main():
    updater = Updater(Config.BOT_API, use_context=True)
    dp = updater.dispatcher
    FUNCTION = dp.add_handler
    
    # Creater a command and generate a function
    FUNCTION(CMH("start", commands.start.init))
    FUNCTION(CMH("config", commands.config_bot.init))
    FUNCTION(CMH("setmain", commands.config_bot.update_main_text))
    FUNCTION(CMH("setbutton", commands.config_bot.update_button_text))
    FUNCTION(CMH("result", commands.result.init))
    FUNCTION(CMH("refresh", commands.refresh.init))
    FUNCTION(CMH("list", commands.list.init))
    
   
    #CallBackQuery Handler
    FUNCTION(CQH(commands.start.participate, pattern='participate'))
    FUNCTION(CQH(commands.config_bot.ON, pattern='ON'))
    FUNCTION(CQH(commands.config_bot.OFF, pattern='OFF'))
    
    dp.add_error_handler(error)
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()