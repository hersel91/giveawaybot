from functools import wraps
from core.sql.db_connect import Connection

def init(func):
    @wraps(func)
    def wrapped(update, context):
        connector = Connection()
        user_id = str(update.effective_user.id)
        user_username = "@"+str(update.effective_user.username)
        query = "INSERT IGNORE INTO users(user_id, user_nickname) VALUES (%s,%s)"
        connector.cur.execute(query,[user_id,user_username])
        return func(update, context)
    return wrapped