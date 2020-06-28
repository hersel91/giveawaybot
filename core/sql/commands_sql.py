class SQL_Select_ON_OFF:
    SQL = "SELECT * FROM config_table WHERE switch"
class SQL_Select_text:
    SQL = "SELECT * FROM config_table"
class SQL_Rand:
    SQL = "SELECT * FROM users ORDER BY RAND() LIMIT 1"
class SQL_Config:
    SQL_ON = "UPDATE config_table SET switch = 1 WHERE ID=1"
    SQL_OFF = "UPDATE config_table SET switch = 0 WHERE ID=1"
    SQL_UPDATE_MT = "UPDATE config_table SET main_text = %s WHERE ID=1"
    SQL_UPDATE_BT = "UPDATE config_table SET button_text = %s WHERE ID=1"
class SQL_Refresh:
    SQL = "DELETE FROM users"
class SQL_List:
    SQL = "SELECT * FROM users"