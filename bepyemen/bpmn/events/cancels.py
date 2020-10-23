from .base import BaseEvent, DoubleBoundaryEvent


class CancelBoundary(DoubleBoundaryEvent):
    """
    Cancel : Intermediate : Boundary
    """

    pass


class CancelEnd(BaseEvent):
    """
    Cancel : End
    """

    pass