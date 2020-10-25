from bepyemen.core.concepts import Colour
from bepyemen.core.shapes import Circle


EVENT_FILL_COLOUR = Colour("white")


class BaseEvent(Circle):
    def __init__(self, centre, radius, dashed=False, thick=False):
        super().__init__(centre, radius, EVENT_FILL_COLOUR, dashed, thick)


class DashedEvent(BaseEvent):
    def __init__(self, centre, radius):
        super().__init__(centre, radius, dashed=True)


class DoubleBoundaryEvent(BaseEvent):
    def __init__(self, centre, radius, dashed=False):
        super().__init__(centre, radius, dashed)
        self._inner_radius = radius - 2
        self._inner_boundary = Circle(
            self._centre,
            self._inner_radius,
            fill=EVENT_FILL_COLOUR,
            dashed=self._dashed,
        )

    def __str__(self):
        return super().__str__() + "\n" + str(self._inner_boundary)


class DoubleDashedBoundaryEvent(DoubleBoundaryEvent):
    def __init__(self, centre, radius):
        super().__init__(centre, radius, True)


class StartEvent(BaseEvent):
    pass


class EndEvent(BaseEvent):
    def __init__(self, centre, radius):
        super().__init__(centre, radius, thick=True)
