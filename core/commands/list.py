import core.decorators
from core.sql.db_connect import Connection
from core.sql.commands_sql import SQL_List

@core.decorators.admin.init
def init(update, context):
    connector = Connection()
    query = SQL_List.SQL
    connector.cur.execute(query)
    rows = connector.cur.fetchall()
    string = ""
    for link in rows:
        string += f"<code>ID {link[0]}:</code> <a href=\"{link[2]}\">{link[2]}</a>\n"
    message = "GIVEAWAY LIST:"
    update.effective_message.reply_html(message + "\n\nParticipants List:\n" + string)