import sqlite3

connection = sqlite3.connect("./hack.db")

crsr = connection.cursor()

def check_if_databse_has_data():
    sql_query = """SELECT COUNT(DISTINCT `table_name`) FROM `information_schema`.`columns` WHERE `table_schema` = 'hack'"""
    try:
        crsr.execute(sql_query)
        ans = crsr.fetchall()
        return ans
    except:
        return 0

def create_and_write_tables():
    sql_statement = """
    CREATE TABLE user()  
    
    """

print(check_if_databse_has_data())