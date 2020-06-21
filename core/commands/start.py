import core.decorators
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from core.sql.db_connect import Connection
from core.sql.commands_sql import SQL_Select_ON_OFF
from core.sql.commands_sql import SQL_Select_text

@core.decorators.private_chat.init
def init(update, context):
    connector = Connection()
    query = SQL_Select_ON_OFF.SQL
    connector.cur.execute(query)
    res = connector.cur.fetchone()
    if res is not None:
        textconnector = Connection()
        query_text = SQL_Select_text.SQL
        textconnector.cur.execute(query_text)
        row = textconnector.cur.fetchone()
        main_text = "{}".format(row[2])
        button_text = "{}".format(row[3])
        keyboard = [[InlineKeyboardButton(button_text, callback_data='participate')]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        update.message.reply_text(main_text,reply_markup=reply_markup,parse_mode='HTML')

@core.decorators.save_user.init
def participate(update, context):
    query = update.callback_query
    query.edit_message_text(text="<b>Thank you for participate: @{username}, Good Luck!</b>"
    .format(username=str(update.effective_user.username or update.effective_user.first_name)),parse_mode='HTML')