from operator import attrgetter

from testtools.matchers import AfterPreprocessing, Equals, MatchesAll
from testtools.twistedsupport import failed


def failed_with(matcher):
    """
    Match against the exception of a failure.
    """
    return failed(AfterPreprocessing(attrgetter('value'), matcher))


def performed(perform, matcher):
    """
    Match against a result after performing a single action in a memory worker.
    """
    return MatchesAll(
        AfterPreprocessing(lambda _: perform(), Equals(True)),
        matcher)


__all__ = ['failed_with', 'performed']
