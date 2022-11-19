import sqlite3

connection = sqlite3.connect("../backends/database.db")

crsr = connection.cursor()

def get_users():
    sql_query = """
    SELECT * FROM USER        
    """
    crsr.execute(sql_query)