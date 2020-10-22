from .base import Shape
from .concepts import Colour, Position


class Line(Shape):
    def __init__(self, start: Position, end: Position, colour: Colour, dashed: bool = False):
        self._start = start
        self._end = end
        self._colour = colour
        self._dashed = dashed

    def __str__(self):
        stroke_dasharray = 'stroke-dasharray="4 4" ' if self._dashed else ""
        return f"""
            <line x1="{self._start.x}" y1="{self._start.y}" 
                x2="{self._end.x}" y2="{self._end.y}" 
                stroke="{self._colour}" stroke-width="2" {stroke_dasharray}/>
        """


class Circle(Shape):
    def __init__(self, centre: Position, radius: int, fill: Colour):
        self._centre = centre
        self._radius = radius
        self._fill = fill

    def __str__(self):
        return f"""
            <circle cx="{self._centre.x}" cy="{self._centre.y}" 
                r="{self._radius}" 
                stroke="black" stroke-width="3" 
                fill="{self._fill}" />
        """

    def __repr__(self):
        return f"{self.__class__}({self._centre}, {self._radius})"


class Rectangle(Shape):
    def __init__(self, pos: Position, width: int, height: int, fill: Colour):
        self._pos = pos
        self._width = width
        self._height = height
        self._fill = fill

    def __str__(self):
        return f"""
            <rect x="{self._pos.x}" y="{self._pos.y}" 
                width="{self._width}" height="{self._height}" 
                fill="{self._fill}" 
                stroke-width="4" stroke="pink" />
        """

    def __repr__(self):
        return f"{self.__class__}({self._top_left}, {self._width}x{self._height})"