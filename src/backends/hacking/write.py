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
        create_and_write_tables()

def create_and_write_tables():
    sql_statement = """
    CREATE TABLE user(
        id INT AUTO_INCREMENT PRIMARY KEY,
        email VARCHAR(65),
        password VARCHAR(60),
        name VARCHAR(40)
    )  
    
    """
    crsr.execute(sql_statement)
    ans = crsr.fetchall()
    print(ans)

def insert_into_databse(name, email, password):
    sql_statement = """
    INSERT INTO user (email, password, name) VALUES (email, password, name)
    """

    crsr.execute(sql_statement)
    ans = crsr.fetchall()
    print(ans)
