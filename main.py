from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
import markups
import texts
import time
import pymysql
from config import host, user_name, password, db_name
import re
from openpyxl import load_workbook
import gspread
import datetime
import sk
import json
import aioschedule
import asyncio

TOKEN = ''

bot = Bot(TOKEN, parse_mode='Markdown')
db = Dispatcher(bot)

gc = gspread.service_account(filename='retail-397705-2cb2125124db.json')
sh = gc.open_by_url("https://docs.google.com/spreadsheets/d/1c389riVHBioK2N9elinFl6iqxN_OFTo00EXaipvzN-w")

def update(text, user):
    try:
        connection = pymysql.connect(
            host=host,
            port=3306,
            user=user_name,
            password=password,
            database=db_name,
            cursorclass=pymysql.cursors.DictCursor
        )

        try:
            with connection.cursor() as cursor:
                cursor.execute(text)
                connection.commit()
                return 0

        finally:
            connection.close()
    except Exception as ex:
        return f'Ошибка {ex}. Не продолжайте!\n\nПередайте руководителю и нажмите *ОТМЕНА*'

def create(text, user):
    try:
        connection = pymysql.connect(
            host=host,
            port=3306,
            user=user_name,
            password=password,
            database=db_name,
            cursorclass=pymysql.cursors.DictCursor
        )

        try:
            with connection.cursor() as cursor:
                cursor.execute(text)
                connection.commit()
                return 0

        finally:
            connection.close()
    except Exception as ex:
        return f'Ошибка {ex}. Не продолжайте!\n\nПередайте руководителю и нажмите *ОТМЕНА*'

def selone(text, user):
    try:
        connection = pymysql.connect(
            host=host,
            port=3306,
            user=user_name,
            password=password,
            database=db_name,
            cursorclass=pymysql.cursors.DictCursor
        )

        try:
            with connection.cursor() as cursor:
                cursor.execute(text)
                return cursor.fetchone()

        finally:
            connection.close()
    except Exception as ex:
        return f'Ошибка {ex}. Не продолжайте!\n\nПередайте руководителю и нажмите *ОТМЕНА*'

def selist(text, user):
    try:
        connection = pymysql.connect(
            host=host,
            port=3306,
            user=user_name,
            password=password,
            database=db_name,
            cursorclass=pymysql.cursors.DictCursor
        )

        try:
            with connection.cursor() as cursor:
                cursor.execute(text)
                return cursor.fetchall()

        finally:
            connection.close()
    except Exception as ex:
        return f'Ошибка {ex}. Не продолжайте!\n\nПередайте руководителю и нажмите *ОТМЕНА*'

def defaul_values(id_user):
    try:
        connection = pymysql.connect(
            host=host,
            port=3306,
            user=user_name,
            password=password,
            database=db_name,
            cursorclass=pymysql.cursors.DictCursor
        )

        try:
            with connection.cursor() as cur:
                cur.execute(f"UPDATE users SET word_5 = ' ', calc_box = 0, price = 0, height = 0, height_flag = 0, length1 = 0, "
                            f"length_flag = 0, width = 0, width_flag = 0, min_price = 0, minus_item2 = 0, "
                            f"xl_ul = 0, xl_ul_text = '', xl_tel = 0, xl_tel_text = 0, xl_type = 0, "
                            f"xl_type_text = '', xl_count_type = 0, xl_count_type_text = 0, xl_mark = 0, "
                            f"xl_mark_text = '', xl_pack = 0, xl_pack_text = '', xl_comment = 0, "
                            f"xl_comment_text = '', xl_city = 0, xl_city_text = '', xl_count_box = 0, "
                            f"xl_count_box_text = 0, xl_count_items = 0, xl_count_items_text = '', "
                            f"xl_comment_city = 0, xl_comment_city_text = '', xl_markbox = 0, xl_markbox_text = '', "
                            f"logistic = 0, ff = 0, new_id_user = 0, new_id_user_text = '', new_name_user = 0, "
                            f"remove_user = 0, fbo_15 = 0, new_car_city = 0, new_car_plan_start = 0, "
                            f"new_car_plan_end = 0, car_drive = 0, num_car = 0, drive_num = 0, gate = 0, "
                            f"find_car = 0, car_city = 0, chcar = 0, del_car = 0, find_zakaz = 0, sumpd = 0, "
                            f"countpd = 0, text_user = 0, id_fbo = 0, new_car_city_text = '', zak_day = 0, "
                            f"zak_mon = 0, zak_year = 0, ef_day = 0, ef_mon = 0, ef_year = 0, zabor = 0, "
                            f"ed_day = 0, ed_mon = 0, ed_year = 0, prib_day = 0, prib_mon = 0, prib_year = 0, "
                            f"fbo_16 = 0, chcar_2 = 0, remove_user_adm = 0, fbo_11 = 0, fbo_18 = 0, fbo_18_1 = 0, "
                            f"gate_2 = 0, find_car = 0, find_car_4 = 0, weight = 0, count_pal_flag = 0, "
                            f"max_id_item = 0, add_set_0 = 0, add_set_1 = 0, add_set_4 = 0, "
                            f"add_set_5 = 0, add_set_6 = 0, add_set_7 = 0, add_set_8 = 0, add_set_9 = 0, "
                            f"add_set_10 = 0, add_set_11 = 0, add_set_12 = 0, add_set_13 = 0, find_item = 0, "
                            f"what_in_box = 0, choose_ul = '', edit_item = 0, all_edit_item = 0, choose_id = '', "
                            f"choose_pr = '', edit_pr = 0, add_ul = 0, plus_new_sell = 0, plus_new_sell2 = 0, "
                            f"plus_new_sell3 = 0, count_wb = 0, count_ozon = 0, edit_box = 0, edit_box_item = 0, "
                            f"choose_box = '', edit_box_item_add = 0, find_item_id = 0, edit_ul_2 = 0, "
                            f"new_id_user = 0, new_id_user_text = '', new_name_user = 0, remove_user = 0, "
                            f"plus_new_sell4 = 0, text_user = 0, count_wb_60 = 0, count_ozon_60 = 0, "
                            f"count_wb_120 = 0, count_ozon_120 = 0, count_wb_max = 0, count_ozon_max = 0, "
                            f"plus_new_sell5 = 0, plus_new_sell6 = 0, plus_new_sell7 = 0, plus_new_sell8 = 0, "
                            f"plus_new_sell9 = 0, remove_user_adm = 0, find_item2 = 0, choose_ul_id = 0, act_sk = ' ', "
                            f"act_log = ' ' WHERE id_user = '{id_user}'")
                connection.commit()
                return 0

        finally:
            connection.close()
    except Exception as ex:
        return f'Ошибка {ex}. Не продолжайте!\n\nПередайте руководителю и нажмите *ОТМЕНА*'


async def startup(_):
    print('Бот запущен')

@db.message_handler(commands='info')
async def info_command(message: types.Message):
    id_user_get = f'`{message.chat.id}`'
    await message.answer(text=id_user_get, parse_mode='Markdown')

@db.message_handler(commands='test')
async def test_command(message: types.Message):
    user = message.chat.id
    msg = await message.answer('Привет')
    await bot.delete_message(user, msg.message_id)

@db.message_handler(commands='start')
async def start_command(message: types.Message):
    user = message.chat.id
    if selone(f"SELECT id_user FROM users WHERE id_user = '{user}'", user) is None or (selone(f"SELECT company FROM users WHERE id_user = '{user}'", user)["company"] != 'Водитель' and selone(f"SELECT company FROM users WHERE id_user = '{user}'", user)["company"] != 'Босс'):
        await message.answer(text=texts.start_text)
    else:
        if selone(f"SELECT driver FROM users WHERE id_user = '{user}'", user)['driver'] == 0:
            await message.answer(text=texts.start_text)
        else:
            if selone(f"SELECT driver FROM users WHERE id_user = '{user}'", user)['driver'] == 2:
                await message.answer(text=texts.menu_name, reply_markup=markups.menu_log_n)
            elif selone(f"SELECT driver FROM users WHERE id_user = '{user}'", user)['driver'] == 1:
                await message.answer(text=texts.menu_name, reply_markup=markups.menu_log_b)
            else:
                await message.answer(text='У вас нет доступа!')

@db.message_handler(content_types=['photo'])
async def handle_docs_photo(message):
    user = message.chat.id
    try:
        await message.answer(text=message)
    except Exception as e:
        await bot.send_message(-4077236615, f'🚚 Бот логистики\n\n{user}\nОшибка 196\n{e}')

