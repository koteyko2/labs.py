def zad5_1():
    numbers = [randint(1, 100) for i in range(5)]
    if int(input('Введите число: ')) in numbers:
        print('Поздравляю, Вы угадали число!', numbers, sep='\n')
    else:
        print('Нет такого числа!', numbers, sep='\n')


def zad5_2():
    numbers = [randint(1, 50) for i in range(15)]
    duplicates = [x for i, x in enumerate(numbers) if i != numbers.index(x)]
    print(f'Исходный список: {numbers}')
    print(f'Повторяющиеся элементы: {duplicates}')


def zad5_3():
    week = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')
    holidays = int(input('Кол-во выходных: '))
    print('Выходные: ', week[-holidays:])
    print('Рабочие: ', week[:7 - holidays])


def zad5_4():
    group_1 = ['Петров', 'Иванов', 'Сидоров', 'Исаев', 'Капустин']
    group_2 = ['Соболев', 'Никитин', 'Карпов', 'Калинин', 'Ченцов']
    sport_group = []
    counter = 0
    for i in range(3):
        sport_group.append(group_1[randint(0, 4)])
    for i in range(2):
        sport_group.append(group_2[randint(0, 4)])
    for i in range(5):
        if 'Иванов' in sport_group[i]:
            counter += 1

    print(group_1, group_2, tuple(sorted(sport_group)), len(str(sport_group)), counter, sep='\n')