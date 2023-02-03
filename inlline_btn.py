from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

#кнопка с callback
main_btn = InlineKeyboardMarkup(row_width = 6)#указываем сколько кнопок будет в одной строке

in_btn_m = InlineKeyboardButton(text = 'ПН', callback_data = 'monday')
in_btn_tu = InlineKeyboardButton(text = 'ВТ', callback_data = 'tuesday')
in_btn_w = InlineKeyboardButton(text = 'СР', callback_data = 'wednesday')
in_btn_th = InlineKeyboardButton(text = 'ЧТ', callback_data = 'thursday')
in_btn_f = InlineKeyboardButton(text = 'ПТ', callback_data = 'friday')
in_btn_s = InlineKeyboardButton(text = 'СБ', callback_data = 'saturday')
# in_btn_url = InlineKeyboardButton(text = 'Перейти на канал', url = 'https://t.me/infaPRO_botov') #кнопка с сылкой
# in_btn_share = InlineKeyboardMarkup(text = 'Поделиться ботом с друзьями:', switch_inline_query = 'Это не плохой бот: ')

main_btn.insert(in_btn_m)
main_btn.insert(in_btn_tu)
main_btn.insert(in_btn_w)
main_btn.insert(in_btn_th)
main_btn.insert(in_btn_f)
main_btn.insert(in_btn_s)
# main_btn.insert(in_btn_url)
