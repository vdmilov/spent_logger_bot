import gspread
from main import allowed_ids
from datetime import datetime
import os

sa = gspread.service_account(filename='google_config.json')
sheet_id = os.environ.get('sheet_id')
sh = sa.open_by_key(sheet_id)
wks = sh.worksheet('spent_log')
s_id = int(wks.id)

vlad = []
sophie = []


def kill_list(user_id):
    if user_id == allowed_ids[0]:
        global vlad
        vlad = []
    elif user_id == allowed_ids[1]:
        global sophie
        sophie = []


def append_list(user_id, data):
    if user_id == allowed_ids[0]:
        vlad.append(data)
    elif user_id == allowed_ids[1]:
        sophie.append(data)


def extend_list(user_id, data):
    if user_id == allowed_ids[0]:
        vlad.extend(data)
    elif user_id == allowed_ids[1]:
        sophie.extend(data)


def new_entry(user_id):
    month = datetime.now().month
    year = datetime.now().year
    if user_id == allowed_ids[0]:
        user = 'Vlad'
    elif user_id == allowed_ids[1]:
        user = 'Sophie'
    data = [month, year, 'Out', user]
    return data


def last_row():
    return len(wks.col_values(1))


def copy_paste(s_id, last_row):
    reqs = [
        {
            "copyPaste": {
                "source": {
                    "sheetId": s_id,
                    "startRowIndex": last_row - 2,
                    "endRowIndex": last_row - 1,
                    "startColumnIndex": 10,
                    "endColumnIndex": 16,
                },
                "destination": {
                    "sheetId": s_id,
                    "startRowIndex": last_row - 1,
                    "endRowIndex": last_row,
                    "startColumnIndex": 10,
                    "endColumnIndex": 16,
                },
                "pasteType": "PASTE_FORMULA",
                "pasteOrientation": "NORMAL",
            }
        }
    ]
    sh.batch_update({"requests": reqs})


def input_entry(user_id):
    if user_id == allowed_ids[0]:
        wks.append_row(values=vlad)
    elif user_id == allowed_ids[1]:
        wks.append_row(values=sophie)
    copy_paste(s_id=s_id, last_row=last_row())


def delete_row(row_number):
    wks.delete_row(row_number)
