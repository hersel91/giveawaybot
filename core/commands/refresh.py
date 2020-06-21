import core.decorators
from core.sql.db_connect import Connection
from core.sql.commands_sql import SQL_Refresh

@core.decorators.admin.init
def init(update, context):
    bot = context.bot
    connector = Connection()
    query = SQL_Refresh.SQL
    connector.cur.execute(query)
    if connector.cur.rowcount == 0:
        bot.send_message(update.message.chat_id, text="Database is empty!")
    else:
        bot.send_message(update.message.chat_id, text="You succesfully refresh the database")