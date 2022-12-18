from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton
import os

ccy_chf = InlineKeyboardButton(text='CHF', callback_data='CHF')
ccy_eur = InlineKeyboardButton(text='EUR', callback_data='EUR')
ccy_aud = InlineKeyboardButton(text='AUD', callback_data='AUD')
ccy_rub = InlineKeyboardButton(text='RUB', callback_data='RUB')
ccy_usd = InlineKeyboardButton(text='USD', callback_data='USD')
ccy = InlineKeyboardMarkup(resize_keyboard=True).row(ccy_chf, ccy_eur, ccy_aud, ccy_rub, ccy_usd)

cat_car = InlineKeyboardButton(text='Car', callback_data='Car')
cat_groceries = InlineKeyboardButton(text='Groceries', callback_data='Groceries')
cat_travel = InlineKeyboardButton(text='Travel', callback_data='Travel')
cat_etna = InlineKeyboardButton(text='Etna', callback_data='Etna')
cat_taxes = InlineKeyboardButton(text='Taxes', callback_data='Taxes')
cat_rest = InlineKeyboardButton(text='Restaurants', callback_data='Restaurants')
cat_shopping = InlineKeyboardButton(text='Shopping', callback_data='Shopping')
cat_utilities = InlineKeyboardButton(text='Utilities', callback_data='Utilities')
cat_other = InlineKeyboardButton(text='Other', callback_data='Other')
category = (
            InlineKeyboardMarkup(resize_keyboard=True)
            .add(cat_groceries, cat_car, cat_travel)
            .add(cat_rest, cat_etna, cat_utilities)
            .add(cat_shopping, cat_other, cat_taxes)
            )

personal_yes = InlineKeyboardButton(text='Family', callback_data='Family')
personal_no = InlineKeyboardButton(text='Personal', callback_data='Personal')
personal = InlineKeyboardMarkup(resize_keyboard=True).row(personal_yes, personal_no)

no_detail_kb = KeyboardButton(text='no detail')
no_detail = ReplyKeyboardMarkup(resize_keyboard=True).add(no_detail_kb)

dashboard_kb = InlineKeyboardButton(text='Click', url=os.environ.get('dashboard_url'))
dashboard = InlineKeyboardMarkup(resize_keyboard=True).add(dashboard_kb)

sheet_kb = InlineKeyboardButton(text='Click', url=os.environ.get('sheet_url'))
sheet = InlineKeyboardMarkup(resize_keyboard=True).add(sheet_kb)
