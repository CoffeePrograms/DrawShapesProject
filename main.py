import random

from PIL import Image, ImageDraw

from Data.Shapes import Circle, Ellipse, Rectangle, Point


def check_int(value) -> int | bool:
    try:
        value = int(value)
    except ValueError:
        print('Введите число!')
        return False
    return value


def input_int() -> int:
    option = ""
    is_processed = False
    while is_processed is False:
        option = input(">> ")
        option = check_int(option)
        if option is not False:
            is_processed = True
    return option


def random_color() -> str:
    r = random.randint(1, 5)
    match r:
        case 1:
            return '#B5FBDD'
        case 2:
            return '#FBE7B5'
        case 3:
            return '#F85C50'
        case 4:
            return '#FE634E'
        case 5:
            return '#BDCCFF'


def main():
    im = Image.new('RGB', (1366, 768), '#FFDFDC')
    draw = ImageDraw.Draw(im)

    print("Введите кол-во фигур")
    n = input_int()

    shapes = []

    random.seed()
    for i in range(n):
        r = random.randint(1, 3)
        match r:
            case 1:
                item = Circle(random_color(),
                              Point(random.randint(1, 700), random.randint(1, 1300)),
                              random.randint(50, 500))
            case 2:
                item = Ellipse(random_color(),
                               Point(random.randint(1, 700), random.randint(1, 1300)),
                               random.randint(50, 500), random.randint(50, 500))
            case _:
                item = Rectangle(random_color(),
                                 Point(random.randint(1, 700), random.randint(1, 1300)),
                                 random.randint(50, 500))
        shapes.append(item)

    for item in shapes:
        item.draw(draw)

    im.show()
    # im.save('drawed-shapes.jpg', quality=95)


main()
