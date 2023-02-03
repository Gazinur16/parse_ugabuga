from config import TOKEN 
import logging
from aiogram import Bot, Dispatcher, executor, types
from datetime import datetime
from db import Database
import nums_from_string

import buttons as keyboard #импортируем кнопки из отдельного файла
import inlline_btn as inline_kb #импортируем из файла инлайн кнопки
import btn_response as btn_res

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
# db = Database('database.db')

#Статические поля(типа)
str_week = btn_res.get_week()
num_week = nums_from_string.get_nums(str_week) #номер текушей недели

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    if message.chat.type == 'private':
        #TODO тут будет проверка на созданный профиль

        # if not db.user_exists(message.from_user.id):
        #     db.add_user(message.from_user.id)
        await bot.send_message(message.from_user.id, "Привет, для начала введи свою группу: ")

@dp.message_handler(commands=['profile'])
async def start(message: types.Message):
    if message.chat.type == 'private':
        # TODO добавить возможность изменить группу

        # if not db.user_exists(message.from_user.id):
        #     db.add_user(message.from_user.id)
        await bot.send_message(message.from_user.id, "Твоя группа: ")

@dp.message_handler(commands=['today'])
async def start(message: types.Message):
    if message.chat.type == 'private':
        async def output_today(str_date): #Метод для отображения сегоднящнего расписания
            # print(str_date[0][0])
            mass = []
            f = 0
            for i in str_date:
                for j in i:
                    if f == len(str_date):
                        break
                    k = 0

                    a = (f"Пара №{str_date[f][k]} {str_date[f][k + 1]} \n{str_date[f][k + 2]}: "
                         f"{str_date[f][k + 3]} - {str_date[f][k + 4]} - {str_date[f][k + 5]}\n\n")
                    mass.append(a)
                    f += 1
                    # print(f)

            await bot.send_message(message.from_user.id, "Твое расписание на сегодня: " + '\n\n' + ''.join(mass))
            print(mass)

        now = datetime.now()
        weekday = datetime.weekday(now) #Узнаем день недели

        if weekday == 0: #monday
            str_date = btn_res.monday(num_week[0])
            await output_today(str_date)

        elif weekday == 1: #tuesday
            str_date = btn_res.tuesday(num_week[0])
            await output_today(str_date)

        elif weekday == 2: #wednesday
            str_date = btn_res.wednesday(num_week[0])
            await output_today(str_date)

        elif weekday == 3:  #thursday
            str_date = btn_res.thursday(num_week[0])
            await output_today(str_date)

        elif weekday == 4:  #friday
            str_date = btn_res.friday(num_week[0])
            await output_today(str_date)

        elif weekday == 5:  #saturday
            str_date = btn_res.saturday(num_week[0])
            await output_today(str_date)

@dp.message_handler(commands=['by_group'])
async def start(message: types.Message):
    if message.chat.type == 'private':
        # TODO просьба вводить неделю(предлагать нынешнюю) и отвечать расписанием на неделю
        #Проверить статус пользователся на то, что он делает запрос на неделю
        await bot.send_message(message.from_user.id, "Введи неделю: ")
        #Проверка на то что введена цифра



@dp.message_handler(commands=['by_teacher'])
async def start(message: types.Message):
    if message.chat.type == 'private':
        # TODO нужно парсить данные с другого окна - сделаю позже

        await bot.send_message(message.from_user.id, "Скоро тут все будет... наверное.")

@dp.message_handler(commands=['week'])
async def start(message: types.Message):
    if message.chat.type == 'private':
        await bot.send_message(message.from_user.id, f"{str_week}")

@dp.message_handler(commands=['help'])
async def start(message: types.Message):
    if message.chat.type == 'private':
        await bot.send_message(message.from_user.id, '''При ошибках, сперва попробуйте перезагрузить бота /start 
        Кратко о командах: 
        /profile - выводит информацию о вашей группе, при необходимости тут можно поменять группу.
        /today - выводить расписание вашей группы на сегодня.
        /by_group - показывает недельное расписание по вашей группе.
        /by_teacher - показывает расписание по преподу.
        /week - показывает текущую неделю.
        
        Код проекта находится на моем GitHub''')

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
    print(message.text)

    async def output_today(str_date):  #Метод для отображения сегодняшнего расписания
        # print(str_date[0][0])
        mass = []
        f = 0
        for i in str_date:
            for j in i:
                if f == len(str_date):
                    break
                k = 0

                a = (f"Пара №{str_date[f][k]} {str_date[f][k + 1]} \n{str_date[f][k + 2]}: "
                     f"{str_date[f][k + 3]} - {str_date[f][k + 4]} - {str_date[f][k + 5]}\n\n")
                mass.append(a)
                f += 1
                # print(f)

        await bot.send_message(message.from_user.id, "Твое расписание на неделю: " + '\n\n' + ''.join(mass),
                               reply_markup=inline_kb.main_btn)
        print(mass)

    if message.text == str(num_week[0]): #Когда выбрана текущая неделя.

        now = datetime.now()
        weekday = datetime.weekday(now)# Узнаем день недели

        if weekday == 0:  # monday
            str_date = btn_res.monday(num_week[0])
            await output_today(str_date)

        elif weekday == 1:  # tuesday
            str_date = btn_res.tuesday(num_week[0])
            await output_today(str_date)

        elif weekday == 2:  # wednesday
            str_date = btn_res.wednesday(num_week[0])
            await output_today(str_date)

        elif weekday == 3:  # thursday
            str_date = btn_res.thursday(num_week[0])
            await output_today(str_date)

        elif weekday == 4:  # friday
            str_date = btn_res.friday(num_week[0])
            await output_today(str_date)

        elif weekday == 5:  # saturday
            str_date = btn_res.saturday(num_week[0])
            await output_today(str_date)

    else: #Если неделя не текущая начинаем с понедельника
        str_date = btn_res.monday(message.text)
        await output_today(str_date)

# @dp.callback_query_handler(text = 'cat')#реакция на инлайн кнопку
# async def send_inll_btn(message: types.Message):
#     await bot.delete_message(message.from_user.id, message.message.message_id)#удаление последнего сообщения
#     await bot.send_message(message.from_user.id, 'Я не знаю почему программисты любят примеры с котиками, так сложилось)')
#     await bot.send_message(message.from_user.id, 'и то инлайн кнопки:' ,  reply_markup = inline_kb.main_btn)

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates = True)