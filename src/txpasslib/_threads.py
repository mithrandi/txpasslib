from twisted.internet.defer import Deferred
from twisted.python.failure import Failure


def defer_to_worker(deliver, worker, work, *args, **kwargs):
    """
    Run a task in a worker, delivering the result as a ``Deferred`` in the
    reactor thread.
    """
    deferred = Deferred()

    def wrapped_work():
        try:
            result = work(*args, **kwargs)
        except BaseException:
            f = Failure()
            deliver(deferred.errback, f)
        else:
            deliver(deferred.callback, result)
    worker.do(wrapped_work)
    return deferred


__all__ = ['defer_to_worker']
