from .base import BaseEvent, DoubleBoundaryEvent


class ErrorEventSubProcess(BaseEvent):
    """
    Error : Start : Event Subprocess
    """

    pass


class ErrorBoundary(DoubleBoundaryEvent):
    """
    Error : Intermediate : Boundary
    """

    pass


class ErrorEnd(BaseEvent):
    """
    Error : End
    """

    pass