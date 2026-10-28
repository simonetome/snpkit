from .api_clients.exphewas_client import ExPhewasClient
from .exception_utils import get_exception

class PheWASResolver:
    def __init__(self, backend="auto"):
        self._api = ExPhewasClient(rate_limit_delay=0.5)
        self._backend = backend

    @get_exception
    def get_assoc_by_gene(
            self, 
            genes: str | list, 
        ):
        if self._backend == "local":
            return None
        else:
            return self._api.get_assoc_by_gene(genes)


def get_assoc_by_gene(genes, backend="auto"):
    """Public one-liner most users will actually call."""
    return PheWASResolver(
        backend=backend
    ).get_assoc_by_gene(
        genes=genes,
    )
