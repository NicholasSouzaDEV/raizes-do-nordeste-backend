from sqlalchemy.orm import Session
from fastapi import HTTPException

from app.models.order import Order
from app.models.product import Product


def create_order(
    db: Session,
    usuario_id: int,
    produto_id: int,
    quantidade: int,
    canal_pedido: str
):
    produto = (
        db.query(Product)
        .filter(Product.id == produto_id)
        .first()
    )

    if not produto:
        raise HTTPException(
            status_code=404,
            detail="Produto não encontrado"
        )

    total = produto.preco * quantidade

    order = Order(
        usuario_id=usuario_id,
        produto_id=produto_id,
        quantidade=quantidade,
        total=total,
        status="PENDENTE",
        canal_pedido=canal_pedido
    )

    db.add(order)
    db.commit()
    db.refresh(order)

    return order


def get_orders(
    db: Session,
    canal_pedido: str | None = None
):
    query = db.query(Order)

    if canal_pedido:
        query = query.filter(
            Order.canal_pedido == canal_pedido
        )

    return query.all()


def get_order_by_id(
    db: Session,
    order_id: int
):
    order = (
        db.query(Order)
        .filter(Order.id == order_id)
        .first()
    )

    if not order:
        raise HTTPException(
            status_code=404,
            detail="Pedido não encontrado"
        )

    return order


def pay_order(
    db: Session,
    order_id: int
):
    order = (
        db.query(Order)
        .filter(Order.id == order_id)
        .first()
    )

    if not order:
        raise HTTPException(
            status_code=404,
            detail="Pedido não encontrado"
        )

    order.status = "PAGO"

    db.commit()
    db.refresh(order)

    return order