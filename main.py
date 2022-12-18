from aiogram import Bot, Dispatcher, executor, types
import os

import keyboards as kb
import gs
from steps import ccy, category, personal, investment_category

bot = Bot(token=os.environ.get('token'))
allowed_ids = [int(os.environ.get('vlad_id')), int(os.environ.get('sophie_id'))]
dp = Dispatcher(bot)


def auth(func):
    async def wrapper(message):
        if message.from_user.id not in allowed_ids:
            return await message.reply("Access denied", reply=False)
        return await func(message)
    return wrapper


@dp.message_handler(commands=['start'])
@auth
async def start(message: types.Message):
    await bot.send_message(message.from_user.id, "Select /new_entry")


@dp.message_handler(commands=['new_entry'])
@auth
async def new_entry(message: types.Message):
    gs.kill_list(user_id=message.from_user.id)
    await bot.send_message(message.from_user.id, "Input amount")
    gs.extend_list(user_id=message.from_user.id, data=gs.new_entry(message.from_user.id))


@dp.message_handler(commands=['delete_entry'])
@auth
async def delete_entry(message: types.Message):
    await bot.send_message(message.from_user.id, "Last entry deleted!")
    gs.delete_row(row_number=gs.last_row())


@dp.message_handler(commands=['dashboard'])
@auth
async def dashboard(message: types.Message):
    await bot.send_message(message.from_user.id, "Here is the dashboard", reply_markup=kb.dashboard)


@dp.message_handler(commands=['sheet'])
@auth
async def dashboard(message: types.Message):
    await bot.send_message(message.from_user.id, "Here is the google sheet", reply_markup=kb.sheet)    


@dp.message_handler()
@auth
async def any_message(message: types.Message):
    try:
        if ',' in message.text:
            amount = float(message.text.replace(',', '.'))
        else:
            amount = float(message.text)

        gs.append_list(user_id=message.from_user.id, data=amount)
        await bot.send_message(message.from_user.id, 'Select currency', reply_markup=kb.ccy)
    except ValueError:
        gs.append_list(user_id=message.from_user.id, data=message.text.lower())
        await bot.send_message(message.from_user.id, 'Logged! Another one /new_entry',
                               reply_markup=types.ReplyKeyboardRemove())
        gs.input_entry(user_id=message.from_user.id)


@dp.callback_query_handler()
async def callback_workaround(callback: types.callback_query):
    await callback.answer()
    gs.append_list(user_id=callback.from_user.id, data=callback.data)
    await bot.send_message(callback.from_user.id, text=f'Selected: {callback.data}')
    await bot.delete_message(chat_id=callback.from_user.id, message_id=callback.message.message_id)
    if callback.data in ccy:
        await bot.send_message(callback.from_user.id, text='Select category', reply_markup=kb.category)
    elif callback.data in investment_category:
        gs.append_list(user_id=callback.from_user.id, data='Yes')
        await bot.send_message(callback.from_user.id, text='Family or personal?', reply_markup=kb.personal)
    elif callback.data in category:
        gs.append_list(user_id=callback.from_user.id, data='No')
        await bot.send_message(callback.from_user.id, text='Family or personal?', reply_markup=kb.personal)
    elif callback.data in personal:
        await bot.send_message(callback.from_user.id, text='Please, provide detail or select "no detail"',
                               reply_markup=kb.no_detail)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
