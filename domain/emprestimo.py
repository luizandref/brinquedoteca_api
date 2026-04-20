from dataclasses import dataclass
from domain.enum import Status

@dataclass(frozen=True)
class Emprestimo:
    id: int
    crianca_id: int
    briquedo_id: int
    data_emprestimo: str
    data_devolucao: str = None
    Status: status = status.DISPONIVEL
    