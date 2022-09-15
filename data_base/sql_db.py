import sqlite3 as sq


def sql_start():
    """Creating data base for 'menu'"""
    global base, cur
    base = sq.connect('smart_plate.db')
    cur = base.cursor()
    if base:
        print('DB connected OK')
    base.execute('CREATE TABLE IF NOT EXISTS menu(img TEXT, name TEXT PRIMARY KEY, description TEXT, price TEXT)')
    base.commit()


async def sql_add_command(state):
    async with state.proxy() as data:
        cur.execute('INSERT INTO menu VALUES(?, ?, ?, ?)', tuple(data.values()))
        base.commit()
