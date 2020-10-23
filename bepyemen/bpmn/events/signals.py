from .base import BaseEvent, DashedEvent, DoubleBoundaryEvent, DoubleDashedBoundaryEvent


class SignalNormal(BaseEvent):
    """
    Signal : Start : Normal
    """

    pass


class SignalEventSubProcess(SignalNormal):
    """
    Signal : Start : Event Subprocess
    Comment : Symbol is a duplicate of SignalNormal and requires no changes
    """

    pass


class SignalEventSubProcessNonInterrupt(DashedEvent):
    """
    Signal : Start : Event Subprocess non-interrupt
    """

    pass


class SignalCatch(DoubleBoundaryEvent):
    """
    Signal : Intermediate : Catch
    """

    pass


class SignalBoundary(SignalCatch):
    """
    Signal : Intermediate : Boundary
    Comment : Symbol is a duplicate of SignalCatch and requires no changes
    """

    pass


class SignalBoundaryNonInterrupt(DoubleDashedBoundaryEvent):
    """
    Signal : Intermediate : Boundary non-interrupt
    """

    pass


class SignalThrow(DoubleBoundaryEvent):
    """
    Signal : Intermediate : Throw
    """

    pass


class SignalEnd(BaseEvent):
    """
    Signal : End
    """

    pass