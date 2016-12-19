from hypothesis import strategies as s
from hypothesis import given
from passlib.context import CryptContext
from testtools import TestCase
from testtools.matchers import Always, Equals, IsInstance
from testtools.twistedsupport import succeeded
from twisted._threads import createMemoryWorker

from txpasslib.context import TxCryptContext
from txpasslib.test.doubles import SynchronousReactorThreads
from txpasslib.test.matchers import failed_with


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
        d = ctx.hash(password)
        perform()
        self.assertThat(d, succeeded(Always()))
        password_hash = d.result

        d = ctx.verify(password, password_hash)
        perform()
        self.assertThat(d, succeeded(Equals(True)))

        d = ctx.verify(password + u'junk', password_hash)
        perform()
        self.assertThat(d, succeeded(Equals(False)))

    def test_verify_nonsense(self):
        """
        Hashing a value of the wrong type fails with ``TypeError``.
        """
        reactor = SynchronousReactorThreads()
        worker, perform = createMemoryWorker()
        ctx = TxCryptContext(
            CryptContext(schemes=['plaintext']),
            reactor, worker)
        d = ctx.hash(42)
        perform()
        self.assertThat(d, failed_with(IsInstance(TypeError)))


__all__ = ['ContextTests']
