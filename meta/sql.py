import sqlite3

connection = sqlite3.connect("../backends/database.db")

crsr = connection.cursor()

def get_users():
    sql_query = """
    SELECT name, timestamp, points, email FROM USER        
    """
    crsr.execute(sql_query)
    ans = crsr.fetchall()
    return ans

def get_blogs():
    sql_query = """
    SELECT * FROM BLOG
    """
    crsr.execute(sql_query)
    ans = crsr.fetchall()
    return ans

get_users()
