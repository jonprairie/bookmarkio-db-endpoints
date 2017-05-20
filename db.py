"""database interface for bookmark.io"""

import sqlite3

table_definitions = {
    'users': "username TEXT PRIMARY KEY",
    'bookmarks': "username TEXT, name TEXT, url TEXT, description TEXT, PRIMARY KEY (username, name)"
}


def create_table(table):
    conn = sqlite3.connect('bookmark.db')
    try:
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
    conn = sqlite3.connect('bookmark.db')
    try:
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
