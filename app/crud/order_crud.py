from sqlalchemy.orm import Session

from app.models.order import Order
from app.models.product import Product
from fastapi import HTTPException

def create_order(
    db: Session,
    usuario_id: int,
    produto_id: int,
    quantidade: int
):

    produto = (
        db.query(Product)
        .filter(Product.id == produto_id)
        .first()
    )

    if not produto:
        return None

    total = produto.preco * quantidade

    order = Order(
        usuario_id=usuario_id,
        produto_id=produto_id,
        quantidade=quantidade,
        total=total,
        status="PENDENTE"
    )

    db.add(order)
    db.commit()
    db.refresh(order)

    return order


def get_orders(db: Session):
    return db.query(Order).all()


def get_order_by_id(
    db: Session,
    order_id: int
):
    return (
        db.query(Order)
        .filter(Order.id == order_id)
        .first()
    )
    

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