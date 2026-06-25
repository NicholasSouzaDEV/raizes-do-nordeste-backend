from sqlalchemy import Column, Integer, Float, ForeignKey

from app.database.database import Base


class Order(Base):
    __tablename__ = "orders"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    usuario_id = Column(
        Integer,
        ForeignKey("users.id")
    )

    produto_id = Column(
        Integer,
        ForeignKey("products.id")
    )

    quantidade = Column(Integer)

    total = Column(Float)

    