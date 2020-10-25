from bepyemen.core.concepts import Position, Colour
from bepyemen.core.shapes import Rectangle

PARTICIPANT_FILL_COLOUR = Colour("white")
POOL_START_POS = Position(0, 0)
PARTICIPANT_NAME_WIDTH = 20
LANE_HEIGHT = 100
LANE_WIDTH = 600


class BaseParticipant(Rectangle):
    def __init__(self, pos, width, height, /, text: str):
        super().__init__(pos, width, height, fill=PARTICIPANT_FILL_COLOUR)
        self._text = text
        self._participants = []

    def __str__(self):
        return (
            super().__str__()
            + "\n"
            + str(self._name_box)
            + self._text
            + "/n".join([str(part) for part in self._participants])
        )


class Pool(BaseParticipant):
    def __init__(self, text="", /, level=0):
        offset = Position(PARTICIPANT_NAME_WIDTH, LANE_HEIGHT) * level
        width = LANE_WIDTH - (PARTICIPANT_NAME_WIDTH * level)
        super().__init__(POOL_START_POS + offset, width, LANE_HEIGHT, text)
        self._name_box = Rectangle(
            self._pos, PARTICIPANT_NAME_WIDTH, self._height, fill=PARTICIPANT_FILL_COLOUR
        )
        self._level = level

    def add_pool(self, text="", /):
        """
        Add a nested pool
        """
        self._height += LANE_HEIGHT
        self._name_box._height += LANE_HEIGHT
        nested_pool = Pool(text, level=self._level + 1)
        self._participants.append(nested_pool)

    def add_lane(self):
        """
        Add a swimlane to the current pool
        """
        pass


class Lane(BaseParticipant):
    pass
