import requests
from bs4 import BeautifulSoup
import output_couples as oc

link = "https://isu.ugatu.su/api/new_schedule_api/?schedule_semestr_id=222&WhatShow=1&student_group_id=1557"
responce = requests.get(link).text
soup = BeautifulSoup(responce, 'lxml')

tbody_block = soup.find('tbody') #Тело таблицы там усе
lesson = tbody_block.find_all('tr')
check_lessik = tbody_block.find_all('td')

week = input("Введи неделю: ")
day_week = input("Введите день недели: ")


"""Штука высчитывает сколько строк с парами есть в этот день и передает их в функцию для вывода,
Чтобы функция вывода не выходила за рамки вызываемого дня"""

if day_week == "Понедельник": #Если чувак написал Понедельник
    j = 0 #Переменная помогающая найти строку вызываего дня
    for i in check_lessik: #Пербором находим нужный день

        if check_lessik[j].text == "Понедельник":
            num = 1 #перемменая которая содержит количество строк с парами в этот день(везде разное)
            index = 0 #переменная которая показывает функции вывода откуда(с какой позиции td) нужно начинать

            for i in check_lessik: #Перебор строк для счета количества строк
                # print(check_less[index].text)

                if check_lessik[index].text == "" and (check_lessik[index-1].text == "" or
                                                       check_lessik[index-1].text == "Нет информации"):
                    index += 1
                    num += 1
                elif check_lessik[index].text == "Вторник": #Если дошел до строки Вторник остановись
                    break
                else:
                    index += 1
        else:
            j+=1
    print(num)
    oc.ras_less(num, 0, week, lesson)

elif day_week == "Вторник":
    j = 0
    for i in check_lessik:
        if check_lessik[j].text == "Вторник":
            num = 1
            index = j
            for i in check_lessik:
                # print(check_lessik[index].text)
                if check_lessik[index].text == "" and (check_lessik[index - 1].text == "" or
                                                       check_lessik[index - 1].text == "Нет информации"):
                    index += 1
                    num += 1
                elif check_lessik[index].text == "Среда":
                    break
                else:
                    index += 1
        else:
            j += 1
    print(num)
    oc.ras_less(num, 14, week)

elif day_week == "Среда":
    index = 20
    oc.ras_less(index, week)
elif day_week == "Четверг":
    index = 34
    oc.ras_less(index, week)
elif day_week == "Пятница":
    index = 30
    oc.ras_less(index, week)