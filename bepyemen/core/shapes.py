from .base import Shape
from .concepts import Colour, Position

STROKE_DASHARRAY = 'stroke-dasharray="4 4" '
STROKE_WIDTH_NORMAL = 1
STROKE_WIDTH_THICK = 4


class Line(Shape):
    def __init__(self, start: Position, end: Position, colour: Colour, dashed: bool = False):
        self._start = start
        self._end = end
        self._colour = colour
        self._dashed = dashed

    def __str__(self):
        stroke_dasharray = STROKE_DASHARRAY if self._dashed else ""
        return (
            f"""<line x1="{self._start.x}" y1="{self._start.y}" """
            f"""x2="{self._end.x}" y2="{self._end.y}" """
            f"""stroke="{self._colour}" stroke-width="{STROKE_WIDTH_NORMAL}" {stroke_dasharray}/> """
        )


class Circle(Shape):
    def __init__(
        self,
        centre: Position,
        radius: int,
        /,
        fill: Colour,
        dashed: bool = False,
        thick: bool = False,
    ):
        self._centre = centre
        self._radius = radius
        self._fill = fill
        self._dashed = dashed
        self._thick = thick

    def __str__(self):
        stroke_dasharray = STROKE_DASHARRAY if self._dashed else ""
        stroke_width = STROKE_WIDTH_THICK if self._thick else STROKE_WIDTH_NORMAL
        return (
            f"""<circle cx="{self._centre.x}" cy="{self._centre.y}" """
            f"""r="{self._radius}" """
            f"""stroke="black" stroke-width="{stroke_width}" {stroke_dasharray}"""
            f"""fill="{self._fill}" />"""
        )

    def __repr__(self):
        return f"{self.__class__.__name__}({self._centre}, {self._radius})"


class Rectangle(Shape):
    def __init__(self, pos: Position, width: int, height: int, fill: Colour):
        self._pos = pos
        self._width = width
        self._height = height
        self._fill = fill

    def __str__(self):
        return (
            f"""<rect x="{self._pos.x}" y="{self._pos.y}" """
            f"""width="{self._width}" height="{self._height}" """
            f"""fill="{self._fill}" """
            f"""stroke-width="{STROKE_WIDTH_NORMAL}" stroke="pink" />"""
        )

    def __repr__(self):
        return f"{self.__class__.__name__}({self._top_left}, {self._width}x{self._height})"


class Diamond(Shape):
    def __init__(self, pos: Position, width: int, height: int, fill: Colour):
        self._pos = pos
        self._width = width
        self._height = height
        self._fill = fill

    def __str__(self):
        return (
            f"""<polygon points="{self._pos.x},{self._pos.y} """
            f"{self._pos.x + self._width // 2},{self._pos.y + self._height // 2} "
            f"{self._pos.x},{self._pos.y + self._height} "
            f"""{self._pos.x - self._width // 2},{self._pos.y + self._height // 2}" """
            f"""fill="{self._fill}" />"""
        )

    def __repr__(self):
        return f"{self.__class__.__name__}({self._pos}, {self._width}x{self._height})"
