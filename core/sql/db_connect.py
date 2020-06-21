from config import Config
import MySQLdb

class Connection:
    def __init__(self):
        self.db=MySQLdb.connect(
            Config.DATABASE_CONFIG['server'],
            Config.DATABASE_CONFIG['user'],
            Config.DATABASE_CONFIG['password'],
            Config.DATABASE_CONFIG['name']
            )
        self.db.autocommit(True)
        self.db.set_character_set('utf8mb4')
        self.cur=self.db.cursor()