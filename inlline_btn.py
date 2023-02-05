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

def show_groups(a, index_page): # передаём в функцию data
    show_groups = InlineKeyboardMarkup(row_width=4)
    if index_page == '1':
        for i in a[0:44]: # цикл для создания кнопок
            show_groups.insert(InlineKeyboardButton(i, callback_data=i))

    elif index_page == '2':
        for i in a[44:88]: # цикл для создания кнопок
            show_groups.insert(InlineKeyboardButton(i, callback_data=i))

    elif index_page == '3':
        for i in a[88:132]:  # цикл для создания кнопок
            show_groups.insert(InlineKeyboardButton(i, callback_data=i))

    elif index_page == '4':
        for i in a[132:176]:  # цикл для создания кнопок
            show_groups.insert(InlineKeyboardButton(i, callback_data=i))

    elif index_page == '5':
        for i in a[176:220]:  # цикл для создания кнопок
            show_groups.insert(InlineKeyboardButton(i, callback_data=i))

    elif index_page == '6':
        for i in a[220:264]:  # цикл для создания кнопок
            show_groups.insert(InlineKeyboardButton(i, callback_data=i))

    elif index_page == '7':
        for i in a[264:308]:  # цикл для создания кнопок
            show_groups.insert(InlineKeyboardButton(i, callback_data=i))

    elif index_page == '8':
        for i in a[308:352]:  # цикл для создания кнопок
            show_groups.insert(InlineKeyboardButton(i, callback_data=i))


    in_btn_1 = InlineKeyboardButton(text='-1-', callback_data='1')
    in_btn_2 = InlineKeyboardButton(text='-2-', callback_data='2')
    in_btn_3 = InlineKeyboardButton(text='-3-', callback_data='3')
    in_btn_4 = InlineKeyboardButton(text='-4-', callback_data='4')
    in_btn_5 = InlineKeyboardButton(text='-5-', callback_data='5')
    in_btn_6 = InlineKeyboardButton(text='-6-', callback_data='6')
    in_btn_7 = InlineKeyboardButton(text='-7-', callback_data='7')
    in_btn_8 = InlineKeyboardButton(text='-8-', callback_data='8')

    show_groups.insert(in_btn_1)
    show_groups.insert(in_btn_2)
    show_groups.insert(in_btn_3)
    show_groups.insert(in_btn_4)
    show_groups.insert(in_btn_5)
    show_groups.insert(in_btn_6)
    show_groups.insert(in_btn_7)
    show_groups.insert(in_btn_8)

    return show_groups#возвращаем клавиатуру
