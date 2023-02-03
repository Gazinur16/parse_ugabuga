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
num_week = nums_from_string.get_nums(str_week)

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
        # TODO распознавать какой сегодня день и на этой основе вызывать определенную функцию из btn_response

        await bot.send_message(message.from_user.id, "Твое расписание на сегодня: ")
        now = datetime.now()
        weekday = datetime.weekday(now)

        if weekday == 0: #monday
            str_date = btn_res.monday(num_week[0])
            await bot.send_message(message.from_user.id, f"Пара №{str_date[0]} {str_date[1]} \n{str_date[2]}: "
                                                         f"{str_date[3]} - {str_date[4]} - {str_date[5]}")
        elif weekday == 1: #tuesday
            str_date = btn_res.tuesday(num_week[0])
            await bot.send_message(message.from_user.id, f"Пара №{str_date[0]} {str_date[1]} \n{str_date[2]}: "
                                                         f"{str_date[3]} - {str_date[4]} - {str_date[5]}")
        elif weekday == 2: #wednesday
            str_date = btn_res.wednesday(num_week[0])
            await bot.send_message(message.from_user.id, f"Пара №{str_date[0]} {str_date[1]} \n{str_date[2]}: "
                                                         f"{str_date[3]} - {str_date[4]} - {str_date[5]}")
        elif weekday == 4:  #thursday
            str_date = btn_res.thursday(num_week[0])
            # print(str_date[0][0])
            mass = []
            for i in str_date:
                f = 0
                for j in i:
                    k = 0
                    await bot.send_message(message.from_user.id,
                                       f"Пара №{str_date[f][k]} {str_date[f][k + 1]} \n{str_date[f][k + 2]}: "
                                       f"{str_date[f][k + 3]} - {str_date[f][k + 4]} - {str_date[f][k + 5]}")

                    # a = (f"Пара №{str_date[f][k]} {str_date[f][k + 1]} \n{str_date[f][k + 2]}: "
                    #            f"{str_date[f][k + 3]} - {str_date[f][k + 4]} - {str_date[f][k + 5]}\n")
                    # mass.append((f"Пара №{str_date[f][k]} {str_date[f][k + 1]} \n{str_date[f][k + 2]}: "
                    #            f"{str_date[f][k + 3]} - {str_date[f][k + 4]} - {str_date[f][k + 5]}\n"))
                    f+=1


            # await bot.send_message(message.from_user.id,
            #                    f"Пара №{str_date[f][k]} {str_date[f][k + 1]} \n{str_date[f][k + 2]}: "
            #                    f"{str_date[f][k + 3]} - {str_date[f][k + 4]} - {str_date[f][k + 5]}")
            #await bot.send_message(message.from_user.id,mass)
            # print(mass)

        elif weekday == 4:  #friday
            str_date = btn_res.friday(num_week[0])
            await bot.send_message(message.from_user.id, f"Пара №{str_date[0]} {str_date[1]} \n{str_date[2]}: "
                                                         f"{str_date[3]} - {str_date[4]} - {str_date[5]}")
        elif weekday == 5:  #saturday
            str_date = btn_res.saturday(num_week[0])
            await bot.send_message(message.from_user.id, f"Пара №{str_date[0]} {str_date[1]} \n{str_date[2]}: "
                                                         f"{str_date[3]} - {str_date[4]} - {str_date[5]}")

@dp.message_handler(commands=['by_group'])
async def start(message: types.Message):
    if message.chat.type == 'private':
        # TODO просьба вводить неделю(предлагать нынешнюю) и отвечать расписанием на неделю

        await bot.send_message(message.from_user.id, "Твое расписание на неделю N{week}: ")

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

'''
@dp.message_handler() #реакция на кнопки
async def send_btn(message: types.Message):
    if message.text == 'Кнопка2':
        await bot.send_message(message.from_user.id, txt.text2)
        await bot.send_message(message.from_user.id, 'А это инлайн кнопка:' ,  reply_markup = inline_kb.main_btn)
    elif message.text == 'Кнопка1':
        await bot.send_message(message.from_user.id, txt.text1)
    elif message.text == 'Ваш товар':
        await bot.send_message(message.from_user.id, 'ИНФОРМАЦИЯ о Вашем товаре!')
    elif message.text == 'Информация о вашей услуге':
        await bot.send_message(message.from_user.id, 'Я не знаю какая у вас услуга, поэтому это поле пока пустует :(')
    elif message.text == 'Ваш текст':
        await bot.send_message(message.from_user.id, f'Скоро тут будет ваш текст, но пока тут еще один отрывок из "Мастер и Маргарита": \n\n  {txt.text3}')
    elif message.text == 'Далее:':
        await bot.send_message(message.from_user.id, 'Подменю:', reply_markup = keyboard.shou_btn2)#вызываем подменю
    elif message.text == 'Ваши контакты':
        await bot.send_message(message.from_user.id, txt.text4)
    elif message.text == 'Ваши картинки':
        await bot.send_message(message.from_user.id, 'Ваших картинок у меня нет, поэтому тут котик')
        photo1 = open('cat.jpg','rb')
        await bot.send_photo(chat_id=message.chat.id, photo=photo1)
    elif message.text == 'Ваши данные':
        await bot.send_message(message.from_user.id, 'Я их скоро получу)))')
    elif message.text == 'Оплата':
        await bot.send_message(message.from_user.id, 'В дальнейшем можно будет сделать оплату прямо через бота на ваш Киви')
    elif message.text == 'Назад:':
        await bot.send_message(message.from_user.id, 'Назад', reply_markup = keyboard.shou_btn)
'''
# @dp.callback_query_handler(text = 'cat')#реакция на инлайн кнопку
# async def send_inll_btn(message: types.Message):
#     await bot.delete_message(message.from_user.id, message.message.message_id)#удаление последнего сообщения
#     await bot.send_message(message.from_user.id, 'Я не знаю почему программисты любят примеры с котиками, так сложилось)')
#     await bot.send_message(message.from_user.id, 'и то инлайн кнопки:' ,  reply_markup = inline_kb.main_btn)

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates = True)