import sqlite3

def initialize():
    db = sqlite3.connect('database.db')
    db_cursor = db.cursor()
    db_cursor.execute('CREATE TABLE IF NOT EXISTS users(telegram_id INTEGER PRIMARY KEY, ombi_id TEXT, status INTEGER, name TEXT)')
    db_cursor.execute('CREATE TABLE IF NOT EXISTS shows(tvdb_id INTEGER PRIMARY KEY, name TEXT)')
    db_cursor.execute('CREATE TABLE IF NOT EXISTS movies(tmdb_id INTEGER PRIMARY KEY, name TEXT)')
    db_cursor.execute('CREATE TABLE IF NOT EXISTS notifications(notification_id INTEGER PRIMARY KEY, telegram_id INTEGER, media_id INTEGER, media_type INTEGER, desc TEXT, FOREIGN KEY(telegram_id) REFERENCES users ON DELETE CASCADE)')
    db.commit()
    db.close()