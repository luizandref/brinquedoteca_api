from fastapi import APIRouter
from schemas.brinquedo import BrinquedoCreate

router = APIRouter(prefix="/brinquedo", tags=["Brinquedo"])


@router.post("")
def criar_brinquedo_route(data: BrinquedoCreate):
    if data is None:
        return 