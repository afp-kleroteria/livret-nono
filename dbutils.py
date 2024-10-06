import sqlite3

DATABASE= './livret.db'

def get_db():
    return sqlite3.connect(DATABASE)


def get_category():
    db= get_db()
    category_liste=db.cursor().execute("SELECT * FROM category ORDER BY category_order").fetchall()
    
    db.close()
    return category_liste

toto=get_category()
for i in toto:
    print (i)



