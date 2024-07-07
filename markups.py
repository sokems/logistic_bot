from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

menu_main = '🗓 Главное меню'
menu_back = 'Отмена ❌'

main_menu = ReplyKeyboardMarkup(resize_keyboard=True)
main_menu.add(menu_main)

menu_log = ReplyKeyboardMarkup(resize_keyboard=True)
menu_log_b = ReplyKeyboardMarkup(resize_keyboard=True)
menu_log_n = ReplyKeyboardMarkup(resize_keyboard=True)
menu_log_b1 = '⬇️ Загрузки'
menu_log_b2 = '✅ Разгрузки'
menu_log_b3 = '🔒 Закрыть смену'
menu_log_b4 = '🔐 Открыть смену'
menu_log_b5 = '❓ НДЗ'
menu_log_b6 = '📦 Забрал возврат'
menu_log.add(menu_log_b1, menu_log_b2).add(menu_log_b5, menu_log_b6).add(menu_log_b4)
menu_log_n.add(menu_log_b1, menu_log_b2).add(menu_log_b5, menu_log_b6).add(menu_log_b3)
menu_log_b.add(menu_log_b4)

menu_none = ReplyKeyboardMarkup(resize_keyboard=True)
menu_none_b1 = '...'
menu_none.add(menu_none_b1)

back = ReplyKeyboardMarkup(resize_keyboard=True)
back.add(menu_back)
