from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types, Dispatcher
from aiogram.types import ReplyKeyboardRemove
from aiogram.dispatcher.filters import Text
from create_bot import bot, dp
from keyboards import but_case_admin, but_cancel_pack
from data_base import sql_db

ID = None


class FSMAdmin(StatesGroup):
    photo = State()
    name = State()
    description = State()
    price = State()


# determining id of the current moderator
async def make_changes_command(message: types.Message):
    global ID
    ID = message.from_user.id
    await bot.send_message(message.from_user.id, 'Чем могу помочь, уважаемый администратор?',
                           reply_markup=but_case_admin)
    await message.delete()


async def start_fsm(message: types.Message):
    if message.from_user.id == ID:
        await FSMAdmin.photo.set()
        await message.reply('Загрузите фото.', reply_markup=but_cancel_pack)


# forsed stop
async def cancel_handler(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    await state.finish()
    await message.reply('Ok')


async def load_photo(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['photo'] = message.photo[0].file_id
    await FSMAdmin.next()
    await message.reply('Теперь введите название блюда.', reply_markup=but_cancel_pack)


async def load_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
    await FSMAdmin.next()
    await message.reply('Введите описание блюда.', reply_markup=but_cancel_pack)


async def load_description(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['description'] = message.text
    await FSMAdmin.next()
    await message.reply('Обозначьте цену.', reply_markup=but_cancel_pack)


async def load_price(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['price'] = float(message.text)
    await sql_db.sql_add_command(state)
    await state.finish()
    await bot.send_message(message.from_user.id, 'Всё сделано!', reply_markup=but_case_admin)


def register_handlers_admin(dp: Dispatcher):
    dp.register_message_handler(start_fsm, commands='Загрузить', state=None)
    dp.register_message_handler(cancel_handler, state="*", commands='отмена')
    dp.register_message_handler(cancel_handler, Text(equals='отмена', ignore_case=True), state="*")
    dp.register_message_handler(load_photo, content_types=['photo'], state=FSMAdmin.photo)
    dp.register_message_handler(load_name, state=FSMAdmin.name)
    dp.register_message_handler(load_description, state=FSMAdmin.description)
    dp.register_message_handler(load_price, state=FSMAdmin.price)
    dp.register_message_handler(make_changes_command, commands=['moderator'], is_chat_admin=True)
