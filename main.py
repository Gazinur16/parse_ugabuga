from config import TOKEN
import logging
from aiogram import Bot, Dispatcher, executor, types
from datetime import datetime
from db import Database
import nums_from_string
from fuzzywuzzy import process

import inlline_btn as inline_kb #импортируем из файла инлайн кнопки
import btn_response as btn_res

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
db = Database('database.db')

#Статические поля(типа)
str_week = btn_res.get_week()
num_week = nums_from_string.get_nums(str_week) #номер текушей недели

#Методы:
async def output_schedule(str_date, day):  #Метод для отображения расписания
    mass = []
    f = 0
    for i in str_date:
        for j in i:
            if f == len(str_date):
                break
            k = 0

            a = (f"*Пара №{str_date[f][k]} {str_date[f][k + 1]}* \n> {str_date[f][k + 2]}: "
                 f"{str_date[f][k + 3]} - {str_date[f][k + 4]} - {str_date[f][k + 5]}\n\n")
            mass.append(a)
            f += 1
            # print(f)
    #TODO день недели с числом
    header_mess = f"*{day}*"
    couples = '\n\n' + ''.join(mass)
    if len(mass) == 0:
        couples = "\n\n"+"_> Похоже сегодня пар нет._"
    mess = header_mess + couples
    return mess

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    if message.chat.type == 'private':

        if not db.user_exists(message.from_user.id): #Провеерка что у User`а нет
            db.add_user(message.from_user.id)#Если нет, добавляем id и выводим сообщение с просьбой написать группу
            await bot.send_message(message.from_user.id, 'Добро пожаловать в бота расписаний!\n'
                                                         'Напиши свою группу в формате: ГРУППА-НОМЕР(Б)', parse_mode="Markdown")
        elif db.check_group(message.from_user.id): #Если id есть но группа не выбрана
            await bot.send_message(message.from_user.id, 'C возвращением!\n'
                                                         'Напиши свою группу в формате: ГРУППА-НОМЕР(Б)', parse_mode="Markdown")
        else:
            name_group = db.get_name_group(message.from_user.id)#если группа есть, получаем ее
            btn_res.get_id_group(name_group) # обновляем ссылку для парсинга
            await bot.send_message(message.from_user.id, f"С возвращением, ваша группа: *{name_group}*", parse_mode="Markdown")

@dp.message_handler(commands=['profile'])
async def profile(message: types.Message):
    if message.chat.type == 'private':
        # TODO добавить возможность изменить группу
        if db.check_group(message.from_user.id):
            await bot.delete_message(message.from_user.id, message.message_id)
            await bot.send_message(message.from_user.id, f"Вы еще не выбрали группу.")
        else:
            name_group = db.get_name_group(message.from_user.id)
            await bot.send_message(message.from_user.id, f"Твоя группа: *{name_group}*", parse_mode="Markdown")
            await bot.send_message(message.from_user.id, f"Скоро будет возможность менять группу")

@dp.message_handler(commands=['today'])
async def today(message: types.Message):
    if message.chat.type == 'private':
        if db.check_group(message.from_user.id):
            await bot.delete_message(message.from_user.id, message.message_id)
            await bot.send_message(message.from_user.id, f"Вы еще не выбрали группу.")
        else:
            now = datetime.now()
            weekday = datetime.weekday(now) #Узнаем день недели

            if weekday == 0:  # monday
                str_date = btn_res.monday(num_week[0])
                mess = await output_schedule(str_date, "Понедельник")
                await bot.send_message(message.from_user.id, mess, parse_mode="Markdown")

            elif weekday == 1:  # tuesday
                str_date = btn_res.tuesday(num_week[0])
                mess = await output_schedule(str_date, "Вторник")
                await bot.send_message(message.from_user.id, mess, parse_mode="Markdown")

            elif weekday == 2:  # wednesday
                str_date = btn_res.wednesday(num_week[0])
                mess = await output_schedule(str_date, "Среда")
                await bot.send_message(message.from_user.id, mess, parse_mode="Markdown")

            elif weekday == 3:  # thursday
                str_date = btn_res.thursday(num_week[0])
                mess = await output_schedule(str_date, "Четверг")
                await bot.send_message(message.from_user.id, mess, parse_mode="Markdown")

            elif weekday == 4:  # friday
                str_date = btn_res.friday(num_week[0])
                mess = await output_schedule(str_date, "Пятница")
                # await bot.send_message(message.from_user.id, mess)
                await bot.send_message(message.from_user.id, mess, parse_mode="Markdown")

            elif weekday == 5:  # saturday
                str_date = btn_res.saturday(num_week[0])
                mess = await output_schedule(str_date, "Cуббота")
                await bot.send_message(message.from_user.id, mess, parse_mode="Markdown")
            else:
                await bot.send_message(message.from_user.id, "Сегодня же воскресенье, отдыхай!")

