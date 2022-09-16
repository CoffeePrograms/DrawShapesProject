import abc

from PIL import ImageDraw


class Point:
    x: float
    y: float

    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y


class Shape:
    """Фигура"""
    __metaclass__ = abc.ABCMeta

    # цвет
    _outline = (255, 255, 255)
    _color: str
    # левый верхний угол
    _point: Point

    def __init__(self, color: str, point: Point):
        self._color = color
        self._point = point

    @abc.abstractmethod
    def draw(self, image_draw: ImageDraw):
        """Отрисовка"""
        return


class Circle(Shape):
    """Круг"""
    # диаметр
    _d: float

    def __init__(self, color, point, d):
        Shape.__init__(self, color, point)
        self._d = d

    def draw(self, image_draw: ImageDraw):
        image_draw.ellipse((self._point.y, self._point.x, self._point.y + self._d, self._point.x + self._d),
                           fill=self._color,
                           outline=self._outline)


class Ellipse(Circle):
    """Эллипс"""
    # полуось 1 - d (диметр по горизонтали)
    # полуось 2 - d_v (диметр по вертикали)
    __d_v: float

    def __init__(self, color, point, d_h, d_v):
        Circle.__init__(self, color, point, d=d_h)
        self.__d_v = d_v

    def draw(self, image_draw: ImageDraw):
        image_draw.ellipse((self._point.y, self._point.x, self._point.y + self._d, self._point.x + self.__d_v),
                           fill=self._color,
                           outline=self._outline)


class Rectangle(Shape):
    """Квадрат"""
    # сторона
    _a: float

    def __init__(self, color, point, a):
        Shape.__init__(self, color, point)
        self._a = a

    def draw(self, image_draw: ImageDraw):
        image_draw.rectangle((self._point.y, self._point.x, self._point.y + self._a, self._point.x + self._a),
                             fill=self._color,
                             outline=self._outline)
