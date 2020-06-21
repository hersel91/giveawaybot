import core.decorators
from core.sql.db_connect import Connection
from core.sql.commands_sql import SQL_Rand

@core.decorators.admin.init
def init(update,context):
    bot = context.bot
    connector = Connection()
    query = SQL_Rand.SQL
    connector.cur.execute(query)
    row = connector.cur.fetchone()
    if row is not None:
        message = "<b>The winner is:</b>\nUser_Id: <code>{}</code>\nNickname: {}".format(row[1],row[2])
        bot.send_message(update.message.chat_id, text=message, parse_mode='HTML')
    else:
        bot.send_message(update.message.chat_id, text="No users in list!")