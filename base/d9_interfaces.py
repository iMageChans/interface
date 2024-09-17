import threading

from substrateinterface import SubstrateInterface
from threading import Lock

from base.config import PYTHON_MAIN_NET_URL


class D9Interface(SubstrateInterface):
    _instance = None
    _lock = Lock()

    def __new__(cls, *args, **kwargs):
        with cls._lock:
            if cls._instance is None:
                cls._instance = super(D9Interface, cls).__new__(cls)
                super(D9Interface, cls._instance).__init__(*args, **kwargs)
            return cls._instance


substrate_local = threading.local()

def get_thread_substrate():
    if not hasattr(substrate_local, 'substrate'):
        substrate_local.substrate = SubstrateInterface(
            url=PYTHON_MAIN_NET_URL,
            ss58_format=9,
            type_registry_preset='polkadot',
        )
        substrate_local.substrate.init_runtime()
    return substrate_local.substrate
