import sqlite3

DATABASE = 'database.db'

def create_todos_table():
    con = sqlite3.connect(DATABASE)
    con.execute("CREATE TABLE IF NOT EXISTS todos (id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT, detail TEXT, due TEXT)")
    con.close()