import core.decorators
from core.sql.db_connect import Connection
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from core.sql.commands_sql import SQL_Config

####################  CLOSED OR OPENED THE GIVEAWAY#####################
@core.decorators.admin.init
def init(update,context):
    keyboard = [[InlineKeyboardButton("Start", callback_data='ON'),
                InlineKeyboardButton("Closed", callback_data='OFF')]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text(text="Do you want to start a new giveaway?\nRemember to erase the database with /refresh",
    reply_markup=reply_markup)

@core.decorators.admin.init
def ON(update,context):
    query = update.callback_query
    connector = Connection()
    sql = SQL_Config.SQL_ON
    connector.cur.execute(sql)
    query.edit_message_text(text="<b>Giveaway Open</b>",parse_mode='HTML')

@core.decorators.admin.init
def OFF(update,context):
    query = update.callback_query
    connector = Connection()
    sql = SQL_Config.SQL_OFF
    connector.cur.execute(sql)
    query.edit_message_text(text="<b>Giveaway Closed</b>",parse_mode='HTML')

### EDIT MAIN TEXT AND BUTTON_TEXT VIA DATABASE ###
@core.decorators.admin.init
def update_main_text(update,context):
    bot = context.bot
    connector = Connection()
    message = str(update.message.text[8:])
    if message != "":
        query = SQL_Config.SQL_UPDATE_MT
        connector.cur.execute(query,[message])
        connector.db.commit()
        bot.send_message(update.message.chat_id, text="You succesfully inserted the main text")
    else:
        bot.send_message(update.message.chat_id, text="You can't insert an empty message!")

@core.decorators.admin.init
def update_button_text(update,context):
    bot = context.bot
    connector = Connection()
    message = str(update.message.text[10:])
    if message != "":
        query = SQL_Config.SQL_UPDATE_BT
        connector.cur.execute(query,[message])
        connector.db.commit()
        bot.send_message(update.message.chat_id, text="You succesfully inserted the button text")
    else:
        bot.send_message(update.message.chat_id, text="You can't insert an empty message!")