from sqlalchemy.orm import Session
from fastapi import HTTPException

from app.models.product import Product


def create_product(
    db: Session,
    nome: str,
    descricao: str,
    preco: float
):
    product = Product(
        nome=nome,
        descricao=descricao,
        preco=preco
    )

    db.add(product)
    db.commit()
    db.refresh(product)

    return product


def get_products(db: Session):
    return db.query(Product).all()


def get_product_by_id(
    db: Session,
    product_id: int
):
    product = (
        db.query(Product)
        .filter(Product.id == product_id)
        .first()
    )

    if not product:
        raise HTTPException(
            status_code=404,
            detail="Produto não encontrado"
        )

    return product


def update_product(
    db: Session,
    product_id: int,
    nome: str,
    descricao: str,
    preco: float
):
    product = (
        db.query(Product)
        .filter(Product.id == product_id)
        .first()
    )

    if not product:
        raise HTTPException(
            status_code=404,
            detail="Produto não encontrado"
        )

    product.nome = nome
    product.descricao = descricao
    product.preco = preco

    db.commit()
    db.refresh(product)

    return product


def delete_product(
    db: Session,
    product_id: int
):
    product = (
        db.query(Product)
        .filter(Product.id == product_id)
        .first()
    )

    if not product:
        raise HTTPException(
            status_code=404,
            detail="Produto não encontrado"
        )

    db.delete(product)
    db.commit()

    return {
        "message": "Produto removido com sucesso"
    }