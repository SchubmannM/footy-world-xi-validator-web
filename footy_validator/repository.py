from django.db import transaction


def _ensure_durable_atomic():
    # https://seddonym.me/2020/11/19/trouble-atomic/
    if not transaction.get_autocommit():
        raise RuntimeError("Function should not be called within an atomic block.")


def ensure_durable_atomic():
    _ensure_durable_atomic()


class BaseDjangoRepository:
    atomic = None

    def __enter__(self):
        ensure_durable_atomic()
        self.atomic = transaction.atomic()
        self.atomic.__enter__()
        return self

    def __exit__(self, *args):
        """
        We want to automatically rollback the transaction if it was not committed.
        That is why we are doing a rollback here.
        """
        self.rollback()

    def commit(self):
        if self.atomic:
            try:
                self.atomic.__exit__(None, None, None)
            finally:
                self.atomic = None

    def rollback(self):
        if self.atomic:
            transaction.set_rollback(True)
            try:
                self.atomic.__exit__(None, None, None)
            finally:
                self.atomic = None
