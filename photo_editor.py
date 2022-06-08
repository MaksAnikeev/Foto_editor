from PIL import Image, ImageFilter, ImageDraw, ImageFont
from easygui import *


def convertation():
    picture = Image.open(k)
    name = k.partition('.')[0]
    name = name.split(r'\\'[:-1])
    name = name[-1]
    picture.save(name + '.png')


def cutting():
    picture = Image.open(k)
    list1 = ['x верхний левый', 'y верхний левый', 'x нижний правый', 'y нижний правый']
    list = []
    list = multenterbox('Введите параметры вырезаемого куска', 'вырезать кусок', fields=list1)
    x0 = int(list[0])
    y0 = int(list[1])
    x1 = int(list[2])
    y1 = int(list[3])
    new_picture = picture.crop((x0, y0, x1, y1))
    name = k.partition('.')[0]
    name = name.split(r'\\'[:-1])
    name = name[-1]
    new_picture.save(name + '_cut.png')
    msgbox('Результат', image=name + '_cut.png')


def resize():
    picture = Image.open(k)
    a, b = picture.size
    chose = ['Увеличить', 'Уменьшить']
    question = buttonbox('Вы хотите увеличить или уменьшить картинку', choices=chose)
    if question == 'Увеличить':
        x0 = enterbox('Введите во сколько раз вы хотите увеличить картинку')
        x0 = 1 / int(x0)
    else:
        x0 = enterbox('Введите во сколько раз вы хотите уменьшить картинку')
        x0 = int(x0)
    new_picture = picture.resize((int(a / x0), int(b / x0)))
    name = k.partition('.')[0]
    name = name.split(r'\\'[:-1])
    name = name[-1]
    new_picture.save(name + '_resize.png')
    msgbox('Результат', image=name + '_resize.png')


def blak():
    picture = Image.open(k)
    name1 = k.partition('.')[2]
    if name1 == 'jpg':
        w, h = picture.size
        for x in range(w):
            for y in range(h):
                r, g, b = picture.getpixel((x, y))
                num = r * 0.12 + g * 0.715 + b * 0.0746
                picture.putpixel((x, y), (int(num), int(num), int(num)))
        name = k.partition('.')[0]
        name = name.split(r'\\'[:-1])
        name = name[-1]
        picture.save(name + '_black.png')
        msgbox('Результат', image=name + '_black.png')
    else:
        msgbox('вы открыли файл с расширением отличающимся от jpg, выберете другой файл')


def filters():
    picture = Image.open(k)
    list = ['размытость', 'карандаш', 'выпуклые края']
    y = buttonbox('Выберите эффект', 'эффекты', choices=list)
    if y == 'размытость':
        new_picture = picture.filter(ImageFilter.BLUR)
        name = k.partition('.')[0]
        name = name.split(r'\\'[:-1])
        name = name[-1]
        new_picture.save(name + '_filter.png')
        msgbox('Результат', image=name + '_filter.png')
    elif y == 'карандаш':
        new_picture = picture.filter(ImageFilter.CONTOUR)
        name = k.partition('.')[0]
        name = name.split(r'\\'[:-1])
        name = name[-1]
        new_picture.save(name + '_filter.png')
        msgbox('Результат', image=name + '_filter.png')
    else:
        new_picture = picture.filter(ImageFilter.EDGE_ENHANCE)
        name = k.partition('.')[0]
        name = name.split(r'\\'[:-1])
        name = name[-1]
        new_picture.save(name + '_filter.png')
        msgbox('Результат', image=name + '_filter.png')


def printer():
    picture = Image.open(k)
    idraw = ImageDraw.Draw(picture)
    list = ['напиши надпись', 'Задай размер шрифта надписи', 'Задай х координату начала надписи',
            'Задай y координату начала надписи']
    list_1 = []
    list_1 = multenterbox('Введите информацию о надписи', 'Надпись', fields=list)
    text = list_1[0]
    z = int(list_1[1])
    font = ImageFont.truetype('arial', size=z)
    x = int(list_1[2])
    y = int(list_1[3])
    idraw.text((x, y), text, font=font)
    name = k.partition('.')[0]
    name = name.split(r'\\'[:-1])
    name = name[-1]
    picture.save(name + '_text.png')
    msgbox('Результат', image=name + '_text.png')

def avatar():
    picture = Image.open(k)
    rgb_picture = picture.convert("RGB")
    red_canel_picture, green_canel_picture, blue_canel_picture = rgb_picture.split()
    coordinates_left_red = (60, 0, red_canel_picture.width, red_canel_picture.height)
    left_red_picture = red_canel_picture.crop(coordinates_left_red)
    coordinates_middle_red = (30, 0, red_canel_picture.width - 30, red_canel_picture.height)
    middle_red_picture = red_canel_picture.crop(coordinates_middle_red)
    avatar_red = Image.blend(left_red_picture, middle_red_picture, 0.3)

    coordinates_left_blue = (0, 0, blue_canel_picture.width - 60, blue_canel_picture.height)
    blue_right = blue_canel_picture.crop(coordinates_left_blue)
    coordinates_middle_blue = (30, 0, blue_canel_picture.width - 30, blue_canel_picture.height)
    blue_middle = blue_canel_picture.crop(coordinates_middle_blue)
    avatar_blue = Image.blend(blue_right, blue_middle, 0.3)

    coordinates_middle_green = (30, 0, green_canel_picture.width - 30, green_canel_picture.height)
    avatar_green = green_canel_picture.crop(coordinates_middle_green)

    avatar = Image.merge("RGB", (avatar_red, avatar_green, avatar_blue))
    size = ['Ширина', 'Высота']
    fieldValues = []
    fieldValues = multenterbox(msg='Размеры аватарки', title='Данные', fields=size)
    avatar.thumbnail((int(fieldValues[0]), int(fieldValues[1])))
    name = k.partition('.')[0]
    name = name.split(r'\\'[:-1])
    name = name[-1]
    avatar.save(name +'_avatar.jpg')
    msgbox('Результат', image=name +'_avatar.jpg')


reading_help = open('подсказка.txt','r', encoding='utf-8')
help = []
for line in reading_help:
    help.append(line)

start = msgbox('Вы запустили фоторедактор, выберите файл для редактирования', 'фоторедактор')
k = fileopenbox()
while True:
    msgbox('Выберите что будем делать с изображением ')
    list_1 = ['Конвертация в png', 'Обрезка', 'Изменение размеров', 'Сделаем надпись',
              'Сделаем черно/белым (только для файла с расширением jpg)', 'Наложим фильтры', 'Сделаем аватарку', 'Подсказка']
    chose = choicebox('Выберите действие', 'действия', choices=list_1)
    if chose == 'Конвертация в png':
        convertation()
    elif chose == 'Обрезка':
        cutting()
    elif chose == 'Изменение размеров':
        resize()
    elif chose == 'Сделаем надпись':
        printer()
    elif chose == 'Сделаем черно/белым (только для файла с расширением jpg)':
        blak()
    elif chose == 'Наложим фильтры':
        filters()
    elif chose == 'Сделаем аватарку':
        avatar()
    elif chose == 'Подсказка':
        textbox('Пояснения по действиям', 'Подсказка', help)
    var = ['Стоп', 'Продолжить']
    stop = buttonbox('если хотите выйти напишите стоп', choices=var)
    if stop != 'Стоп':
        start = msgbox('Вы запустили фоторедактор, выберите файл для редактирования', 'фоторедактор')
        k = fileopenbox()
    else:
        break

