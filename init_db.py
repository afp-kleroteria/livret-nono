import sqlite3

DATABASE= './livret.db'

def get_db():
    return sqlite3.connect(DATABASE)



def init_db():
    db= get_db()
    f = open("schema.sql", "r")
    db.cursor().executescript(f.read())
    db.commit()
    db.close()
    return True
init_db()