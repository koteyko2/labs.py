def zad3_1():
    n = int(input('Кол-во слов : '))
    all_words = ''
    for i in range(n):
        word = input()
        all_words += word + ' '
    print(all_words)


def zad3_2():
    a = input()
    res = ''
    while a != 'stop':
        a = input()
        res = res + a + ''
    print(res)


def zad3_3():
    slovo = input()
    if 'ф' in slovo:
        print('Ого, Это редкое слово')
    else:
        print('Эх...Это не очень редкое слово')


def zad3_4():
    from random import randint
    m = 0
    r = 0
    while m < 3:
        a = randint(1, 100)
        b = randint(1, 100)
        res = int(input(str(a) + '+' + str(b) + '='))
        if res != a+b:
            print("Ответ не верный")
            m += 1
        else:
            print("Правильно")
            r += 1
    if m == 3:
        print("игра окончена правильных ответов", r)