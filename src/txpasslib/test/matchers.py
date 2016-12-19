from operator import attrgetter

from testtools.matchers import AfterPreprocessing
from testtools.twistedsupport import failed


def failed_with(matcher):
    """
    Match against the exception of a failure.
    """
    return failed(AfterPreprocessing(attrgetter('value'), matcher))


__all__ = ['failed_with']
