import requests
from bs4 import BeautifulSoup
import output_couples as oc

link = "https://isu.ugatu.su/api/new_schedule_api/?schedule_semestr_id=222&WhatShow=1&student_group_id=1557"
responce = requests.get(link).text
soup = BeautifulSoup(responce, 'lxml')

tbody_block = soup.find('tbody') #Тело таблицы там усе
lesson = tbody_block.find_all('tr')
check_lessik = tbody_block.find_all('td')

def get_week():
    str_week = soup.find('div', 'col-lg-3').text
    return str_week

"""Штука высчитывает сколько строк с парами есть в этот день и передает их в функцию для вывода,
Чтобы функция вывода не выходила за рамки вызываемого дня"""

def monday(week): #Если чувак написал Понедельник
    position = 0
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
    # print(num)
    # print(position)
    return oc.ras_less(num, position, week, lesson)

def tuesday(week):
    position = 1
    j = 0
    for i in check_lessik:
        if check_lessik[j].text == "" and (check_lessik[j - 1].text == "" or
                                           check_lessik[j - 1].text == "Нет информации"):
            position += 1

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
    # print(position)
    # print(num)
    return oc.ras_less(num, position, week, lesson)

def wednesday(week):
    position = 1
    j = 0
    for i in check_lessik:
        if (check_lessik[j].text == ""  and (check_lessik[j - 1].text == "" or
                                           check_lessik[j - 1].text == "Нет информации")) or check_lessik[j].text == "Вторник":
            position += 1

        if check_lessik[j].text == "Среда":
            num = 1
            index = j
            for i in check_lessik:
                # print(check_lessik[index].text)
                if check_lessik[index].text == "" and (check_lessik[index - 1].text == "" or
                                                       check_lessik[index - 1].text == "Нет информации"):
                    index += 1
                    num += 1
                elif check_lessik[index].text == "Четверг":
                    break
                else:
                    index += 1
        else:
            j += 1
    # print(position)
    # print(num)
    return oc.ras_less(num, position , week, lesson)

def thursday(week):
    position = 1
    j = 0
    for i in check_lessik:
        if (check_lessik[j].text == "" and (check_lessik[j - 1].text == "" or
                                           check_lessik[j - 1].text == "Нет информации")) or \
                check_lessik[j].text == "Вторник" or check_lessik[j].text == "Среда":
            position += 1

        if check_lessik[j].text == "Четверг":
            num = 1
            index = j
            for i in check_lessik:
                # print(check_lessik[index].text)
                if (check_lessik[index].text == "" and (check_lessik[index - 1].text == "" or
                                                       check_lessik[index - 1].text == "Нет информации")):
                    index += 1
                    num += 1
                elif check_lessik[index].text == "Пятница":
                    break
                else:
                    index += 1
        else:
            j += 1
    # print(position)
    # print(num)
    return oc.ras_less(num, position, week, lesson)

def friday(week):
    position = 1
    j = 0
    for i in check_lessik:
        if check_lessik[j].text == "" and (check_lessik[j - 1].text == "" or
                                           check_lessik[j - 1].text == "Нет информации") or \
                        check_lessik[j].text == "Вторник" or check_lessik[j].text == "Среда" or check_lessik[j].text == "Четверг":
            position += 1

        if check_lessik[j].text == "Пятница":
            num = 1
            index = j
            for i in check_lessik:
                # print(check_lessik[index].text)
                if check_lessik[index].text == "" and (check_lessik[index - 1].text == "" or
                                                       check_lessik[index - 1].text == "Нет информации"):
                    index += 1
                    num += 1
                elif check_lessik[index].text == "Суббота":
                    break
                else:
                    index += 1
        else:
            j += 1
    # print(position)
    # print(num)
    friday_date = oc.ras_less(num, position, week, lesson)
    return friday_date

def saturday(week):
    position = 1
    j = 0
    for i in check_lessik:
        if check_lessik[j].text == "" and (check_lessik[j - 1].text == "" or
                                           check_lessik[j - 1].text == "Нет информации") or \
                        check_lessik[j].text == "Вторник" or check_lessik[j].text == "Среда" or \
                check_lessik[j].text == "Четверг" or check_lessik[j].text == "Пятница":
            position += 1

        if check_lessik[j].text == "Суббота":
            num = 1
            index = j
            for i in check_lessik:
                # print(check_lessik[index].text)
                if check_lessik[index].text == "" and (check_lessik[index - 1].text == "" or
                                                       check_lessik[index - 1].text == "Нет информации"):
                    index += 1
                    num += 1
                elif check_lessik[index].text == "21:55-23:00":
                    break
                else:
                    index += 1
        else:
            j += 1
    # print(position)
    # print(num)
    return oc.ras_less(num, position, week, lesson)
