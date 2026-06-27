from sqlalchemy.orm import Session
from fastapi import HTTPException
import logging

from app.models.order import Order
from app.models.product import Product


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


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
        logger.warning(
            f"Tentativa de criar pedido com produto inexistente. produto_id={produto_id}"
        )

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

    logger.info(
        f"Pedido criado com sucesso. "
        f"pedido_id={order.id}, "
        f"usuario_id={usuario_id}, "
        f"produto_id={produto_id}, "
        f"quantidade={quantidade}, "
        f"canal_pedido={canal_pedido}, "
        f"status={order.status}"
    )

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

        logger.info(
            f"Consulta de pedidos filtrada por canal. canal_pedido={canal_pedido}"
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
        logger.warning(
            f"Tentativa de consultar pedido inexistente. pedido_id={order_id}"
        )

        raise HTTPException(
            status_code=404,
            detail="Pedido não encontrado"
        )

    return order


def pay_order(
    db: Session,
    order_id: int,
    aprovado: bool = True
):
    order = (
        db.query(Order)
        .filter(Order.id == order_id)
        .first()
    )

    if not order:
        logger.warning(
            f"Tentativa de pagamento em pedido inexistente. pedido_id={order_id}"
        )

        raise HTTPException(
            status_code=404,
            detail="Pedido não encontrado"
        )

    if aprovado:
        order.status = "PAGO"
    else:
        order.status = "RECUSADO"

    db.commit()
    db.refresh(order)

    logger.info(
        f"Pagamento mock processado. "
        f"pedido_id={order.id}, "
        f"aprovado={aprovado}, "
        f"novo_status={order.status}"
    )

    return order