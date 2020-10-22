from .base import Shape


class Diagram:
    def __init__(self, height: int, width: int):
        self._height = height
        self._width = width
        self.shapes = []

    def draw(self):
        shapes = "\n".join(str(s) for s in self.shapes)
        return f"""
            <svg height="{self._height}" 
                 width="{self._width}" 
                 xmlns="http://www.w3.org/2000/svg">'
                {shapes}
            </svg>
        """

    def add_symbol(self, symbol: Shape):
        self.shapes.append(symbol)
        # return unique ID for symbol for linking?


class Colour:
    def __init__(self, named_colour: str):
        if named_colour:
            self._named_colour = named_colour
        else:
            self._named_colour = "white"

    def __str__(self):
        return self._named_colour


class Position:
    def __init__(self, x: int, y: int):
        self._x = x
        self._y = y

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y