@db.callback_query_handler()
async def action_callback(callback: types.CallbackQuery):
    user = callback.message.chat.id
    datework = sk.date_create()
    if 'crash_no' == callback.data:
        await callback.message.delete()
        res = selone(f"SELECT act_log FROM users WHERE id_user = '{user}'", user)['act_log'].split('_')
        update(f"UPDATE users SET act_log = ' ' WHERE id_user = '{user}'", user)
        datework = sk.date_create()
        create(f"INSERT INTO `data`.`work_drive` (`date_work`, `crash_auto`, `km_auto`) VALUES ('{datework}', 'Нет', '{res[1]}')", user)

        admins = selist(f"SELECT id_user FROM users WHERE driver = 1", user)
        for adm in admins:
            id_adm = adm['id_user']
            update(f"UPDATE users SET driver = 2 WHERE id_user = '{id_adm}'", user)

        name_user_log = selone(f"SELECT name_user FROM users WHERE id_user = '{user}'", user)['name_user']

        list_all_users = selist(f"SELECT * FROM users", user)
        list_users = []
        for us in list_all_users:
            if 'admin' in us['notif']:
                list_users.append(us)
        for user1 in list_users:
            try:
                chat_id = str(user1["id_user"])
                destination_bot = Bot(token='6682205213:AAFFV1avM8cVCZhgv-K8pzKeJ_c20Wle_P4')
                await destination_bot.send_message(chat_id, f'Водитель *{name_user_log}* вышел на смену\n\nПоказания пробега: *{res[1]}*', parse_mode='Markdown')
            except Exception as e:
                await bot.send_message(-4077236615, f'🚚 Бот логистики\n\n{user}\nОшибка 237\n{e}')

        await callback.message.answer(text='Смена открыта!', reply_markup=markups.menu_log_n)
        await callback.answer()
    elif 'crash_yes' == callback.data:
        await callback.message.delete()
        res = selone(f"SELECT act_log FROM users WHERE id_user = '{user}'", user)['act_log'].split('_')

        new_res = 'cryes_' + res[1]
        update(f"UPDATE users SET act_log = '{new_res}' WHERE id_user = '{user}'", user)

        await callback.message.answer(text='Опишите повреждения как можно точнее:', reply_markup=markups.back)
        await callback.answer()
    elif 'access_' in callback.data:
        if len(selist(f"SELECT * FROM shipping WHERE date_ship = '{datework}' AND status_ship = 'Принят'", user)) == 0:
            id_ship = callback.data.split('_')[1]
            str_id_list = selone(f"SELECT id_list FROM users WHERE id_user = '{user}'", user)['id_list']
            update(f"UPDATE users SET id_list = ' ' WHERE id_user = '{user}'", user)
            if str_id_list != ' ' and '_' in str_id_list:
                id_list = str_id_list.split('_')
                for i in id_list:
                    await bot.delete_message(user, i)
            else:
                await callback.message.delete()

            adress = selone(f"SELECT adress_begin FROM shipping WHERE id_ship = '{id_ship}'", user)['adress_begin']

            inline_m = InlineKeyboardMarkup(row_width=2)
            inline_m_b1 = InlineKeyboardButton(text='Да, адрес верен', callback_data=f'wait_{id_ship}')
            inline_m_b2 = InlineKeyboardButton(text='Адрес не верен', callback_data=f'waitno_{id_ship}')
            inline_m.add(inline_m_b1).add(inline_m_b2)

            await callback.message.answer(text=f'Клиент ждёт по адресу {adress}?', reply_markup=inline_m)
            await callback.answer()
        else:
            await callback.message.answer(text='У вас уже есть принятая заявка')
            l = selist(f"SELECT * FROM shipping WHERE date_ship = '{datework}' AND status_ship = 'Принят'", user)[0]

            inline_m = InlineKeyboardMarkup(row_width=2)
            inline_m_b1 = InlineKeyboardButton(text='Загрузился', callback_data=f'wacc_{l["id_ship"]}')
            inline_m_b2 = InlineKeyboardButton(text='Отмена заявки', callback_data=f'cancel_{l["id_ship"]}')
            inline_m.add(inline_m_b1).add(inline_m_b2)
            await message.answer(text=f'ID: *{l["id_ship"]}*\n'
                                      f'Тип: *{l["type_ship"]}*\n'
                                      f'Дата: *{l["date_ship"]}*\n'
                                      f'Время: *{l["time_ship"]}*\n'
                                      f'Предмет: *{l["item_ship"]}*\n'
                                      f'Количество: *{l["count_item_ship"]}*\n'
                                      f'Вес: *{l["w_ship"]}*\n\n'
                                      f'Адрес загрузки: `{l["adress_begin"]}`\n'
                                      f'Телефон загрузки: `{l["phone_begin"]}`\n'
                                      f'Адрес разгрузки: `{l["adress_end"]}`\n'
                                      f'Телефон разгрузки: `{l["phone_end"]}`\n'
                                      f'Комментарий: *{l["comment_ship"]}*\n\n'
                                      f'Статус: *{l["status_ship"]}*', parse_mode='Markdown', reply_markup=inline_m)
            await callback.answer()
    elif 'wait_' in callback.data:
        await callback.message.delete()
        id_ship = callback.data.split('_')[1]
        await callback.message.answer(text='Заявка принята!', reply_markup=markups.menu_log_n)
        update(f"UPDATE users SET act_log = ' ' WHERE id_user = '{user}'", user)
        update(f"UPDATE shipping SET status_ship = 'Принят' WHERE id_ship = '{id_ship}'", user)
        time_sk = sk.date_and_time_create()
        update(f"UPDATE shipping SET begin_ship = '{time_sk}' WHERE id_ship = '{id_ship}'", user)
        l = selist(f"SELECT * FROM shipping WHERE id_ship = '{id_ship}'", user)[0]
        inline_m = InlineKeyboardMarkup(row_width=2)
        inline_m_b1 = InlineKeyboardButton(text='Загрузился', callback_data=f'wacc_{l["id_ship"]}')
        inline_m_b2 = InlineKeyboardButton(text='Отмена заявки', callback_data=f'cancel_{l["id_ship"]}')
        inline_m.add(inline_m_b1).add(inline_m_b2)
        await callback.message.answer(text=f'ID: *{l["id_ship"]}*\n'
                                  f'Тип: *{l["type_ship"]}*\n'
                                  f'Дата: *{l["date_ship"]}*\n'
                                  f'Время: *{l["time_ship"]}*\n'
                                  f'Предмет: *{l["item_ship"]}*\n'
                                  f'Количество: *{l["count_item_ship"]}*\n'
                                  f'Вес: *{l["w_ship"]}*\n\n'
                                  f'Адрес загрузки: `{l["adress_begin"]}`\n'
                                  f'Телефон загрузки: `{l["phone_begin"]}`\n'
                                  f'Адрес разгрузки: `{l["adress_end"]}`\n'
                                  f'Телефон разгрузки: `{l["phone_end"]}`\n'
                                  f'Комментарий: *{l["comment_ship"]}*\n\n'
                                  f'Статус: *{l["status_ship"]}*', parse_mode='Markdown', reply_markup=inline_m)

        if l["type_ship"] == 'Забор' and l["nons"] != '0':
            nons_us = l["nons"]
            update(f"UPDATE new_fbo SET status_zakaz = 82 WHERE nons = '{nons_us}'", user)

            list_zakaz = selist(f"SELECT * FROM new_fbo WHERE nons = '{nons_us}'", user)
            id_user = list_zakaz[0]["own_zakaz"]
            list_client = selist(f"SELECT * FROM clients WHERE id_user = '{id_user}'", user)

            zakaz_text = f'У Вашей заявки с ID {list_zakaz[0]["id_zakaz"]} изменился статус!\n' \
                         f'\n<i>Склад отправки:</i> <b>{list_zakaz[0]["city"]}</b>' \
                         f'\n<i>Количество товара:</i> <b>{list_zakaz[0]["count_items"]}</b>' \
                         f'\n<i>Статус:</i> <b>Водитель выехал к Вам</b>'

            try:
                chat_id = str(id_user)
                destination_bot = Bot(token='6220819545:AAFS7TBQlmaZfpBEyoooOL-ac0YZQFxzec0')
                await destination_bot.send_message(chat_id, zakaz_text, parse_mode='html')
            except Exception as e:
                await bot.send_message(-4077236615, f'🚚 Бот логистики\n\n{user}\nОшибка 306\n{e}')

        await callback.answer()
    elif 'waitno_' in callback.data:
        await callback.message.delete()
        id_ship = callback.data.split('_')[1]
        new_res = 'waitno_' + id_ship
        update(f"UPDATE users SET act_log = '{new_res}' WHERE id_user = '{user}'", user)
        await callback.message.answer(text='Введите новый адрес:')
        await callback.answer()
    elif 'nophone_' in callback.data:
        if len(selist(f"SELECT * FROM shipping WHERE date_ship = '{datework}' AND status_ship = 'Принят'", user)) == 0:
            id_ship = callback.data.split('_')[1]
            str_id_list = selone(f"SELECT id_list FROM users WHERE id_user = '{user}'", user)['id_list']
            update(f"UPDATE users SET id_list = ' ' WHERE id_user = '{user}'", user)
            if str_id_list != ' ' and '_' in str_id_list:
                id_list = str_id_list.split('_')
                for i in id_list:
                    await bot.delete_message(user, i)
            else:
                await callback.message.delete()

            inline_m = InlineKeyboardMarkup(row_width=2)
            inline_m_b1 = InlineKeyboardButton(text='Да', callback_data=f'yessure_{id_ship}')
            inline_m_b2 = InlineKeyboardButton(text='Нет', callback_data=f'nosure_{id_ship}')
            inline_m.add(inline_m_b1).add(inline_m_b2)

            await callback.message.answer(text=f'Вы уверены?', reply_markup=inline_m)
            await callback.answer()
        else:
            await callback.message.answer(text='У вас уже есть принятая заявка')
            l = selist(f"SELECT * FROM shipping WHERE date_ship = '{datework}' AND status_ship = 'Принят'", user)[0]

            inline_m = InlineKeyboardMarkup(row_width=2)
            inline_m_b1 = InlineKeyboardButton(text='Загрузился', callback_data=f'wacc_{l["id_ship"]}')
            inline_m_b2 = InlineKeyboardButton(text='Отмена заявки', callback_data=f'cancel_{l["id_ship"]}')
            inline_m.add(inline_m_b1).add(inline_m_b2)
            await message.answer(text=f'ID: *{l["id_ship"]}*\n'
                                      f'Тип: *{l["type_ship"]}*\n'
                                      f'Дата: *{l["date_ship"]}*\n'
                                      f'Время: *{l["time_ship"]}*\n'
                                      f'Предмет: *{l["item_ship"]}*\n'
                                      f'Количество: *{l["count_item_ship"]}*\n'
                                      f'Вес: *{l["w_ship"]}*\n\n'
                                      f'Адрес загрузки: `{l["adress_begin"]}`\n'
                                      f'Телефон загрузки: `{l["phone_begin"]}`\n'
                                      f'Адрес разгрузки: `{l["adress_end"]}`\n'
                                      f'Телефон разгрузки: `{l["phone_end"]}`\n'
                                      f'Комментарий: *{l["comment_ship"]}*\n\n'
                                      f'Статус: *{l["status_ship"]}*', parse_mode='Markdown', reply_markup=inline_m)
            await callback.answer()
    elif 'yessure_' in callback.data:
        await callback.message.delete()
        id_ship = callback.data.split('_')[1]
        update(f"UPDATE shipping SET status_ship = 'Не дозвонился' WHERE id_ship = '{id_ship}'", user)
        await callback.message.answer(text='Статус не дозвонился проставлен!', reply_markup=markups.menu_log_n)

        l = selist(f"SELECT * FROM shipping WHERE id_ship = '{id_ship}'", user)[0]
        if l["type_ship"] == 'Забор' and l["nons"] != '0':
            nons_us = l["nons"]
            update(f"UPDATE new_fbo SET status_zakaz = 82 WHERE nons = '{nons_us}'", user)

            list_zakaz = selist(f"SELECT * FROM new_fbo WHERE nons = '{nons_us}'", user)
            id_user = list_zakaz[0]["own_zakaz"]
            list_client = selist(f"SELECT * FROM clients WHERE id_user = '{id_user}'", user)

            zakaz_text = f'<b>Водитель до Вас не дозвонился</b>'

            try:
                chat_id = str(id_user)
                destination_bot = Bot(token='6220819545:AAFS7TBQlmaZfpBEyoooOL-ac0YZQFxzec0')
                await destination_bot.send_message(chat_id, zakaz_text, parse_mode='html')
            except Exception as e:
                await bot.send_message(-4077236615, f'🚚 Бот логистики\n\n{user}\nОшибка 371\n{e}')

        await callback.answer()
    elif 'nosure_' in callback.data:
        await callback.message.delete()
        id_ship = callback.data.split('_')[1]

        l = selist(f"SELECT * FROM shipping WHERE id_ship = '{id_ship}'", user)[0]

        inline_m = InlineKeyboardMarkup(row_width=2)
        inline_m_b1 = InlineKeyboardButton(text='Принять', callback_data=f'access_{l["id_ship"]}')
        inline_m_b2 = InlineKeyboardButton(text='Не дозвонился', callback_data=f'nophone_{l["id_ship"]}')
        inline_m_b3 = InlineKeyboardButton(text='Перенос', callback_data=f'edite_{l["id_ship"]}')
        inline_m.add(inline_m_b1, inline_m_b2).add(inline_m_b3)
        await callback.message.answer(text=f'ID: *{l["id_ship"]}*\n'
                                           f'Тип: *{l["type_ship"]}*\n'
                                           f'Дата: *{l["date_ship"]}*\n'
                                           f'Время: *{l["time_ship"]}*\n'
                                           f'Предмет: *{l["item_ship"]}*\n'
                                           f'Количество: *{l["count_item_ship"]}*\n'
                                           f'Вес: *{l["w_ship"]}*\n\n'
                                           f'Адрес загрузки: `{l["adress_begin"]}`\n'
                                           f'Телефон загрузки: `{l["phone_begin"]}`\n'
                                           f'Адрес разгрузки: `{l["adress_end"]}`\n'
                                           f'Телефон разгрузки: `{l["phone_end"]}`\n'
                                           f'Комментарий: *{l["comment_ship"]}*\n\n'
                                           f'Статус: *{l["status_ship"]}*', parse_mode='Markdown',
                                      reply_markup=inline_m)
        await callback.answer()
    elif 'wacc_' in callback.data:
        id_ship = callback.data.split('_')[1]

        str_id_list = selone(f"SELECT id_list FROM users WHERE id_user = '{user}'", user)['id_list']
        update(f"UPDATE users SET id_list = ' ' WHERE id_user = '{user}'", user)
        if str_id_list != ' ' and '_' in str_id_list:
            id_list = str_id_list.split('_')
            for i in id_list:
                await bot.delete_message(user, i)
        else:
            await callback.message.delete()

        item_ship = selone(f"SELECT item_ship FROM shipping WHERE id_ship = '{id_ship}'", user)['item_ship']

        if selone(f"SELECT count_item_ship FROM shipping WHERE id_ship = '{id_ship}'", user)['count_item_ship'] == 'Не указано':
            update(f"UPDATE users SET act_log = ' ' WHERE id_user = '{user}'", user)
            update(f"UPDATE shipping SET status_ship = 'Едет к получателю' WHERE id_ship = '{id_ship}'", user)

            l = selist(f"SELECT * FROM shipping WHERE id_ship = '{id_ship}'", user)[0]

            inline_m = InlineKeyboardMarkup(row_width=2)
            inline_m_b1 = InlineKeyboardButton(text='Разгрузился', callback_data=f'done_{l["id_ship"]}')
            inline_m.add(inline_m_b1)
            await callback.message.answer(text=f'ID: *{l["id_ship"]}*\n'
                                      f'Тип: *{l["type_ship"]}*\n'
                                      f'Дата: *{l["date_ship"]}*\n'
                                      f'Время: *{l["time_ship"]}*\n'
                                      f'Предмет: *{l["item_ship"]}*\n'
                                      f'Количество: *{l["count_item_ship"]}*\n'
                                      f'Вес: *{l["w_ship"]}*\n\n'
                                      f'Адрес загрузки: `{l["adress_begin"]}`\n'
                                      f'Телефон загрузки: `{l["phone_begin"]}`\n'
                                      f'Адрес разгрузки: `{l["adress_end"]}`\n'
                                      f'Телефон разгрузки: `{l["phone_end"]}`\n'
                                      f'Комментарий: *{l["comment_ship"]}*\n\n'
                                      f'Статус: *{l["status_ship"]}*', parse_mode='Markdown', reply_markup=inline_m)
        else:
            new_res = 'wacc_' + id_ship
            update(f"UPDATE users SET act_log = '{new_res}' WHERE id_user = '{user}'", user)
            await callback.message.answer(text=f'Какое количество позиции «{item_ship}» вы забрали?', reply_markup=markups.back)
        await callback.answer()
    elif 'cancel_' in callback.data:
        id_ship = callback.data.split('_')[1]

        str_id_list = selone(f"SELECT id_list FROM users WHERE id_user = '{user}'", user)['id_list']
        update(f"UPDATE users SET id_list = ' ' WHERE id_user = '{user}'", user)
        if str_id_list != ' ' and '_' in str_id_list:
            id_list = str_id_list.split('_')
            for i in id_list:
                await bot.delete_message(user, i)
        else:
            await callback.message.delete()

        inline_m = InlineKeyboardMarkup(row_width=2)
        inline_m_b1 = InlineKeyboardButton(text='Да', callback_data=f'yescenc_{id_ship}')
        inline_m_b2 = InlineKeyboardButton(text='Нет', callback_data=f'noscenc_{id_ship}')
        inline_m.add(inline_m_b1).add(inline_m_b2)

        await callback.message.answer(text=f'Вы уверены, что хотите отменить заявку?', reply_markup=inline_m)
        await callback.answer()
    elif 'yescenc_' in callback.data:
        await callback.message.delete()
        id_ship = callback.data.split('_')[1]
        list_ship = selist(f"SELECT * FROM shipping WHERE id_ship = '{id_ship}'", user)[0]

        list_all_users = selist(f"SELECT * FROM users WHERE company = 'Босс'", user)
        list_users = []
        for us in list_all_users:
            if 'log' in us['notif']:
                list_users.append(us)
        for user1 in list_users:
            try:
                chat_id = str(user1["id_user"])
                destination_bot = Bot(token='6682205213:AAFFV1avM8cVCZhgv-K8pzKeJ_c20Wle_P4')
                await destination_bot.send_message(chat_id, f'Заявка с ID: {id_ship} отменена.\n\n'
                                                            f'Тип: *{list_ship["type_ship"]}*\n'
                                                            f'Предмет: *{list_ship["item_ship"]}*\n'
                                                            f'Адрес загрузки: *{list_ship["adress_begin"]}*\n'
                                                            f'Адрес разгрузки: *{list_ship["adress_end"]}*\n', parse_mode='Markdown')
            except Exception as e:
                await bot.send_message(-4077236615, f'🚚 Бот логистики\n\n{user}\nОшибка 460\n{str(user1["id_user"])}\n{e}')

        update(f"UPDATE shipping SET status_ship = 'Отменен' WHERE id_ship = '{id_ship}'", user)
        await callback.message.answer(text='Статус «Отменен» проставлен!', reply_markup=markups.menu_log_n)

        l = selist(f"SELECT * FROM shipping WHERE id_ship = '{id_ship}'", user)[0]
        if l["type_ship"] == 'Забор' and l["nons"] != '0':
            nons_us = l["nons"]
            update(f"UPDATE new_fbo SET status_zakaz = 80 WHERE nons = '{nons_us}'", user)

            list_zakaz = selist(f"SELECT * FROM new_fbo WHERE nons = '{nons_us}'", user)
            id_user = list_zakaz[0]["own_zakaz"]
            list_client = selist(f"SELECT * FROM clients WHERE id_user = '{id_user}'", user)

            zakaz_text = f'<b>Забор товара отменен!</b>'

            try:
                chat_id = str(id_user)
                destination_bot = Bot(token='6220819545:AAFS7TBQlmaZfpBEyoooOL-ac0YZQFxzec0')
                await destination_bot.send_message(chat_id, zakaz_text, parse_mode='html')
            except Exception as e:
                await bot.send_message(-4077236615, f'🚚 Бот логистики\n\n{user}\nОшибка 481\n{e}')

        await callback.answer()
    elif 'noscenc_' in callback.data:
        await callback.message.delete()
        await callback.message.answer(text= 'Главное меню', reply_markup=markups.menu_log_n)
        await callback.answer()
    elif 'done_' in callback.data:
        id_ship = callback.data.split('_')[1]

        str_id_list = selone(f"SELECT id_list FROM users WHERE id_user = '{user}'", user)['id_list']
        update(f"UPDATE users SET id_list = ' ' WHERE id_user = '{user}'", user)
        if str_id_list != ' ' and '_' in str_id_list:
            id_list = str_id_list.split('_')
            for i in id_list:
                await bot.delete_message(user, i)
        else:
            await callback.message.delete()

        new_res = 'done_' + id_ship
        update(f"UPDATE users SET act_log = '{new_res}' WHERE id_user = '{user}'", user)

        await callback.message.answer(text=f'Введите фамилию и имя, кто принял у вас груз:')
        await callback.answer()
    elif 'edite_' in callback.data:

        id_ship = callback.data.split('_')[1]
        str_id_list = selone(f"SELECT id_list FROM users WHERE id_user = '{user}'", user)['id_list']
        update(f"UPDATE users SET id_list = ' ' WHERE id_user = '{user}'", user)
        if str_id_list != ' ' and '_' in str_id_list:
            id_list = str_id_list.split('_')
            for i in id_list:
                await bot.delete_message(user, i)
        else:
            await callback.message.delete()
        new_res = 'edite_' + id_ship
        update(f"UPDATE users SET act_log = '{new_res}' WHERE id_user = '{user}'", user)
        await callback.message.answer(text='Введите новую дату в формате 21.12.2012:')
        await callback.answer()
    elif 'ref_' in callback.data:
        id_item = callback.data.split('_')[1]
        req = f'ref_{id_item}'
        update(f"UPDATE users SET act_log = '{req}' WHERE id_user = '{user}'", user)
        await callback.message.edit_text(text=f'Введите *количество*, которое забрали:', parse_mode='Markdown')
        await callback.answer()

