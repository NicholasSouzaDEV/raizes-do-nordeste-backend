from pydantic import BaseModel


class ProductCreate(BaseModel):
    nome: str
    descricao: str
    preco: float


class ProductResponse(BaseModel):
    id: int
    nome: str
    descricao: str
    preco: float

    class Config:
        from_attributes = True