import requests
from bs4 import BeautifulSoup

link = "https://isu.ugatu.su/api/new_schedule_api/?schedule_semestr_id=222&WhatShow=1&student_group_id=1557"
responce = requests.get(link).text
soup = BeautifulSoup(responce, 'lxml')

tbody_block = soup.find('tbody') #Тело таблицы там усе
week_days = tbody_block.find_all('tr', 'noinfo dayheader' and 'dayheader') #Споисок со всеми днями неделями(пока не используется)


'''
#Получаем названия дней недели, максимально топорно и тупо конечно
j = 0
for i in week_days:
    #print(week_days[j].find('td').text)
    j+=1
# check_wd = week_days[0].find_all('td')
'''


def ras_less(num, index, week): #метод для вывода собственно расписания
    num_less = 0  # эта
    last_time = 0  # и эта переменная введена для адекватного отображения списка

    for k in range(num):
        check_less = lesson[index].find_all('td')

        # print(last_time, check_less[1].text)

        if check_less[2].text == "Нет информации":#те случаи когда td имеет содержание "Нет информации"
            num_less += 1
            # Не может быть ситуации когда нет информации и повтор урока
            # Так что, тут проверку делать не обязательно
            # print(f"Пара №{num_less } - {check_less[1].text} - Pizda")
            last_time = check_less[1].text
        else:
            if last_time != check_less[1].text:
                num_less += 1
                if str(week) in check_less[2].text:
                    print(
                        f"Пара №{num_less} - {check_less[1].text} #{check_less[4].text}# {check_less[3].text} - {check_less[5].text} - {check_less[6].text}")
                    last_time = check_less[1].text
                # else:
                # Когда по уроку не "нет информации", а не совпадают по датам
                # print(f"Пара №{num_less} - {check_less[1].text} - Bebra")
                last_time = check_less[1].text
                # num_less += 1
            else:
                if str(week) in check_less[2].text:
                    print(
                        f"Пара №{num_less} - {check_less[1].text} #{check_less[4].text}# {check_less[3].text} - {check_less[5].text} - {check_less[6].text}")
                else:
                    pass
                last_time = check_less[1].text
        index += 1

lesson = tbody_block.find_all('tr')
# check_less = tbody_block.find_all('td')

week = input("Введи неделю: ")
day_week = input("Введите день недели: ")

check_lessik = tbody_block.find_all('td')

if day_week == "Понедельник":
    j = 0
    for i in check_lessik:
        if check_lessik[j].text == "Понедельник":
            num = 1
            index = 0
            for i in check_lessik:
                # print(check_less[index].text)
                if check_lessik[index].text == "" and (check_lessik[index-1].text == "" or check_lessik[index-1].text == "Нет информации"):
                    index += 1
                    num += 1
                elif check_lessik[index].text == "Вторник":
                    break
                else:
                    index += 1
        else:
            j+=1
    print(num)
    ras_less(num, 0, week)

elif day_week == "Вторник":
    j = 0
    for i in check_lessik:
        if check_lessik[j].text == "Вторник":
            num = 1
            index = j
            for i in check_lessik:
                # print(check_lessik[index].text)
                if check_lessik[index].text == "" and (check_lessik[index - 1].text == "" or check_lessik[index - 1].text == "Нет информации"):
                    index += 1
                    num += 1
                elif check_lessik[index].text == "Среда":
                    break
                else:
                    index += 1
        else:
            j += 1
    print(num)
    ras_less(num, 14, week)

elif day_week == "Среда":
    index = 20
    ras_less(index, week)
elif day_week == "Четверг":
    index = 34
    ras_less(index, week)
elif day_week == "Пятница":
    index = 30
    ras_less(index, week)