def zad6_1():
    countries_dict = {"Австрия": "Вена", "Бельгия": "Брюссель", "Великобритания": "Лондон", "Германия": "Берлин",
                      "Ирландия": "Дублин", "Лихтенштейн": "Вадуц", "Нидерладны": "Амстердам","Франция": "Париж",
                      "Белоруссия": "Минск", "Болгария": "София", "Польша": "Варшава", "Чехия": "Прага", "Албания": "Тирана",
                      "Босния и Герцеговина": "Сараево", "Северная Македония": "Скопье", "Сербия": "Белград"}

    print(countries_dict)
    print(countries_dict[input('Введите страну с большой буквы: ')])
    for key in sorted(countries_dict):
        print(key," - ", countries_dict[key])


def zad6_2():
    alph = {"а": 1, "б": 3, "в": 1, "г": 3, "д": 2, "е": 1, "ё": 3, "ж": 5, "з": 5, "и": 1, "й": 4, "к": 2, "л": 2,
            "м": 2, "н": 1, "о": 1, "п": 2, "р": 1, "с": 1, "т": 1, "у": 2, "ф": 10, "х": 5, "ц": 5, "ч": 5, "ш": 8,
            "щ": 10, "ъ": 10, "ы": 4, "ь": 3, "э": 8, "ю": 8, "я": 3}

    w = input('Слово:')
    s = 0
    for i in w:
        s += alph[(i.lower())]
    print('Сумма:', s)


def zad6_3():
    students = {'John': ['English', 'French', 'Spanish'],
                'Kate': ['German', 'Russian'],
                'Mike': ['Chinese', 'Japanese', 'Korean'],
                'Sarah': ['English', 'Italian', 'Portuguese'],
                'Tom': ['Chinese']}
    all_languages = set()
    for student, languages in students.items():
        all_languages.update(languages)
    sorted_languages = sorted(all_languages)
    print("Все языки: ")
    print(sorted_languages)
    chinese_speakers = []
    for student, languages in students.items():
        if 'Chinese' in languages:
            chinese_speakers.append(student)
    print("Носители китайского языка: ")
    print(chinese_speakers)