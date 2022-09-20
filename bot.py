import logging
from aiogram.utils import executor
from create_bot import dp
from data_base import sql_db_menu
from handlers import client, admin, other

logging.basicConfig(level=logging.INFO)


async def on_startup(_):
    print('Бот вышел в онлайн')
    sql_db_menu.sql_start()


client.register_handlers_client(dp)
admin.register_handlers_admin(dp)
other.register_handlers_other(dp)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
