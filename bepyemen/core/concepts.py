from __future__ import annotations

from .base import Shape


class Diagram:
    def __init__(self, width: int, height: int):
        self._width = width
        self._height = height
        self._shapes = []

    def __repr__(self):
        return f"Diagram({self._width}x{self._height}, {len(self._shapes)})"

    def draw(self):
        shapes = "\n   ".join(str(s) for s in self._shapes)
        return (
            f"""<svg height="{self._height}" width="{self._width}" """
            f"""xmlns="http://www.w3.org/2000/svg">\n   {shapes}\n</svg>"""
        )

    def add_symbol(self, symbol: Shape):
        self._shapes.append(symbol)
        # return unique ID for symbol for linking?


class Colour:
    def __init__(self, named_colour: str):
        if named_colour:
            self._named_colour = named_colour
        else:
            self._named_colour = "white"

    def __str__(self):
        return self._named_colour


POSITION_POSITIVE_ONLY_MSG = "Position co-ordinates must be positive"


class Position:
    def __init__(self, x: int, y: int):
        if x < 0 or y < 0:
            raise ValueError(POSITION_POSITIVE_ONLY_MSG)
        self._x = x
        self._y = y

    def __str__(self):
        return f"({self._x}, {self._y})"

    def __repr__(self):
        return f"Position({self._x}, {self._y})"

    def __add__(self, other: Position) -> Position:
        """
        Position(x, y) + Position(m, n) = Position(x + m, y + n)
        """
        if (new_x := self._x + other.x) < 0 or (new_y := self._y + other.y) < 0:
            raise ValueError(POSITION_POSITIVE_ONLY_MSG)
        return Position(new_x, new_y)

    def __sub__(self, other: Position) -> Position:
        """
        Position(x, y) - Position(m, n) = Position(x - m, y - n)
        """
        if (new_x := self._x - other.x) < 0 or (new_y := self._y - other.y) < 0:
            raise ValueError(POSITION_POSITIVE_ONLY_MSG)
        return Position(new_x, new_y)

    def __mul__(self, multiplier: int) -> Position:
        """
        Position(x, y) => Position(x * mutlipler, y * multiplier)
        """
        if multiplier < 0:
            raise ValueError("Multiplier must be >= 0")
        return Position(self._x * multiplier, self._y * multiplier)

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y