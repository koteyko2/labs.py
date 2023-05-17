def zad2_1():
    lower = False
    numeric = False
    specs = False
    lenght = False

    password = input('Введите пароль : ')
    for dig in password:
        if dig.isnumeric():
            numeric = True
        if dig.islower():
            lower = True
        if len(password) >= 6:
            lenght = True
        if dig in '&*%$#№@':
            specs = True

    if numeric is True and lower is True and lenght is True and specs is True:
        print('Пароль принят!')
    else:
        print('Пароль не надёжен!')


def zad2_2():
    place = int(input('Номер вагона : '))
    if place > 52:
        print('Несуществующий вагон!')
    elif place % 2 == 0:
        print('Верхнее')
    elif place % 2 != 0:
        print('Нижнее')
    elif 37 <= place <= 52:
        print('Боковое')


def zad2_3():
    year = int(input('Год : '))
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        print(f'Год {year} - високосный')
    else:
        print('Этот год не високосный')


def zad2_4():
    color_1 = input('Первый цвет : ')
    color_2 = input('Второй цвет : ')
    if (color_1 == 'красный' and color_2 == 'синий') or (color_2 == 'красный' and color_1 == 'синий'):
        print('Фиолетовый')
    elif (color_1 == 'красный' and color_2 == 'желтый') or (color_2 == 'красный' and color_1 == 'желтый'):
        print('Оранжевый')
    elif (color_1 == 'желтый' and color_2 == 'синий') or (color_2 == 'желтый' and color_1 == 'синий'):
        print('Зеленый')
    else:
        print('Неверно введен цвет!')