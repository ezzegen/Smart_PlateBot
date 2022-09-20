import sqlite3 as sq


def create_table_id(message):
    """Creating database with user's id"""
    connect = sq.connect('users.db')
    cursor = connect.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS user(login_id INT);''')
    connect.commit()

    user_id = message.chat.id
    cursor.execute(f'SELECT login_id FROM user WHERE login_id = {user_id};')
    data = cursor.fetchone()
    if data is None:
        user_id = [message.chat.id]
        cursor.execute('INSERT INTO user VALUES(?);', user_id)
        connect.commit()
