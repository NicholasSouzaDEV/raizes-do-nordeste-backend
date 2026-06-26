from pydantic import BaseModel
from typing import Literal


class OrderCreate(BaseModel):
    usuario_id: int
    produto_id: int
    quantidade: int
    canalPedido: Literal[
        "APP",
        "TOTEM",
        "BALCAO",
        "PICKUP",
        "WEB"
    ]


class OrderResponse(BaseModel):
    id: int
    usuario_id: int
    produto_id: int
    quantidade: int
    total: float
    status: str
    canalPedido: str

    class Config:
        from_attributes = True