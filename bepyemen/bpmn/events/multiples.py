from .base import BaseEvent, DashedEvent, DoubleBoundaryEvent, DoubleDashedBoundaryEvent


class MultipleNormal(BaseEvent):
    """
    Multiple : Start : Normal
    """

    pass


class MultipleEventSubProcess(MultipleNormal):
    """
    Multiple : Start : Event Subprocess
    Comment : Symbol is a duplicate of MultipleNormal and requires no changes
    """

    pass


class MultipleEventSubProcessNonInterrupt(DashedEvent):
    """
    Multiple : Start : Event Subprocess non-interrupt
    """

    pass


class MultipleCatch(DoubleBoundaryEvent):
    """
    Multiple : Intermediate : Catch
    """

    pass


class MultipleBoundary(MultipleCatch):
    """
    Multiple : Intermediate : Boundary
    Comment : Symbol is a duplicate of MultipleCatch and requires no changes
    """

    pass


class MultipleBoundaryNonInterrupt(DoubleDashedBoundaryEvent):
    """
    Multiple : Intermediate : Boundary non-interrupt
    """

    pass


class MultipleThrow(DoubleBoundaryEvent):
    """
    Multiple : Intermediate : Throw
    """

    pass


class MultipleEnd(BaseEvent):
    """
    Multiple : End
    """

    pass