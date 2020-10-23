from .base import BaseEvent, DashedEvent, DoubleBoundaryEvent, DoubleDashedBoundaryEvent


class ConditionalNormal(BaseEvent):
    """
    Conditional : Start : Normal
    """

    pass


class ConditionalEventSubProcess(ConditionalNormal):
    """
    Conditional : Start : Event Subprocess
    Comment : Symbol is a duplicate of ConditionalNormal and requires no changes
    """

    pass


class ConditionalEventSubProcessNonInterrupt(DashedEvent):
    """
    Conditional : Start : Event Subprocess non-interrupt
    """

    pass


class ConditionalCatch(DoubleBoundaryEvent):
    """
    Conditional : Intermediate : Catch
    """

    pass


class ConditionalBoundary(ConditionalCatch):
    """
    Conditional : Intermediate : Boundary
    Comment : Symbol is a duplicate of ConditionalCatch and requires no changes
    """

    pass


class ConditionalBoundaryNonInterrupt(DoubleDashedBoundaryEvent):
    """
    Conditional : Intermediate : Boundary non-interrupt
    """

    pass
