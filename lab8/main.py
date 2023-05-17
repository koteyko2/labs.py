from PIL import Image, ImageOps, ImageFilter, ImageDraw, ImageFont


def zad8_1():
    filename = "otrk.jpg"
    with Image.open(filename) as img:
        img.load()
    cropped_img = img.crop((200, 250, 800, 470))
    img.show()
    cropped_img.show()
    cropped_img.save("cropped_otrk.jpg")


def zad8_2():
    d = {1: "otrk.jpg", 2: "paskha.jpg", 3: "maslenitsa.jpg", 4: "newyear.jpg"}
    print('''1 - Хорошее настроение
2 - Пасха
3 - Масленница
4 - Новый год
''')
    ans = int(input("Какую открытку вы хотите получить: "))
    filename = d[ans]
    with Image.open(filename) as img:
        img.load()

    img.show()


def zad8_3():
    name = input("Имя: ")
    filename = "otrk.jpg"
    with Image.open(filename) as img:
        img.load()
    font = ImageFont.truetype("shrift.ttf", 50)
    draw_text = ImageDraw.Draw(img)
    draw_text.text(
        (img.width // 2 - 300, 15),
        "Поздравляю, " + name,
        font=font,
        fill=('#FF2400')
    )
    img.show()
    img.save(f'otrk {name}.jpg')


zad8_2()