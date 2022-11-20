import sqlite3

connection = sqlite3.connect("./hack.db")

crsr = connection.cursor()

def check_if_databse_has_data():
    sql_query = """SELECT COUNT(DISTINCT `TABLE_NAME`) AS anyAliasName FROM `INFORMATION_SCHEMA`.`COLUMNS` WHERE `table_schema` = 'hack'"""

    crsr.execute(sql_query)
    ans = crsr.fetchall()
    return ans