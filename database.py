import sqlite3

def connect():
    conn = sqlite3.connect('application.db')
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS routine (Id INTEGER PRIMARY KEY , date text , earning integer , exercise text, study text, diet text, python text)") #DROP TABLE routine
    conn.commit()
    conn.close()

def insert(date, earning, exercise, study, diet, python):
    conn = sqlite3.connect('application.db')
    cur = conn.cursor()
    cur.execute("INSERT INTO routine VALUES (NULL,?,?,?,?,?,?)",(date, earning, exercise, study, diet, python)) #DROP TABLE routine
    conn.commit()
    conn.close()

def view():
    conn = sqlite3.connect('application.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM routine") #DROP TABLE routine
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    return rows


def delete(id):
    conn = sqlite3.connect('application.db')
    cur = conn.cursor()
    cur.execute("DELETE FROM routine WHERE (id=?)",(id,)) #DROP TABLE routine     Li9 virgule mor id (-_-)
    conn.commit()
    conn.close()

def search(date='', earning='', exercise='', study='', diet='', python=''):
    conn = sqlite3.connect('application.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM routine WHERE date=? OR earning=? OR exercise=? OR study=? OR diet=? OR python=?",(date, earning, exercise, study, diet, python))  # DROP TABLE routine
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    return rows

connect()
#insert('15-10-2020',200, 'did exercise', 'no studied', 'diet taken', 'did python')
#print(view())
#delete(2)
#print(search(earning=200))