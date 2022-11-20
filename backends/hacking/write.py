import sqlite3

connection = sqlite3.connect("./hack.db")

crsr = connection.cursor()

def check_if_databse_has_data():
    sql_query = """USE hack SHOW tables"""

    crsr.execute(sql_query)
    ans = crsr.fetchall()
    return ans

print(check_if_databse_has_data())