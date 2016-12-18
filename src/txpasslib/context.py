"""
Asynchronous wrappers for ``passlib.context``.
"""
import attr

from txpasslib._threads import defer_to_worker


@attr.s
class TxCryptContext(object):
    """
    An asynchronous wrapper for ``CryptContext`` from ``passlib``.

    Expensive operations are run in a thread pool to avoid blocking the main
    thread.
    """
    _context = attr.ib()
    _reactor = attr.ib()
    _worker = attr.ib()

    def _defer(self, f, *a, **kw):
        return defer_to_worker(
            self._reactor.callFromThread, self._worker,
            f, *a, **kw)

    def hash(self, secret, scheme=None, category=None, **kw):
        """
        Hash a secret.

        See ``passlib.context.CryptContext.hash``.
        """
        return self._defer(self._context.hash, secret, scheme, category, **kw)

    def verify(self, secret, hash, scheme=None, category=None, **kw):
        """
        Verify a secret against an existing hash.

        See ``passlib.context.CryptContext.verify``.
        """
        return self._defer(
            self._context.verify, secret, hash, scheme, category, **kw)


__all__ = ['TxCryptContext']
