import sqlite3 as sq
from create_bot import bot


def sql_start():
    """Creating database for 'menu'"""
    global base, cur
    base = sq.connect('smart_plate.db')
    cur = base.cursor()
    if base:
        print('DB connected OK')
    base.execute('CREATE TABLE IF NOT EXISTS menu(img TEXT, name TEXT PRIMARY KEY, description TEXT, price TEXT);')
    base.commit()


async def sql_add_command(state):
    """Writing the received data to the table"""
    async with state.proxy() as data:
        cur.execute('INSERT INTO menu VALUES(?, ?, ?, ?);', tuple(data.values()))
        base.commit()


async def sql_read(message):
    """Reading data for menu"""
    for r in cur.execute('SELECT * FROM menu;').fetchall():
        await bot.send_photo(message.from_user.id, r[0],
                             f'{r[1]}\nОписание: {r[2]}\n'
                             f'Цена {r[-1]} руб.')


async def sql_read2():
    return cur.execute('SELECT * FROM menu;').fetchall()


async def sql_delete(data):
    """deleting data from the database"""
    cur.execute('DELETE FROM menu WHERE name is ? ', (data,))
    base.commit()
