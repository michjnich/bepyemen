from .base import BaseEvent, DashedEvent, DoubleBoundaryEvent, DoubleDashedBoundaryEvent


class MultipleParallelNormal(BaseEvent):
    """
    MultipleParallel : Start : Normal
    """

    pass


class MultipleParallelEventSubProcess(MultipleParallelNormal):
    """
    MultipleParallel : Start : Event Subprocess
    Comment : Symbol is a duplicate of MultipleParallelNormal and requires no changes
    """

    pass


class MultipleParallelEventSubProcessNonInterrupt(DashedEvent):
    """
    MultipleParallel : Start : Event Subprocess non-interrupt
    """

    pass


class MultipleParallelCatch(DoubleBoundaryEvent):
    """
    MultipleParallel : Intermediate : Catch
    """

    pass


class MultipleParallelBoundary(MultipleParallelCatch):
    """
    MultipleParallel : Intermediate : Boundary
    Comment : Symbol is a duplicate of MultipleParallelCatch and requires no changes
    """

    pass


class MultipleParallelBoundaryNonInterrupt(DoubleDashedBoundaryEvent):
    """
    MultipleParallel : Intermediate : Boundary non-interrupt
    """

    pass
