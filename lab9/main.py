from pathlib import Path
from PIL import Image, ImageOps, ImageFilter, ImageDraw, ImageFont
import os

a = '1.jpeg'
b = '2.jpg'
c = '3.jpeg'
d = '4.jpeg'
e = '5.jpg'


def zad9_1():
    z = [a, b, c, d, e]
    count = 0
    for file in z:
        count += 1
        img = Image.open(file)
        new_img = img.filter(ImageFilter.SMOOTH_MORE)
        new_img.show()
        try:
            os.mkdir("D:/Denisenko/papka")
        except:
            pass
        new_img.save(f"D:/Denisenko/papka/new_img{count}.jpg")


def zad_9_2():
    z = [a, b, c, d, e]
    count = 0
    for file in z:
        if Path(file).suffix == '.jpg' or Path(file).suffix == '.jpeg':
            count += 1
            img = Image.open(file)
            new_img = img.filter(ImageFilter.SMOOTH_MORE)
            new_img.show()
            try:
                os.mkdir("D:/Denisenko/papka")
            except:
                pass
                new_img.save(f"D:/Denisenko/papka/new_img{count}.jpg")
            else:
                print('Нет файлов типа .jpg или .png')

def zad_9_3():
    with open('D:/Denisenko/Продукты.csv') as file:
        reading = csv.reader(file)
        next(reading)
        products = {}
        summ = 0
        for elem in reading:
            product = elem[0]
            count = int(elem[1])
            price = int(elem[2])
            products[product] = (count, price)
            summ += count * price
        print('Нужно купить:')
        for product, products[product] in products.items():
            print(f'{product} - {count} шт. за {price} руб.')
        print(f'Итоговая сумма: {summ} руб.')

