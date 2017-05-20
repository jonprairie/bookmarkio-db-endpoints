"""database interface for bookmark.io"""

import sqlite3


def create_user_table():
    conn = sqlite3.connect('bookmark.db')
    try:
        c = conn.cursor()
        c.execute('CREATE TABLE users (username TEXT PRIMARY KEY)')
        conn.commit()
    except:
        print('could not create users table')
        raise
    finally:
        conn.close()


def drop_user_table():
    conn = sqlite3.connect('bookmark.db')
    try:
        c = conn.cursor()
        c.execute('DROP TABLE users')
        conn.commit()
    except:
        print('could not drop users table')
        raise
    finally:
        conn.close()
    

def reset_user_table():
    try:
        drop_user_table()
        create_user_table()
        return True
    except:
        return False
    

def add_user(username):
    try:
        conn = sqlite3.connect('bookmark.db')
        c = conn.cursor()
        c.execute('INSERT INTO users VALUES (?)', [username])
        conn.commit()
        return True
    except:
        return False
    finally:
        conn.close()

def get_user(username):
    try:
        conn = sqlite3.connect('bookmark.db')
        c = conn.cursor()
        c.execute('SELECT username FROM users WHERE username = ?', [username])
        return c.fetchone()[0]
    except:
        return False
    finally:
        conn.close()
