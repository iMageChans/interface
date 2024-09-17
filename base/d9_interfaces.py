from substrateinterface import SubstrateInterface
from threading import Lock


class D9Interface(SubstrateInterface):
    _instance = None
    _lock = Lock()

    def __new__(cls, *args, **kwargs):
        with cls._lock:
            if cls._instance is None:
                cls._instance = super(D9Interface, cls).__new__(cls)
                super(D9Interface, cls._instance).__init__(*args, **kwargs)
            return cls._instance
