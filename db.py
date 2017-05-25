"""database interface for bookmark.io"""

import sqlite3
from collections import OrderedDict

db_name = 'bookmark.db'

table_definitions = OrderedDict({
    'users': "username TEXT NOT NULL PRIMARY KEY",
    'bookmarks': "username TEXT NOT NULL, name TEXT NOT NULL, url TEXT NOT NULL, description TEXT, PRIMARY KEY (username, name), FOREIGN KEY(username) REFERENCES users(username)" 
})

def connect_db():
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    c.execute("PRAGMA foreign_keys = ON;")
    return conn

def create_table(table):
    try:
        conn = connect_db()
        c = conn.cursor()
        table_def = table_definitions[table]
        c.execute('CREATE TABLE %s (%s)' % (table, table_def))
        conn.commit()
    except:
        print('could not create table: %s' % table)
        raise
    finally:
        conn.close()


def drop_table(table):
    try:
        conn = connect_db()
        c = conn.cursor()
        c.execute('DROP TABLE %s' % table)
        conn.commit()
    except:
        print('could not drop table: %s' % table)
        raise
    finally:
        conn.close()
    

def reset_table(table):
    try:
        drop_table(table)
        create_table(table)
        return True
    except:
        return False
    

def reset_db():
    for table in table_definitions.keys():
        try:
            reset_table(table)
        except:
            print('could not reset table: %s' % table)
            raise


def dump_table(table):
    try:
        conn = connect_db()
        c = conn.cursor()
        c.execute('SELECT * FROM %s' % table)
        return list(c.fetchall())
    except:
        print('could not dump table')
        raise
    finally:
        conn.close()


def add_user(username):
    try:
        conn = connect_db()
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
        conn = connect_db()
        c = conn.cursor()
        c.execute('SELECT username FROM users WHERE username = ?', [username])
        return c.fetchone()[0]
    except:
        return False
    finally:
        conn.close()

def add_bookmark(username, name, url, description):
    try:
        conn = connect_db()
        c = conn.cursor()
        c.execute(
            'INSERT INTO bookmarks VALUES (?, ?, ?, ?)',
            (username, name, url, description)
        )
        conn.commit()
        return True
    except:
        return False
    finally:
        conn.close()

def get_bookmarks(username):
    try:
        conn = connect_db()
        conn.row_factory = sqlite3.Row
        c = conn.cursor()
        c.execute('SELECT * FROM bookmarks WHERE username = ?', [username])
        return list(map(dict, c.fetchall()))
    except:
        return False
    finally:
        conn.close()