@dp.message_handler(commands=['by_group'])
async def by_group(message: types.Message):
    if message.chat.type == 'private':
        # TODO просьба вводить неделю(предлагать нынешнюю) и сделать проверку
        if db.check_group(message.from_user.id):
            await bot.delete_message(message.from_user.id, message.message_id)
            await bot.send_message(message.from_user.id, f"Вы еще не выбрали группу.")
        else:
            db.set_status(message.from_user.id, 'inweek')
            await bot.send_message(message.from_user.id, "Введи неделю на которе хотите посмотреть расписание: ")


@dp.message_handler(commands=['by_teacher'])
async def by_teacher(message: types.Message):
    if message.chat.type == 'private':
        if db.check_group(message.from_user.id):
            await bot.delete_message(message.from_user.id, message.message_id)
            await bot.send_message(message.from_user.id, f"Вы еще не выбрали группу.")
        else:
            # TODO нужно парсить данные с другого окна - сделаю позже
            await bot.send_message(message.from_user.id, "Скоро тут все будет... наверное.")

@dp.message_handler(commands=['week'])
async def week(message: types.Message):
    if message.chat.type == 'private':
        await bot.send_message(message.from_user.id, f"{str_week}")

@dp.message_handler(commands=['help'])
async def help(message: types.Message):
    if message.chat.type == 'private':
        await bot.send_message(message.from_user.id, '''При ошибках, пишите мне @Cytire и попробуйте перезагрузить бота /start

Кратко о командах: 
/profile - выводит информацию о вашей группе, при необходимости тут можно поменять группу.
/today - выводить расписание вашей группы на сегодня.
/by_group - показывает недельное расписание по вашей группе.
/by_teacher - показывает расписание по преподу.
/week - показывает текущую неделю.

''')

# @dp.message_handler(commands=['news'])
# async def sendall(message: types.Message):
#     if message.chat.type == 'private':
#         if message.from_user.id == 817649215:
#             text = message.text[5:]
#             users = db.get_users()
#             for row in users:
#                 try:
#                     await bot.send_message(row[0], text)
#                     if int(row[1]) != 1:
#                         db.set_active(row[0], 1)
#                 except:
#                     db.set_active(row[0], 0)
#
#             await bot.send_message(message.from_user.id, "Успешная рассылка")

