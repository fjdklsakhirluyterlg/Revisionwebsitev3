import sqlite3

connection = sqlite3.connect("./hack.db")

crsr = connection.cursor()

def check_if_databse_has_data():
    sql_query = """SELECT COUNT(DISTINCT `table_name`) FROM `information_schema`.`columns` WHERE `table_schema` = 'hack'"""

    crsr.execute(sql_query)
    ans = crsr.fetchall()
    return ans

print(check_if_databse_has_data())