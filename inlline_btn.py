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

def show_options(var): #если при вводе группа не нашлась, предлагать 3 варианта
    show_groups = InlineKeyboardMarkup(row_width=3)
    for i in var:  # цикл для создания кнопок
        print(i[0])
        show_groups.insert(InlineKeyboardButton(i[0], callback_data=i[0]))

    edit = InlineKeyboardButton(text='Ввести группу снова', callback_data='edit')
    show_groups.insert(edit)

    return show_groups # возвращаем клавиатуру

def show_weeks(now_week): #если при вводе группа не нашлась, предлагать 3 варианта
    show_week = InlineKeyboardMarkup(row_width=3)

    show_week.insert(InlineKeyboardButton(now_week, callback_data=now_week))
    show_week.insert(InlineKeyboardButton(str(int(now_week)+1), callback_data=str(int(now_week)+1)))
    show_week.insert(InlineKeyboardButton(str(int(now_week)+2), callback_data=str(int(now_week)+2)))

    return show_week # возвращаем клавиатуру

def change_group(): #если при вводе группа не нашлась, предлагать 3 варианта
    change_btn = InlineKeyboardMarkup(row_width=1)

    change_btn.insert(InlineKeyboardButton("Изменить группу", callback_data= 'change_group'))

    return change_btn # возвращаем клавиатуру

