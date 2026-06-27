from pydantic import BaseModel
from enum import Enum


class CanalPedido(str, Enum):
    APP = "APP"
    TOTEM = "TOTEM"
    BALCAO = "BALCAO"
    PICKUP = "PICKUP"
    WEB = "WEB"


class OrderCreate(BaseModel):
    usuario_id: int
    produto_id: int
    quantidade: int
    canalPedido: CanalPedido


class OrderResponse(BaseModel):
    id: int
    usuario_id: int
    produto_id: int
    quantidade: int
    total: float
    status: str
    canalPedido: CanalPedido

    class Config:
        from_attributes = True