from fastapi import APIRouter
from schemas.crianca import CriancaCreate

router = APIRouter(prefix="/crianca", tags=["Crianca"])


@router.post("")
def criar_crianca_route(data: CriancaCreate):
    if data is None:
        return 