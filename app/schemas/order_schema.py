from pydantic import BaseModel


class OrderCreate(BaseModel):
    usuario_id: int
    produto_id: int
    quantidade: int


class OrderResponse(BaseModel):
    id: int
    usuario_id: int
    produto_id: int
    quantidade: int
    total: float
    status: str

    class Config:
        from_attributes = True