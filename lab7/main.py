from PIL import Image, ImageOps, ImageFilter, ImageDraw, ImageFont


def zad7_1():
    image = Image.open('5.jpg')
    image.show()
    print(image.size)
    print(image.mode)
    print(image.format)


def zad7_2():
        z = '5.jpg'
        image = Image.open(z)
        x, y = image.size
        x //= 3
        y //= 3
        print(image.size)
        out = image.resize((x, y))
        out.show()
        print(out.size)
        c = image.transpose(Image.FLIP_TOP_BOTTOM)
        c.show()
        g = ImageOps.mirror(image)
        g.show()
        out.save("11.jpg")
        c.save("22.jpg")
        g.save("33.jpg")


def zad7_3():
    a = "1.jpg"
    b = "2.jpg"
    c = "3.jpg"
    d = "4.jpg"
    f = "5.jpg"
    h = [a, b, c, d, f]
    for file in h:
        with Image.open(file) as img:
            new_img = img.filter(ImageFilter.CONTOUR)
            new_img.show()
            new_img.save("new" + file)


def zad7_4():
    s = "3.jpg"
    v = "2.jpg"
    image1 = Image.open(s)
    image2 = Image.open(v)
    image1.paste(image2)
    image1.show()
