from hypothesis import strategies as s
from hypothesis import given
from passlib.context import CryptContext
from testtools import TestCase
from testtools.matchers import (
    AfterPreprocessing, Equals, IsInstance, MatchesAll)
from testtools.twistedsupport import succeeded
from twisted._threads import createMemoryWorker

from txpasslib.context import TxCryptContext
from txpasslib.test.doubles import SynchronousReactorThreads
from txpasslib.test.matchers import failed_with, performed


class ContextTests(TestCase):
    """
    Tests for `txpasslib.context.CryptContext`.
    """
    @given(password=s.text())
    def test_hash_and_verify(self, password):
        """
        Hashing a password fires with the hash; verifying the password against
        that hash succeeds, while verifying a different password fails.
        """
        reactor = SynchronousReactorThreads()
        worker, perform = createMemoryWorker()
        ctx = TxCryptContext(
            CryptContext(schemes=['plaintext']),
            reactor, worker)
        self.assertThat(
            ctx.hash(password),
            performed(
                perform,
                succeeded(
                    MatchesAll(
                        AfterPreprocessing(
                            lambda h: ctx.verify(password, h),
                            performed(perform, succeeded(Equals(True)))),
                        AfterPreprocessing(
                            lambda h: ctx.verify(password + u'junk', h),
                            performed(perform, succeeded(Equals(False))))))))

    def test_verify_nonsense(self):
        """
        Hashing a value of the wrong type fails with ``TypeError``.
        """
        reactor = SynchronousReactorThreads()
        worker, perform = createMemoryWorker()
        ctx = TxCryptContext(
            CryptContext(schemes=['plaintext']),
            reactor, worker)
        self.assertThat(
            ctx.hash(42),
            performed(perform, failed_with(IsInstance(TypeError))))


__all__ = ['ContextTests']
