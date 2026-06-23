from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from app.database.database import (
    engine,
    Base,
    get_db
)

from app.models.user import User

from app.schemas.user_schema import (
    UserCreate,
    UserResponse,
    LoginRequest,
    TokenResponse
)

from app.crud.user_crud import (
    create_user,
    get_users,
    login_user
)

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Raízes do Nordeste API",
    version="1.0.0"
)


@app.get("/")
def home():
    return {
        "message": "API Raízes do Nordeste funcionando"
    }


@app.post(
    "/users",
    response_model=UserResponse
)
def create_new_user(
    user: UserCreate,
    db: Session = Depends(get_db)
):
    return create_user(
        db,
        user.nome,
        user.email,
        user.senha
    )


@app.get(
    "/users",
    response_model=list[UserResponse]
)
def list_users(
    db: Session = Depends(get_db)
):
    return get_users(db)

@app.post(
    "/login",
    response_model=TokenResponse
)
def login(
    user: LoginRequest,
    db: Session = Depends(get_db)
):

    result = login_user(
        db,
        user.email,
        user.senha
    )

    if not result:
        return {
            "access_token": "",
            "token_type": "invalid"
        }

    return result