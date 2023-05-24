x = input('Введите слово с большой буквы: ')
with open('synonyms.txt') as f:
    lines = [i.rstrip('\n') for i in f]
    n = [i.split(' - ') for i in lines]
    n = sum(n, [])
    myn = {n[i]: n[i + 1] for i in range(0, len(n)-1, 2)}
    if x in n:
        print(myn[x])
        q = input('Вас устраивает подбор синонима?(на / нет): ')
        if q == 'нет':
            s = input('Введите новое слово: ')
            f = open('synonyms.txt', 'a+')
            f.write(s)
        else:
            print('Спасибо!')
    else:
        print('Такого слова нет!')
