from .base import BaseEvent, DoubleBoundaryEvent


class CompensationEventSubProcess(BaseEvent):
    """
    Compensation : Start : Event Subprocess
    """

    pass


class CompensationBoundary(DoubleBoundaryEvent):
    """
    Compensation : Intermediate : Boundary
    """

    pass


class CompensationThrow(DoubleBoundaryEvent):
    """
    Compensation : Intermediate : Throw
    """

    pass


class CompensationEnd(BaseEvent):
    """
    Compensation : End
    """

    pass