@dp.message_handler() #реакция на сообщения
async def send_btn(message: types.Message):

    if db.check_status(message.from_user.id) == 'durak':  # если у юзера статус дурак(не юзер дурак, а защита от дурака)
        await bot.delete_message(message.from_user.id, message.message_id)

    elif db.check_status(message.from_user.id) == 'regis': #если у юзера состояние регистрации
        group = message.text #группа которую ввел пользователь
        a = btn_res.get_groups() #массив из всех групп

        if a.count(group):
            db.set_name_group(message.from_user.id, group)  # записываем группу в БД
            btn_res.get_id_group(group)  # обновляем ссылку парсинга
            await bot.send_message(message.from_user.id,
                                   f"Вы ввели свою  группу: {group}\nТеперь вы можете посмотреть "
                                   f"расписание:\n\n/today - на сегодня\n/by_group - по неделям")
        else:
            options = process.extract(group, a, limit=3)
            await bot.send_message(message.from_user.id, f"Может быть вы имели ввиду: ",
                                    reply_markup=inline_kb.show_options(options))

        db.set_status(message.from_user.id, 'durak')# cразу даем статус дурака

    elif db.check_status(message.from_user.id) == 'inweek':
        print(message.text) #Введеная неделя
        global entered_week # сохраним для инлайн кнопок
        entered_week = message.text

        try:
            if int(message.text) and 22<=int(message.text)<=40:
                if message.text == str(num_week[0]): #Когда выбрана текущая неделя.
                    now = datetime.now()
                    weekday = datetime.weekday(now)# Узнаем день недели

                    if weekday == 0:  # monday
                        str_date = btn_res.monday(num_week[0])
                        mess = await output_schedule(str_date, "Понедельник")
                        await bot.send_message(message.from_user.id, mess,
                                                reply_markup=inline_kb.main_btn, parse_mode="Markdown")

                    elif weekday == 1:  # tuesday
                        str_date = btn_res.tuesday(num_week[0])
                        mess = await output_schedule(str_date, 'Вторник')
                        await bot.send_message(message.from_user.id, mess,
                                               reply_markup=inline_kb.main_btn,  parse_mode="Markdown")

                    elif weekday == 2:  # wednesday
                        str_date = btn_res.wednesday(num_week[0])
                        mess = await output_schedule(str_date, 'Среда')
                        await bot.send_message(message.from_user.id, mess,
                                               reply_markup=inline_kb.main_btn, parse_mode="Markdown")

                    elif weekday == 3:  # thursday
                        str_date = btn_res.thursday(num_week[0])
                        mess = await output_schedule(str_date, 'Четверг')
                        await bot.send_message(message.from_user.id, mess,
                                               reply_markup=inline_kb.main_btn,  parse_mode="Markdown")

                    elif weekday == 4:  # friday
                        str_date = btn_res.friday(num_week[0])
                        mess = await output_schedule(str_date, 'Пятница')
                        await bot.send_message(message.from_user.id, mess,
                                               reply_markup=inline_kb.main_btn, parse_mode="Markdown")

                    elif weekday == 5:  # saturday
                        str_date = btn_res.saturday(num_week[0])
                        mess = await output_schedule(str_date, "Cуббота")
                        await bot.send_message(message.from_user.id, mess,
                                               reply_markup=inline_kb.main_btn, parse_mode="Markdown")

                    elif weekday == 6:  # sunday
                        str_date = btn_res.monday(message.text)
                        mess = await output_schedule(str_date, "monday")
                        await bot.send_message(message.from_user.id, mess,
                                               reply_markup=inline_kb.main_btn, parse_mode="Markdown")

                else: #Если неделя не текущая начинаем с понедельника
                    str_date = btn_res.monday(message.text)
                    mess = await output_schedule(str_date, "monday")
                    await bot.send_message(message.from_user.id, mess,
                                           reply_markup=inline_kb.main_btn, parse_mode="Markdown")
            else:
                await bot.send_message(message.from_user.id, 'Выбрано неправильное значение недели.\n'
                                                             'Допустимые значения от 23 до 40.')
                await bot.delete_message(message.from_user.id, message.message_id)  # удаление последнего сообщения
        except:
            await bot.delete_message(message.from_user.id, message.message_id)  # удаление последнего сообщения
            await bot.send_message(message.from_user.id, 'Выбрано неправильное значение недели.\n'
                                                         'Допустимые значения от 23 до 40.')
    else:
        pass
    db.set_status(message.from_user.id, 'durak')
async def button(weekday): #Мне не нравится как я тут сделал, но пойдет
    if weekday == 'monday':
        str_date = btn_res.monday(entered_week)
    elif weekday == 'tuesday':
        str_date = btn_res.tuesday(entered_week)
    elif weekday == 'wednesday':
        str_date = btn_res.wednesday(entered_week)
    elif weekday == 'thursday':
        str_date = btn_res.thursday(entered_week)
    elif weekday == 'friday':
        str_date = btn_res.friday(entered_week)
    elif weekday == 'saturday':
        str_date = btn_res.saturday(entered_week)

    mess = await output_schedule(str_date, weekday)
    return mess

@dp.callback_query_handler(text = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']) #реакция на инлайн кнопку
async def info_bth(callback: types.CallbackQuery):
    weekday = callback.data
    #TODO попробовать не удалять последние сообщение а изменять его
    await bot.delete_message(callback.from_user.id, callback.message.message_id)# удаление последнего сообщения
    mess = await button(weekday)

    await bot.send_message(callback.from_user.id, mess,
                            reply_markup=inline_kb.main_btn, parse_mode="Markdown")

@dp.callback_query_handler(text = 'edit') #реакция на кнопку выбрать группу снова
async def info_bth(callback: types.CallbackQuery):
    await bot.send_message(callback.from_user.id, f"Введите группу снова: ")
    db.set_status(callback.from_user.id, 'regis') #возвращаем статус регистации
    await bot.delete_message(callback.from_user.id, callback.message.message_id)

@dp.callback_query_handler() #реакция на инлайн кнопку
async def info_bth(callback: types.CallbackQuery):
    await bot.delete_message(callback.from_user.id, callback.message.message_id)
    group = callback.data
    db.set_name_group(callback.from_user.id, group) #запись группы в БД
    btn_res.get_id_group(group) #обновление ссылки
    await bot.send_message(callback.from_user.id, f"Вы выбрали группу: {group}\nТеперь вы можете посмотреть "
                                                  f"расписание:\n\n/today - на сегодня\n/by_group - по неделям")

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates = True)