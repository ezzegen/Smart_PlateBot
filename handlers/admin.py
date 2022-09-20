from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Text
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from create_bot import bot, dp
from keyboards import kb_adm, kb_adm_cancel
from data_base import sql_db_menu
from handlers.admin_id import adm


class FSMAdmin(StatesGroup):
    photo = State()
    name = State()
    description = State()
    price = State()


async def make_changes_command(message: types.Message):
    """ determining id of the current moderator"""
    if message.from_user.id in adm:
        await bot.send_message(message.from_user.id, 'Чем могу помочь, уважаемый администратор?',
                               reply_markup=kb_adm)
        await message.delete()


async def start_fsm(message: types.Message):
    """starting to enter data in the menu"""
    if message.from_user.id in adm:
        await FSMAdmin.photo.set()
        await message.reply('Загрузите фото.', reply_markup=kb_adm_cancel)


async def cancel_handler(message: types.Message, state: FSMContext):
    """ forsed stop """
    current_state = await state.get_state()
    if current_state is None:
        return
    await state.finish()
    await message.reply('Ok', reply_markup=kb_adm)


async def load_photo(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['photo'] = message.photo[0].file_id
    await FSMAdmin.next()
    await message.reply('Теперь введите название блюда.', reply_markup=kb_adm_cancel)


async def load_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
    await FSMAdmin.next()
    await message.reply('Введите описание блюда.', reply_markup=kb_adm_cancel)


async def load_description(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['description'] = message.text
    await FSMAdmin.next()
    await message.reply('Обозначьте цену.', reply_markup=kb_adm_cancel)


async def load_price(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['price'] = float(message.text)
    await sql_db_menu.sql_add_command(state)
    await state.finish()
    await bot.send_message(message.from_user.id, 'Всё сделано!', reply_markup=kb_adm_cancel)


async def del_cb(callback_query: types.CallbackQuery):
    """deleting data from the database"""
    await sql_db_menu.sql_delete(callback_query.data.replace('del ', ''))
    await callback_query.answer(text=f'{callback_query.data.replace("del ", "")} удалена', show_alert=True)


async def del_item(message: types.Message):
    """deleting data from the database"""
    if message.from_user.id == ID:
        read = await sql_db_menu.sql_read2()
        for r in read:
            await bot.send_photo(message.from_user.id, r[0],
                                 f'{r[1]}\nОписание: {r[2]}\n'
                                 f'Цена {r[-1]} руб.')
            await bot.send_message(message.from_user.id, text='^^^',
                                   reply_markup=InlineKeyboardMarkup().add(InlineKeyboardButton(f'Удалять'
                                                                                                f' {r[1]}',
                                                                                                callback_data=f'del {r[1]}')))


def register_handlers_admin(dp: Dispatcher):
    dp.register_message_handler(start_fsm, commands='Загрузить', state=None)
    dp.register_message_handler(cancel_handler, state="*", commands='отмена')
    dp.register_message_handler(cancel_handler, Text(equals='отмена', ignore_case=True), state="*")
    dp.register_message_handler(load_photo, content_types=['photo'], state=FSMAdmin.photo)
    dp.register_message_handler(load_name, state=FSMAdmin.name)
    dp.register_message_handler(load_description, state=FSMAdmin.description)
    dp.register_message_handler(load_price, state=FSMAdmin.price)
    dp.register_message_handler(make_changes_command, commands=['moderator'])
    dp.register_callback_query_handler(del_cb, lambda x: x.data and x.data.startswith('del '))
    dp.register_message_handler(del_item, commands='Удалить')
