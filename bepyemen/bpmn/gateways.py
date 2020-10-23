from bepyemen.core.shapes import Diamond


class BaseGateway(Diamond):
    pass


class ExclusiveGateway(BaseGateway):
    pass


class ParallelGateway(BaseGateway):
    pass


class InclusiveGateway(BaseGateway):
    pass


class EventGateway(BaseGateway):
    pass