@db.message_handler()
async def send_text(message: types.Message):
    user = message.chat.id
    datework = sk.date_create()

    if user == -4077236615:
        pass

    else:
        if selone(f"SELECT id_user FROM users WHERE id_user = '{user}'", user) is None or (
                selone(f"SELECT company FROM users WHERE id_user = '{user}'", user)["company"] != 'Водитель' and
                selone(f"SELECT company FROM users WHERE id_user = '{user}'", user)["company"] != 'Босс'):
            await message.answer(text=texts.start_text)
        else:
            if selone(f"SELECT driver FROM users WHERE id_user = '{user}'", user)['driver'] == 0:
                await message.answer(text=texts.start_text)
            else:
                # Главное меню
                if message.text == markups.menu_main:
                    defaul_values(user)
                    if selone(f"SELECT driver FROM users WHERE id_user = '{user}'", user)['driver'] == 2:
                        await message.answer(text=texts.menu_name, reply_markup=markups.menu_log_n)
                    elif selone(f"SELECT driver FROM users WHERE id_user = '{user}'", user)['driver'] == 1:
                        await message.answer(text=texts.menu_name, reply_markup=markups.menu_log_b)
                    else:
                        await message.answer(text='У вас нет доступа!')

                # Отмена
                elif message.text == markups.menu_back:
                    defaul_values(user)
                    if selone(f"SELECT driver FROM users WHERE id_user = '{user}'", user)['driver'] == 2:
                        await message.answer(text=texts.menu_name, reply_markup=markups.menu_log_n)
                    elif selone(f"SELECT driver FROM users WHERE id_user = '{user}'", user)['driver'] == 1:
                        await message.answer(text=texts.menu_name, reply_markup=markups.menu_log_b)
                    else:
                        await message.answer(text='У вас нет доступа!')

                # Открыть смену
                elif message.text == markups.menu_log_b4:
                    datework = sk.date_create()
                    if selone(f"SELECT driver FROM users WHERE id_user = '{user}'", user)['driver'] == 2:
                        await message.answer(text='Смена была уже открыта!', reply_markup=markups.menu_log_n)
                    else:
                        if selone(f"SELECT date_work FROM work_ship WHERE date_work = '{datework}'", user) is None:
                            await message.answer(text='Маршрутный лист не сформирован!')
                        else:
                            if selone(f"SELECT date_work FROM work_drive WHERE date_work = '{datework}'", user) is None:
                                res = 'crash_'
                                update(f"UPDATE users SET act_log = '{res}' WHERE id_user = '{user}'", user)
                                await message.answer(text=f'Показания пробега:', reply_markup=markups.back)
                            else:
                                await message.answer(text='Сегодняшняя смена завершена!')
                elif 'crash_' in selone(f"SELECT act_log FROM users WHERE id_user = '{user}'", user)['act_log']:
                    if message.text.isdigit():
                        res = 'why_' + message.text
                        update(f"UPDATE users SET act_log = '{res}' WHERE id_user = '{user}'", user)

                        inline_crash = InlineKeyboardMarkup(row_width=1)
                        inline_crash_b1 = InlineKeyboardButton(text='Да', callback_data='crash_yes')
                        inline_crash_b2 = InlineKeyboardButton(text='Нет', callback_data='crash_no')
                        inline_crash.add(inline_crash_b1).add(inline_crash_b2)

                        await message.answer(text=f'Есть ли повреждения на кузове?', reply_markup=inline_crash)
                    else:
                        await message.answer(text=f'Введите пробег целым числом!')
                elif 'why_' in selone(f"SELECT act_log FROM users WHERE id_user = '{user}'", user)['act_log']:
                    inline_crash = InlineKeyboardMarkup(row_width=1)
                    inline_crash_b1 = InlineKeyboardButton(text='Да', callback_data='crash_yes')
                    inline_crash_b2 = InlineKeyboardButton(text='Нет', callback_data='crash_no')
                    inline_crash.add(inline_crash_b1).add(inline_crash_b2)

                    await message.answer(text=f'Есть ли повреждения на кузове?', reply_markup=inline_crash)
                elif 'cryes_' in selone(f"SELECT act_log FROM users WHERE id_user = '{user}'", user)['act_log']:
                    res = selone(f"SELECT act_log FROM users WHERE id_user = '{user}'", user)['act_log'].split('_')
                    update(f"UPDATE users SET act_log = ' ' WHERE id_user = '{user}'", user)
                    datework = sk.date_create()
                    create(f"INSERT INTO `data`.`work_drive` (`date_work`, `crash_auto`, `km_auto`) VALUES ('{datework}', '{message.text}', '{res[1]}')", user)
                    admins = selist(f"SELECT id_user FROM users WHERE driver = 1", user)
                    for adm in admins:
                        id_adm = adm['id_user']
                        update(f"UPDATE users SET driver = 2 WHERE id_user = '{id_adm}'", user)

                    name_user_log = selone(f"SELECT name_user FROM users WHERE id_user = '{user}'", user)['name_user']

                    list_users = selist(f"SELECT * FROM users WHERE company = 'Босс'", user)
                    for user1 in list_users:
                        try:
                            chat_id = str(user1["id_user"])
                            destination_bot = Bot(token='6682205213:AAFFV1avM8cVCZhgv-K8pzKeJ_c20Wle_P4')
                            await destination_bot.send_message(chat_id, f'Водитель *{name_user_log}* вышел на смену\n\nПоказания пробега: *{res[1]}*', parse_mode='Markdown')
                        except Exception as e:
                            await bot.send_message(-4077236615, f'🚚 Бот логистики\n\n{user}\nОшибка 590\n{e}\n\nПользователь написал: {message.text}')

                    await message.answer(text='Смена открыта!', reply_markup=markups.menu_log_n)

                # Закрыть смену
                elif message.text == markups.menu_log_b3:
                    datework = sk.date_create()
                    if selone(f"SELECT driver FROM users WHERE id_user = '{user}'", user)['driver'] == 1:
                        await message.answer(text='Смена была уже закрыта!', reply_markup=markups.menu_log_b)
                    else:
                        if len(selist(f"SELECT * FROM shipping WHERE date_ship = '{datework}' AND status_ship <> 'Отменен' AND status_ship <> 'Закончен'", user)) == 0:
                            admins = selist(f"SELECT id_user FROM users WHERE driver = 2", user)
                            for adm in admins:
                                id_adm = adm['id_user']
                                update(f"UPDATE users SET driver = 1 WHERE id_user = '{id_adm}'", user)

                            await message.answer(text='Смена закрыта!', reply_markup=markups.menu_log_b)
                        else:
                            await message.answer(text='Не все заявки обработаны!')

                # Загрузки
                elif message.text == markups.menu_log_b1:
                    if selone(f"SELECT date_work FROM work_drive WHERE date_work = '{sk.date_create()}'", user) is None:
                            await message.answer(text='Вчерашняя смена не была закрыта! Обратитесь к руководителю!')
                    else:
                        if len(selist(f"SELECT * FROM shipping WHERE date_ship = '{datework}' AND status_ship = 'Принят'", user)) == 0:
                            if len(selist(f"SELECT * FROM shipping WHERE date_ship = '{datework}' AND status_ship = 'В очереди'", user)) != 0:
                                await message.answer(text='*Очередь заявок на загрузку:*', reply_markup=markups.back)
                                newlist = selist(f"SELECT * FROM shipping WHERE date_ship = '{datework}' AND status_ship = 'В очереди'", user)

                                id_list = []
                                list_log = sorted(newlist, key=lambda d: d['num_ship'])
                                for l in list_log:
                                    inline_m = InlineKeyboardMarkup(row_width=2)
                                    inline_m_b1 = InlineKeyboardButton(text='Принять', callback_data=f'access_{l["id_ship"]}')
                                    inline_m_b2 = InlineKeyboardButton(text='Не дозвонился', callback_data=f'nophone_{l["id_ship"]}')
                                    inline_m_b3 = InlineKeyboardButton(text='Перенос', callback_data=f'edite_{l["id_ship"]}')
                                    inline_m_b4 = InlineKeyboardButton(text='Отмена заявки', callback_data=f'cancel_{l["id_ship"]}')
                                    inline_m.add(inline_m_b1, inline_m_b2).add(inline_m_b3).add(inline_m_b4)
                                    msg = await message.answer(text=f'ID: *{l["id_ship"]}*\n'
                                                              f'Тип: *{l["type_ship"]}*\n'
                                                              f'Дата: *{l["date_ship"]}*\n'
                                                              f'Время: *{l["time_ship"]}*\n'
                                                              f'Предмет: *{l["item_ship"]}*\n'
                                                              f'Количество: *{l["count_item_ship"]}*\n'
                                                              f'Вес: *{l["w_ship"]}*\n\n'
                                                              f'Адрес загрузки: `{l["adress_begin"]}`\n'
                                                              f'Телефон загрузки: `{l["phone_begin"]}`\n'
                                                              f'Адрес разгрузки: `{l["adress_end"]}`\n'
                                                              f'Телефон разгрузки: `{l["phone_end"]}`\n'
                                                              f'Комментарий: *{l["comment_ship"]}*\n\n'
                                                              f'Статус: *{l["status_ship"]}*', parse_mode='Markdown', reply_markup=inline_m)

                                    id_list.append(str(msg.message_id))

                                str_id_list = '_'.join(id_list)
                                update(f"UPDATE users SET id_list = '{str_id_list}' WHERE id_user = '{user}'", user)



                            else:
                                await message.answer(text='Очередь пуста!')
                        else:
                            await message.answer(text='*У вас принята заявка:*', reply_markup=markups.back)
                            l = selist(f"SELECT * FROM shipping WHERE date_ship = '{datework}' AND status_ship = 'Принят'", user)[0]

                            inline_m = InlineKeyboardMarkup(row_width=2)
                            inline_m_b1 = InlineKeyboardButton(text='Загрузился', callback_data=f'wacc_{l["id_ship"]}')
                            inline_m_b2 = InlineKeyboardButton(text='Отмена заявки', callback_data=f'cancel_{l["id_ship"]}')
                            inline_m.add(inline_m_b1).add(inline_m_b2)
                            await message.answer(text=f'ID: *{l["id_ship"]}*\n'
                                                      f'Тип: *{l["type_ship"]}*\n'
                                                      f'Дата: *{l["date_ship"]}*\n'
                                                      f'Время: *{l["time_ship"]}*\n'
                                                      f'Предмет: *{l["item_ship"]}*\n'
                                                      f'Количество: *{l["count_item_ship"]}*\n'
                                                      f'Вес: *{l["w_ship"]}*\n\n'
                                                      f'Адрес загрузки: `{l["adress_begin"]}`\n'
                                                      f'Телефон загрузки: `{l["phone_begin"]}`\n'
                                                      f'Адрес разгрузки: `{l["adress_end"]}`\n'
                                                      f'Телефон разгрузки: `{l["phone_end"]}`\n'
                                                      f'Комментарий: *{l["comment_ship"]}*\n\n'
                                                      f'Статус: *{l["status_ship"]}*', parse_mode='Markdown', reply_markup=inline_m)
                elif 'waitno_' in selone(f"SELECT act_log FROM users WHERE id_user = '{user}'", user)['act_log']:
                    th_res = selone(f"SELECT act_log FROM users WHERE id_user = '{user}'", user)['act_log']
                    sec_res = th_res.split('_')
                    id_ship = sec_res[1]
                    update(f"UPDATE users SET act_log = ' ' WHERE id_user = '{user}'", user)
                    update(f"UPDATE shipping SET adress_begin = '{message.text}' WHERE id_ship = '{id_ship}'", user)

                    l = selist(f"SELECT * FROM shipping WHERE id_ship = '{id_ship}'", user)[0]

                    inline_m = InlineKeyboardMarkup(row_width=2)
                    inline_m_b1 = InlineKeyboardButton(text='Принять', callback_data=f'access_{l["id_ship"]}')
                    inline_m_b2 = InlineKeyboardButton(text='Не дозвонился', callback_data=f'nophone_{l["id_ship"]}')
                    inline_m_b3 = InlineKeyboardButton(text='Перенос', callback_data=f'edite_{l["id_ship"]}')
                    inline_m.add(inline_m_b1, inline_m_b2).add(inline_m_b3)
                    await message.answer(text=f'ID: *{l["id_ship"]}*\n'
                                                       f'Тип: *{l["type_ship"]}*\n'
                                                       f'Дата: *{l["date_ship"]}*\n'
                                                       f'Время: *{l["time_ship"]}*\n'
                                                       f'Предмет: *{l["item_ship"]}*\n'
                                                       f'Количество: *{l["count_item_ship"]}*\n'
                                                       f'Вес: *{l["w_ship"]}*\n\n'
                                                       f'Адрес загрузки: `{l["adress_begin"]}`\n'
                                                       f'Телефон загрузки: `{l["phone_begin"]}`\n'
                                                       f'Адрес разгрузки: `{l["adress_end"]}`\n'
                                                       f'Телефон разгрузки: `{l["phone_end"]}`\n'
                                                       f'Комментарий: *{l["comment_ship"]}*\n\n'
                                                       f'Статус: *{l["status_ship"]}*', parse_mode='Markdown', reply_markup=inline_m)
                elif 'wacc_' in selone(f"SELECT act_log FROM users WHERE id_user = '{user}'", user)['act_log']:
                    if message.text.isdigit():
                        th_res = selone(f"SELECT act_log FROM users WHERE id_user = '{user}'", user)['act_log']
                        sec_res = th_res.split('_')
                        id_ship = sec_res[1]
                        update(f"UPDATE users SET act_log = ' ' WHERE id_user = '{user}'", user)

                        if int(message.text) != int(selone(f"SELECT count_item_ship FROM shipping WHERE id_ship = '{id_ship}'", user)['count_item_ship']):
                            list_all_users = selist(f"SELECT * FROM users WHERE company = 'Босс'", user)
                            list_users = []
                            for us in list_all_users:
                                if 'log' in us['notif']:
                                    list_users.append(us)
                            list_ship = selist(f"SELECT * FROM shipping WHERE id_ship = '{id_ship}'", user)[0]
                            for user1 in list_users:
                                try:
                                    chat_id = str(user1["id_user"])
                                    destination_bot = Bot(token='6682205213:AAFFV1avM8cVCZhgv-K8pzKeJ_c20Wle_P4')
                                    await destination_bot.send_message(chat_id, f'Изменено водителем количество позиций у заявки с ID: {id_ship}\n\n'
                                                                                f'Тип: *{list_ship["type_ship"]}*\n'
                                                                                f'Предмет: *{list_ship["item_ship"]}*\n'
                                                                                f'Количество было: *{list_ship["count_item_ship"]}*\n'
                                                                                f'Количество стало: *{message.text}*\n'
                                                                                f'Адрес загрузки: *{list_ship["adress_begin"]}*\n'
                                                                                f'Адрес разгрузки: *{list_ship["adress_end"]}*\n', parse_mode='Markdown')

                                except Exception as e:
                                    await bot.send_message(-4077236615, f'🚚 Бот логистики\n\n{user}\nОшибка 714\n{str(user1["id_user"])}\n{e}\n\nПользователь написал: {message.text}')

                        update(f"UPDATE shipping SET count_item_ship = '{message.text}' WHERE id_ship = '{id_ship}'", user)
                        update(f"UPDATE shipping SET status_ship = 'Едет к получателю' WHERE id_ship = '{id_ship}'", user)

                        l = selist(f"SELECT * FROM shipping WHERE id_ship = '{id_ship}'", user)[0]

                        inline_m = InlineKeyboardMarkup(row_width=2)
                        inline_m_b1 = InlineKeyboardButton(text='Разгрузился', callback_data=f'done_{l["id_ship"]}')
                        inline_m.add(inline_m_b1)
                        await message.answer(text=f'ID: *{l["id_ship"]}*\n'
                                                  f'Тип: *{l["type_ship"]}*\n'
                                                  f'Дата: *{l["date_ship"]}*\n'
                                                  f'Время: *{l["time_ship"]}*\n'
                                                  f'Предмет: *{l["item_ship"]}*\n'
                                                  f'Количество: *{l["count_item_ship"]}*\n'
                                                  f'Вес: *{l["w_ship"]}*\n\n'
                                                  f'Адрес загрузки: `{l["adress_begin"]}`\n'
                                                  f'Телефон загрузки: `{l["phone_begin"]}`\n'
                                                  f'Адрес разгрузки: `{l["adress_end"]}`\n'
                                                  f'Телефон разгрузки: `{l["phone_end"]}`\n'
                                                  f'Комментарий: *{l["comment_ship"]}*\n\n'
                                                  f'Статус: *{l["status_ship"]}*', parse_mode='Markdown', reply_markup=inline_m)

                        id_car = l["car_id"]
                        if id_car != 0:
                            delta_1 = datetime.timedelta(hours=5)
                            now = datetime.datetime.now() + delta_1
                            mes = f'{now.hour}:{now.minute} | {now.day}.{now.month}.{now.year}'

                            list_fbo = selist(f"SELECT * FROM fbo WHERE car_id = '{id_car}' and ff_city = 0", user)

                            for i in list_fbo:
                                if i['own_fbo'] != 0:
                                    fbo_id = i['fbo_id']
                                    update(f"UPDATE new_fbo SET status = 3 WHERE id_fbo = '{fbo_id}'", user)
                                    id_client = selone(f"SELECT own_fbo FROM fbo WHERE fbo_id = '{fbo_id}'", user)[
                                        'own_fbo']
                                    try:
                                        nons = selone(f"SELECT nons FROM new_fbo WHERE id_fbo = '{int(fbo_id)}'", user)[
                                            'nons']
                                        status_zakaz = 3
                                        update(
                                            f"UPDATE new_fbo SET status_zakaz = '{status_zakaz}' WHERE nons = '{nons}'",
                                            user)
                                        list_zakaz = selist(f"SELECT * FROM new_fbo WHERE nons = '{nons}'", user)
                                        id_user = list_zakaz[0]["own_zakaz"]
                                        list_client = selist(f"SELECT * FROM clients WHERE id_user = '{id_user}'", user)

                                        if list_zakaz[0]["status_zakaz"] == 80:
                                            status_zakaz = 'Не принято на фулфилменте'
                                        elif list_zakaz[0]["status_zakaz"] == 100:
                                            status_zakaz = 'Отменен'
                                        elif list_zakaz[0]["status_zakaz"] == 0:
                                            status_zakaz = 'Принято на фулфилменте'
                                        elif list_zakaz[0]["status_zakaz"] == 1:
                                            status_zakaz = 'Обработка...'
                                        elif list_zakaz[0]["status_zakaz"] == 2:
                                            status_zakaz = 'Готов к отправке'
                                        elif list_zakaz[0]["status_zakaz"] == 3:
                                            status_zakaz = 'Доставка...'
                                        elif list_zakaz[0]["status_zakaz"] == 4:
                                            status_zakaz = 'Доставлен'
                                        elif list_zakaz[0]["status_zakaz"] == 5:
                                            status_zakaz = 'Не принято на складе. Обработка...'

                                        zakaz_text = f'У Вашей заявки с ID {list_zakaz[0]["id_zakaz"]} изменился статус!\n' \
                                                     f'\n<i>Склад отправки:</i> <b>{list_zakaz[0]["city"]}</b>' \
                                                     f'\n<i>Количество товара:</i> <b>{list_zakaz[0]["count_items"]}</b>' \
                                                     f'\n<i>Время загрузки:</i> <b>{mes}</b>' \
                                                     f'\n<i>Статус:</i> <b>{status_zakaz}</b>'

                                        try:
                                            chat_id = str(id_user)
                                            destination_bot = Bot(
                                                token='6220819545:AAFS7TBQlmaZfpBEyoooOL-ac0YZQFxzec0')
                                            await destination_bot.send_message(chat_id, zakaz_text, parse_mode='html')
                                        except:
                                            pass
                                    except:
                                        pass

                            update(f"UPDATE cars SET count_pal = '1' WHERE car_id = '{id_car}'", user)
                            update(f"UPDATE cars SET fact_start_date = '{mes}' WHERE car_id = '{id_car}'", user)

                        if l["type_ship"] == 'Забор' and l["nons"] != '0':
                            nons_us = l["nons"]
                            update(f"UPDATE new_fbo SET status_zakaz = 83 WHERE nons = '{nons_us}'", user)

                            list_zakaz = selist(f"SELECT * FROM new_fbo WHERE nons = '{nons_us}'", user)
                            id_user = list_zakaz[0]["own_zakaz"]
                            list_client = selist(f"SELECT * FROM clients WHERE id_user = '{id_user}'", user)

                            zakaz_text = f'У Вашей заявки с ID {list_zakaz[0]["id_zakaz"]} изменился статус!\n' \
                                         f'\n<i>Склад отправки:</i> <b>{list_zakaz[0]["city"]}</b>' \
                                         f'\n<i>Количество товара:</i> <b>{list_zakaz[0]["count_items"]}</b>' \
                                         f'\n<i>Статус:</i> <b>Груз едет на фулфилмент</b>'

                            try:
                                chat_id = str(id_user)
                                destination_bot = Bot(token='6220819545:AAFS7TBQlmaZfpBEyoooOL-ac0YZQFxzec0')
                                await destination_bot.send_message(chat_id, zakaz_text, parse_mode='html')
                            except Exception as e:
                                await bot.send_message(-4077236615, f'🚚 Бот логистики\n\n{user}\nОшибка 756\n{e}')
                    else:
                        await message.answer(text='Введите количество числом!')
                elif 'edite_' in selone(f"SELECT act_log FROM users WHERE id_user = '{user}'", user)['act_log']:
                    callback_data = selone(f"SELECT act_log FROM users WHERE id_user = '{user}'", user)['act_log']
                    list_call = callback_data.split('_')
                    id_ship = list_call[1]
                    if len(message.text.split('.')) == 3 and len(message.text) == 10:
                        delta_1 = datetime.timedelta(hours=5)
                        now = datetime.datetime.now() + delta_1

                        if ((int(message.text[0:2]) < int(now.day)) and (int(message.text[3:5]) == int(now.month))) or (
                                int(message.text[3:5]) < int(now.month)):
                            await message.answer(text='Вы можете указать дату начиная с сегодняшнего дня:')

                        elif (int(message.text[0:2]) == int(now.day)) and (int(sk.time_create()[0:2]) > 18):
                            await message.answer(text='На сегодня вы уже не можете создать заявку, укажите другую дату:')

                        else:
                            update(f"UPDATE users SET edit_log = ' ' WHERE id_user = '{user}'", user)
                            update(f"UPDATE users SET act_log = ' ' WHERE id_user = '{user}'", user)
                            update(f"UPDATE shipping SET date_ship = '{message.text}' WHERE id_ship = '{id_ship}'", user)
                            update(f"UPDATE shipping SET num_ship = 0 WHERE id_ship = '{id_ship}'", user)

                            l = selist(f"SELECT * FROM shipping WHERE id_ship = '{id_ship}'", user)[0]

                            list_all_users = selist(f"SELECT * FROM users WHERE company = 'Босс'", user)
                            list_users = []
                            for us in list_all_users:
                                if 'log' in us['notif']:
                                    list_users.append(us)
                            for user1 in list_users:
                                try:
                                    chat_id = str(user1["id_user"])
                                    destination_bot = Bot(token='6682205213:AAFFV1avM8cVCZhgv-K8pzKeJ_c20Wle_P4')
                                    await destination_bot.send_message(chat_id, f'Водитель изменил дату у заявки с ID: {id_ship}!\n\n'
                                                                                f'Тип: *{l["type_ship"]}*\n'
                                                                                f'Дата: *{l["date_ship"]}*\n'
                                                                                f'Время: *{l["time_ship"]}*\n'
                                                                                f'Предмет: *{l["item_ship"]}*\n'
                                                                                f'Количество: *{l["count_item_ship"]}*\n'
                                                                                f'Вес: *{l["w_ship"]}*\n\n'
                                                                                f'Адрес загрузки: `{l["adress_begin"]}`\n'
                                                                                f'Телефон загрузки: `{l["phone_begin"]}`\n'
                                                                                f'Адрес разгрузки: `{l["adress_end"]}`\n'
                                                                                f'Телефон разгрузки: `{l["phone_end"]}`\n'
                                                                                f'Комментарий: *{l["comment_ship"]}*\n\n'
                                                                                f'Статус: *{l["status_ship"]}*', parse_mode='Markdown')
                                except Exception as e:
                                    await bot.send_message(-4077236615, f'🚚 Бот логистики\n\n{user}\nОшибка 801\n{e}\n\nПользователь написал: {message.text}')

                            await message.answer(text='Дата изменена!', reply_markup=markups.menu_log_n)

                            if l["type_ship"] == 'Забор' and l["nons"] != '0':
                                nons_us = l["nons"]
                                old_zabor = selone(f"SELECT zabor FROM new_fbo WHERE nons = '{nons_us}'", user)['zabor'].split('_')

                                res2 = f'{message.text}_{old_zabor[1]}_{old_zabor[2]}'

                                update(f"UPDATE new_fbo SET zabor = '{nons_us}' WHERE nons = '{nons_us}'", user)

                                list_zakaz = selist(f"SELECT * FROM new_fbo WHERE nons = '{nons_us}'", user)
                                id_user = list_zakaz[0]["own_zakaz"]
                                list_client = selist(f"SELECT * FROM clients WHERE id_user = '{id_user}'", user)

                                zakaz_text = f'У Вашей заявки с ID {list_zakaz[0]["id_zakaz"]} изменилась дата забора!\n' \
                                             f'\n<i>Склад отправки:</i> <b>{list_zakaz[0]["city"]}</b>' \
                                             f'\n<i>Количество товара:</i> <b>{list_zakaz[0]["count_items"]}</b>' \
                                             f'\n\n<i>Дата забора:</i> <b>{message.text}</b>'

                                try:
                                    chat_id = str(id_user)
                                    destination_bot = Bot(token='6220819545:AAFS7TBQlmaZfpBEyoooOL-ac0YZQFxzec0')
                                    await destination_bot.send_message(chat_id, zakaz_text, parse_mode='html')
                                except Exception as e:
                                    await bot.send_message(-4077236615, f'🚚 Бот логистики\n\n{user}\nОшибка 827\n{e}')
                    else:
                        await message.answer(text='Введите дату в формате 01.11.2023')

                # Разгрузки
                elif message.text == markups.menu_log_b2:
                    if selone(f"SELECT date_work FROM work_drive WHERE date_work = '{sk.date_create()}'", user) is None:
                            await message.answer(text='Вчерашняя смена не была закрыта! Обратитесь к руководителю!')
                    else:
                        if len(selist(f"SELECT * FROM shipping WHERE date_ship = '{datework}' AND status_ship = 'Едет к получателю'", user)) != 0:
                            await message.answer(text='*Очередь заявок на разгрузку:*', reply_markup=markups.back)
                            newlist = selist(f"SELECT * FROM shipping WHERE date_ship = '{datework}' AND status_ship = 'Едет к получателю'", user)

                            id_list = []
                            list_log = sorted(newlist, key=lambda d: d['num_ship'])
                            for l in list_log:
                                inline_m = InlineKeyboardMarkup(row_width=2)
                                inline_m_b1 = InlineKeyboardButton(text='Разгрузился', callback_data=f'done_{l["id_ship"]}')
                                inline_m.add(inline_m_b1)
                                msg = await message.answer(text=f'ID: *{l["id_ship"]}*\n'
                                                          f'Тип: *{l["type_ship"]}*\n'
                                                          f'Дата: *{l["date_ship"]}*\n'
                                                          f'Время: *{l["time_ship"]}*\n'
                                                          f'Предмет: *{l["item_ship"]}*\n'
                                                          f'Количество: *{l["count_item_ship"]}*\n'
                                                          f'Вес: *{l["w_ship"]}*\n\n'
                                                          f'Адрес загрузки: `{l["adress_begin"]}`\n'
                                                          f'Телефон загрузки: `{l["phone_begin"]}`\n'
                                                          f'Адрес разгрузки: `{l["adress_end"]}`\n'
                                                          f'Телефон разгрузки: `{l["phone_end"]}`\n'
                                                          f'Комментарий: *{l["comment_ship"]}*\n\n'
                                                          f'Статус: *{l["status_ship"]}*', parse_mode='Markdown', reply_markup=inline_m)
                                id_list.append(str(msg.message_id))

                            str_id_list = '_'.join(id_list)
                            update(f"UPDATE users SET id_list = '{str_id_list}' WHERE id_user = '{user}'", user)
                        else:
                            await message.answer(text='*Очередь заявок на разгрузку пуста*')
                elif 'done_' in selone(f"SELECT act_log FROM users WHERE id_user = '{user}'", user)['act_log']:
                    th_res = selone(f"SELECT act_log FROM users WHERE id_user = '{user}'", user)['act_log']
                    sec_res = th_res.split('_')
                    id_ship = sec_res[1]
                    update(f"UPDATE users SET act_log = ' ' WHERE id_user = '{user}'", user)
                    time_sk = sk.date_and_time_create()
                    update(f"UPDATE shipping SET end_ship = '{time_sk}' WHERE id_ship = '{id_ship}'", user)

                    list_all_users = selist(f"SELECT * FROM users WHERE company = 'Босс'", user)
                    list_users = []
                    for us in list_all_users:
                        if 'log' in us['notif']:
                            list_users.append(us)
                    list_ship = selist(f"SELECT * FROM shipping WHERE id_ship = '{id_ship}'", user)[0]
                    for user1 in list_users:
                        try:
                            chat_id = str(user1["id_user"])
                            destination_bot = Bot(token='6682205213:AAFFV1avM8cVCZhgv-K8pzKeJ_c20Wle_P4')
                            await destination_bot.send_message(chat_id, f'Заявка с ID: {id_ship} завершена!\nПринял груз: {message.text}\n\n'
                                                                        f'Тип: *{list_ship["type_ship"]}*\n'
                                                                        f'Предмет: *{list_ship["item_ship"]}*\n'
                                                                        f'Адрес загрузки: *{list_ship["adress_begin"]}*\n'
                                                                        f'Время загрузки: *{list_ship["begin_ship"]}*\n\n'
                                                                        f'Адрес разгрузки: *{list_ship["adress_end"]}*\n'
                                                                        f'Время разгрузки: *{list_ship["end_ship"]}*\n', parse_mode='Markdown')

                        except Exception as e:
                            await bot.send_message(-4077236615, f'🚚 Бот логистики\n\n{user}\nОшибка 882\n{str(user1["id_user"])}\n{e}\n\nПользователь написал: {message.text}')

                    update(f"UPDATE shipping SET status_ship = 'Закончен' WHERE id_ship = '{id_ship}'", user)


                    id_car = list_ship["car_id"]
                    if id_car != 0:
                        delta_1 = datetime.timedelta(hours=5)
                        now = datetime.datetime.now() + delta_1
                        mes = f'{now.hour}:{now.minute} | {now.day}.{now.month}.{now.year}'

                        list_fbo = selist(f"SELECT * FROM fbo WHERE car_id = '{id_car}' and ff_city = 0", user)

                        for i in list_fbo:
                            if i['own_fbo'] != 0:
                                fbo_id = i['fbo_id']
                                update(f"UPDATE new_fbo SET status = 4 WHERE id_fbo = '{fbo_id}'", user)
                                id_client = selone(f"SELECT own_fbo FROM fbo WHERE fbo_id = '{fbo_id}'", user)['own_fbo']
                                try:
                                    nons = selone(f"SELECT nons FROM new_fbo WHERE id_fbo = '{int(fbo_id)}'", user)['nons']
                                    status_zakaz = 4
                                    update(f"UPDATE new_fbo SET status_zakaz = '{status_zakaz}' WHERE nons = '{nons}'", user)
                                    list_zakaz = selist(f"SELECT * FROM new_fbo WHERE nons = '{nons}'", user)
                                    id_user = list_zakaz[0]["own_zakaz"]
                                    list_client = selist(f"SELECT * FROM clients WHERE id_user = '{id_user}'", user)

                                    if list_zakaz[0]["status_zakaz"] == 80:
                                        status_zakaz = 'Не принято на фулфилменте'
                                    elif list_zakaz[0]["status_zakaz"] == 100:
                                        status_zakaz = 'Отменен'
                                    elif list_zakaz[0]["status_zakaz"] == 0:
                                        status_zakaz = 'Принято на фулфилменте'
                                    elif list_zakaz[0]["status_zakaz"] == 1:
                                        status_zakaz = 'Обработка...'
                                    elif list_zakaz[0]["status_zakaz"] == 2:
                                        status_zakaz = 'Готов к отправке'
                                    elif list_zakaz[0]["status_zakaz"] == 3:
                                        status_zakaz = 'Доставка...'
                                    elif list_zakaz[0]["status_zakaz"] == 4:
                                        status_zakaz = 'Доставлен'
                                    elif list_zakaz[0]["status_zakaz"] == 5:
                                        status_zakaz = 'Не принято на складе. Обработка...'

                                    zakaz_text = f'У Вашей заявки с ID {list_zakaz[0]["id_zakaz"]} изменился статус!\n' \
                                                 f'\n<i>Склад отправки:</i> <b>{list_zakaz[0]["city"]}</b>' \
                                                 f'\n<i>Количество товара:</i> <b>{list_zakaz[0]["count_items"]}</b>' \
                                                 f'\n<i>Статус:</i> <b>{status_zakaz}</b>'

                                    try:
                                        chat_id = str(id_user)
                                        destination_bot = Bot(token='6220819545:AAFS7TBQlmaZfpBEyoooOL-ac0YZQFxzec0')
                                        await destination_bot.send_message(chat_id, zakaz_text, parse_mode='html')
                                    except:
                                        pass
                                except:
                                    pass

                        update(f"UPDATE cars SET gate = '0' WHERE car_id = '{id_car}'", user)
                        update(f"UPDATE cars SET fact_end_date = '{mes}' WHERE car_id = '{id_car}'", user)


                    l = selist(f"SELECT * FROM shipping WHERE id_ship = '{id_ship}'", user)[0]
                    if l["type_ship"] == 'Внутренняя' and (l["item_ship"] == 'Растущий стол и стул 1' or l["item_ship"] == 'Растущий стол и стул 2' or l["item_ship"] == 'Наполнитель 15 кг' or l["item_ship"] == 'Парящие полки') and l["adress_end"] == 'Сафроновский проезд 6 (ФФ)':
                        delta_1 = datetime.timedelta(hours=5)
                        now = datetime.datetime.now() + delta_1
                        if int(now.day) < 10:
                            day_edit = '0' + str(now.day)
                        else:
                            day_edit = now.day

                        if int(now.month) < 10:
                            month_edit = '0' + str(now.month)
                        else:
                            month_edit = now.month
                        date_create = f'{day_edit}.{month_edit}.{now.year}'

                        name_list = f"Складской учет"

                        worksheet = sh.worksheet(name_list)

                        values_list = worksheet.col_values(2)
                        num_row = len(values_list) + 1
                        item_m = l["item_ship"]
                        worksheet.update_cell(num_row, 2, date_create)
                        worksheet.update_cell(num_row, 3, "ЦЕХ")
                        worksheet.update_cell(num_row, 6, "Фулфилмент")
                        worksheet.update_cell(num_row, 9, '-')
                        worksheet.update_cell(num_row, 15, l["count_item_ship"])
                        worksheet.update_cell(num_row, 11, item_m)

                    if l["type_ship"] == 'Доставка' and (l["item_ship"] == 'Растущий стол и стул 1' or l["item_ship"] == 'Растущий стол и стул 2' or l["item_ship"] == 'Наполнитель 15 кг' or l["item_ship"] == 'Парящие полки') and l["adress_begin"] == 'Сафроновский проезд 6 (ФФ)':
                        delta_1 = datetime.timedelta(hours=5)
                        now = datetime.datetime.now() + delta_1
                        if int(now.day) < 10:
                            day_edit = '0' + str(now.day)
                        else:
                            day_edit = now.day

                        if int(now.month) < 10:
                            month_edit = '0' + str(now.month)
                        else:
                            month_edit = now.month
                        date_create = f'{day_edit}.{month_edit}.{now.year}'

                        name_list = f"Складской учет"

                        worksheet = sh.worksheet(name_list)

                        values_list = worksheet.col_values(2)
                        num_row = len(values_list) + 1
                        item_m = l["item_ship"]
                        worksheet.update_cell(num_row, 2, date_create)
                        worksheet.update_cell(num_row, 3, "Фулфилмент")
                        worksheet.update_cell(num_row, 6, "Авито")
                        worksheet.update_cell(num_row, 9, '-')
                        worksheet.update_cell(num_row, 15, l["count_item_ship"])
                        worksheet.update_cell(num_row, 11, item_m)


                    if l["type_ship"] == 'Забор' and l["nons"] != '0':
                        nons_us = l["nons"]
                        update(f"UPDATE new_fbo SET status_zakaz = 80 WHERE nons = '{nons_us}'", user)

                        list_zakaz = selist(f"SELECT * FROM new_fbo WHERE nons = '{nons_us}'", user)
                        id_user = list_zakaz[0]["own_zakaz"]
                        list_client = selist(f"SELECT * FROM clients WHERE id_user = '{id_user}'", user)

                        zakaz_text = f'Ваша заявка с ID {list_zakaz[0]["id_zakaz"]} доставлена на фулфилмент!\n' \
                                     f'\n<i>Склад отправки:</i> <b>{list_zakaz[0]["city"]}</b>' \
                                     f'\n<i>Количество товара:</i> <b>{list_zakaz[0]["count_items"]}</b>' \
                                     f'\n<i>Статус:</i> <b>Ожидает приемки</b>'

                        try:
                            chat_id = str(id_user)
                            destination_bot = Bot(token='6220819545:AAFS7TBQlmaZfpBEyoooOL-ac0YZQFxzec0')
                            await destination_bot.send_message(chat_id, zakaz_text, parse_mode='html')
                        except Exception as e:
                            await bot.send_message(-4077236615, f'🚚 Бот логистики\n\n{user}\nОшибка 907\n{e}')

                    await message.answer(text='Заявка завершена! ', reply_markup=markups.menu_log_n)

                # Забрал возвраты
                elif message.text == markups.menu_log_b6:
                    update(f"UPDATE users SET act_log = ' ' WHERE id_user = '{user}'", user)
                    list_items = selist(f"SELECT * FROM warehouse_refunds", user)
                    inline_key = InlineKeyboardMarkup(row_width=1)
                    await message.answer(text='Какую позицию забрали?', reply_markup=markups.back)
                    for i in list_items:
                        inline_key_b1 = InlineKeyboardButton(text=i["name_item"], callback_data=f'ref_{i["id_item"]}')
                        inline_key.add(inline_key_b1)
                    await message.answer(text='Выберите из списка:', reply_markup=inline_key)
                elif 'ref_' in selone(f"SELECT act_log FROM users WHERE id_user = '{user}'", user)['act_log']:
                    if message.text.isdigit():
                        id_item = selone(f"SELECT act_log FROM users WHERE id_user = '{user}'", user)['act_log'].split('_')[1]
                        update(f"UPDATE users SET act_log = ' ' WHERE id_user = '{user}'", user)
                        voz = int(message.text)
                        count_v = selone(f"SELECT count_item FROM warehouse_refunds WHERE id_item = '{id_item}'", user)['count_item']
                        update(f"UPDATE warehouse_refunds SET count_item = '{int(count_v) + int(voz)}' WHERE id_item = '{id_item}'", user)
                        name_item = selone(f"SELECT name_item FROM warehouse_refunds WHERE id_item = '{id_item}'", user)['name_item']
                        list_all_users = selist(f"SELECT * FROM users WHERE company = 'Менеджер МП' OR company = 'Босс'", user)
                        list_users = []
                        await message.answer(text='Готово', reply_markup=markups.menu_log_n)
                        for us in list_all_users:
                            if 'men' in us['notif']:
                                list_users.append(us)
                        for user1 in list_users:
                            try:
                                chat_id = str(user1["id_user"])
                                destination_bot = Bot(token='6629342340:AAG_DI1HQprpkkA5Ruwfd3E6kLO4tmdbXfw')
                                await destination_bot.send_message(chat_id, f'*Водитель забрал возвраты!*\n\n'
                                                                            f'Позиция: *{name_item}*\n'
                                                                            f'Количество: *{voz}*\n', parse_mode='Markdown')
                            except Exception as e:
                                await bot.send_message(-4077236615,
                                                       f'🚚 Бот логистики\n\n{user}\nОшибка 1225\n{str(user1["id_user"])}\n{e}')
                    else:
                        await message.answer(text='Введите количество числом!')

                # НДЗ
                elif message.text == markups.menu_log_b5:
                    if selone(f"SELECT date_work FROM work_drive WHERE date_work = '{sk.date_create()}'", user) is None:
                            await message.answer(text='Вчерашняя смена не была закрыта! Обратитесь к руководителю!')
                    else:
                        if len(selist(f"SELECT * FROM shipping WHERE date_ship = '{datework}' AND status_ship = 'Не дозвонился'", user)) != 0:
                            await message.answer(text='*Очередь заявок НДЗ:*', reply_markup=markups.back)
                            newlist = selist(f"SELECT * FROM shipping WHERE date_ship = '{datework}' AND status_ship = 'Не дозвонился'", user)
                            id_list = []
                            list_log = sorted(newlist, key=lambda d: d['num_ship'])
                            for l in list_log:
                                inline_m = InlineKeyboardMarkup(row_width=2)
                                inline_m_b1 = InlineKeyboardButton(text='Принять', callback_data=f'access_{l["id_ship"]}')
                                inline_m_b2 = InlineKeyboardButton(text='Отмена заявки', callback_data=f'cancel_{l["id_ship"]}')
                                inline_m_b3 = InlineKeyboardButton(text='Перенос', callback_data=f'edite_{l["id_ship"]}')
                                inline_m.add(inline_m_b1).add(inline_m_b2).add(inline_m_b3)
                                msg = await message.answer(text=f'ID: *{l["id_ship"]}*\n'
                                                          f'Тип: *{l["type_ship"]}*\n'
                                                          f'Дата: *{l["date_ship"]}*\n'
                                                          f'Время: *{l["time_ship"]}*\n'
                                                          f'Предмет: *{l["item_ship"]}*\n'
                                                          f'Количество: *{l["count_item_ship"]}*\n'
                                                          f'Вес: *{l["w_ship"]}*\n\n'
                                                          f'Адрес загрузки: `{l["adress_begin"]}`\n'
                                                          f'Телефон загрузки: `{l["phone_begin"]}`\n'
                                                          f'Адрес разгрузки: `{l["adress_end"]}`\n'
                                                          f'Телефон разгрузки: `{l["phone_end"]}`\n'
                                                          f'Комментарий: *{l["comment_ship"]}*\n\n'
                                                          f'Статус: *{l["status_ship"]}*', parse_mode='Markdown', reply_markup=inline_m)
                                id_list.append(str(msg.message_id))

                            str_id_list = '_'.join(id_list)
                            update(f"UPDATE users SET id_list = '{str_id_list}' WHERE id_user = '{user}'", user)

                        else:
                            await message.answer(text='*Очередь заявок НДЗ пуста*')

                # Не понятно
                else:
                    await message.answer(text='Я вас не понял')



if __name__ == '__main__':
    executor.start_polling(db, on_startup=startup, skip_updates=True)