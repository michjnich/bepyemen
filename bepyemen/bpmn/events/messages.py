from .base import BaseEvent, DashedEvent, DoubleBoundaryEvent, DoubleDashedBoundaryEvent


class MessageNormal(BaseEvent):
    """
    Message : Start : Normal
    """

    pass


class MessageEventSubProcess(MessageNormal):
    """
    Message : Start : Event Subprocess
    Comment : Symbol is a duplicate of MessageNormal and requires no changes
    """

    pass


class MessageEventSubProcessNonInterrupt(DashedEvent):
    """
    Message : Start : Event Subprocess non-interrupt
    """

    pass


class MessageCatch(DoubleBoundaryEvent):
    """
    Message : Intermediate : Catch
    """

    pass


class MessageBoundary(MessageCatch):
    """
    Message : Intermediate : Boundary
    Comment : Symbol is a duplicate of MessageCatch and requires no changes
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