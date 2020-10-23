from .base import BaseEvent, DashedEvent, DoubleBoundaryEvent, DoubleDashedBoundaryEvent


class TimerNormal(BaseEvent):
    """
    Timer : Start : Normal
    """

    pass


class TimerEventSubProcess(TimerNormal):
    """
    Timer : Start : Event Subprocess
    Comment : Symbol is a duplicate of TimerNormal and requires no changes
    """

    pass


class TimerEventSubProcessNonInterrupt(DashedEvent):
    """
    Timer : Start : Event Subprocess non-interrupt
    """

    pass


class TimerCatch(DoubleBoundaryEvent):
    """
    Timer : Intermediate : Catch
    """

    pass


class TimerBoundary(TimerCatch):
    """
    Timer : Intermediate : Boundary
    Comment : Symbol is a duplicate of TimerCatch and requires no changes
    """

    pass


class TimerBoundaryNonInterrupt(DoubleDashedBoundaryEvent):
    """
    Timer : Intermediate : Boundary non-interrupt
    """

    pass
