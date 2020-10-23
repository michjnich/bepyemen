from bepyemen.core.shapes import Rectangle


class BaseActivity(Rectangle):
    pass


class Task(BaseActivity):
    pass


class SubProcess(BaseActivity):
    pass


class CallActivity(BaseActivity):
    pass


class EventSubProcess(BaseActivity):
    pass


class Transaction(BaseActivity):
    pass
