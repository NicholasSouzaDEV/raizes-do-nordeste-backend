from sqlalchemy.orm import Session
from fastapi import HTTPException
import logging

from app.models.product import Product


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


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

    logger.info(
        f"Produto criado com sucesso. "
        f"produto_id={product.id}, "
        f"nome={product.nome}, "
        f"preco={product.preco}"
    )

    return product


def get_products(db: Session):
    logger.info("Consulta de lista de produtos realizada.")

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
        logger.warning(
            f"Tentativa de consultar produto inexistente. produto_id={product_id}"
        )

        raise HTTPException(
            status_code=404,
            detail="Produto não encontrado"
        )

    logger.info(
        f"Produto consultado com sucesso. produto_id={product_id}"
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
        logger.warning(
            f"Tentativa de atualizar produto inexistente. produto_id={product_id}"
        )

        raise HTTPException(
            status_code=404,
            detail="Produto não encontrado"
        )

    product.nome = nome
    product.descricao = descricao
    product.preco = preco

    db.commit()
    db.refresh(product)

    logger.info(
        f"Produto atualizado com sucesso. "
        f"produto_id={product.id}, "
        f"nome={product.nome}, "
        f"preco={product.preco}"
    )

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
        logger.warning(
            f"Tentativa de remover produto inexistente. produto_id={product_id}"
        )

        raise HTTPException(
            status_code=404,
            detail="Produto não encontrado"
        )

    db.delete(product)
    db.commit()

    logger.info(
        f"Produto removido com sucesso. produto_id={product_id}"
    )

    return {
        "message": "Produto removido com sucesso"
    }