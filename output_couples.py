#Метод для отображения пар в консоль
def ras_less(num, index, week, lesson): #метод для вывода собственно расписания
    mass = []
    num_less = 0  # эта
    last_time = 0  # и эта переменная введена для адекватного отображения списка

    for k in range(num):
        check_less = lesson[index].find_all('td')
        # print(last_time, check_less[1].text)

        if check_less[2].text == "Нет информации": #те случаи когда td имеет содержание "Нет информации"
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
                        f"Пара №{num_less} - {check_less[1].text} #{check_less[4].text}# {check_less[3].text} - "
                        f"{check_less[5].text} - {check_less[6].text}")

                    a = (num_less, check_less[1].text, check_less[4].text, check_less[3].text,
                                check_less[5].text,check_less[6].text)
                    mass.append(a)
                    last_time = check_less[1].text
                # else:
                # Когда по уроку не "нет информации", а не совпадают по датам
                # print(f"Пара №{num_less} - {check_less[1].text} - Bebra")
                last_time = check_less[1].text
                # num_less += 1
            else:
                if str(week) in check_less[2].text:
                    print(
                        f"Пара №{num_less} - {check_less[1].text} #{check_less[4].text}# {check_less[3].text} -"
                        f" {check_less[5].text} - {check_less[6].text}")

                    a = (num_less, check_less[1].text, check_less[4].text, check_less[3].text,
                         check_less[5].text, check_less[6].text)
                    mass.append(a)
                    # return num_less, check_less[1].text, check_less[4].text, check_less[3].text, check_less[5].text, \
                    #        check_less[6].text
                else:
                    pass
                last_time = check_less[1].text
        index += 1

    # print(mass)
    return mass