def zad4_1():
    number = int(input('Введите число: '))
    try:
        if int(number) % 3 == 0:
            print("Делится")
        else:
            print("Не делится")
    except:
        print("Некорректный ввод")


def zad4_2():
    number = int(input('Введите число: '))
    try:
        answer = 100/int(number)
    except ValueError:
        print("Вы ввели не число")
    except ZeroDivisionError:
        print("На 0 делить нельзя")
    else:
        print(100 / int(number))


def zad4_3():
    date = input('Введите дату через точку (первый - месяц): ')
    try:
        if int(date.split(".")[0]) > 12 or int(date.split(".")[1]) > 12 or int(date.split(".")[1]) < 1 or int(date.split(".")[0]) < 1:
            print("Вы неправльно ввели дату или месяц")
        else:
            if int(date.split(".")[0]) * int(date.split(".")[1]) == int(date.split(".")[2][2:]):
                print('Дата - магическая')
            else:
                print('Дата - не магическая')
    except:
        print("Вы ввели дату неправильно")


def zad4_4():
    number = input('Введите номер билета: ')
    try:
        sum1 = 0
        sum2 = 0
        for i in number[:int(len(number) / 2)]:
            sum1 += int(i)
        for j in number[int(len(number) / 2):]:
            sum2 += int(j)
        if sum1 == sum2:
            print("Счастливый билет")
        else:
            print("Несчастливый билет")
    except:
        print("Некорректный ввод")