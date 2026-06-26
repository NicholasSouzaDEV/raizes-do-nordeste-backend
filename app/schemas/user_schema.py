from pydantic import BaseModel


class UserCreate(BaseModel):
    nome: str
    email: str
    senha: str
    perfil: str = "CLIENTE"


class UserResponse(BaseModel):
    id: int
    nome: str
    email: str
    perfil: str

    class Config:
        from_attributes = True


class LoginRequest(BaseModel):
    email: str
    senha: str


class TokenResponse(BaseModel):
    access_token: str
    token_type: str