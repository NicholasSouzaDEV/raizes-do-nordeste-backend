from sqlalchemy.orm import Session
from app.models.user import User

from app.services.security import (
    hash_password,
    verify_password,
    create_access_token
)


def create_user(
    db: Session,
    nome: str,
    email: str,
    senha: str,
    perfil: str
):

    user = User(
    nome=nome,
    email=email,
    senha=hash_password(senha),
    perfil=perfil
)

    db.add(user)
    db.commit()
    db.refresh(user)

    return user


def get_users(db: Session):
    return db.query(User).all()


def login_user(
    db: Session,
    email: str,
    senha: str
):

    user = (
        db.query(User)
        .filter(User.email == email)
        .first()
    )

    if not user:
        return None

    if not verify_password(
        senha,
        user.senha
    ):
        return None

    token = create_access_token(
    {
        "sub": user.email,
        "perfil": user.perfil
    }
)

    return {
        "access_token": token,
        "token_type": "bearer"
    }