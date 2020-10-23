from .base import BaseEvent, DashedEvent, DoubleBoundaryEvent, DoubleDashedBoundaryEvent


class MessageEventSubProcess(BaseEvent):
    """
    Message : Start : Event Subprocess
    """

    pass


class MessageEventSubProcessNonInterrupt(DashedEvent):
    """
    Message : Start : Event Subprocess non-interrupt
    """

    pass


class MessageBoundary(DoubleBoundaryEvent):
    """
    Message : Intermediate : Boundary
    """

    pass


class MessageBoundaryNonInterrupt(DoubleDashedBoundaryEvent):
    """
    Message : Intermediate : Boundary non-interrupt
    """

    pass


class MessageThrow(DoubleBoundaryEvent):
    """
    Message : Intermediate : Throw
    """

    pass


class MessageEnd(BaseEvent):
    """
    Message : End
    """

    pass