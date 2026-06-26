from sqlalchemy import Column, Integer, Float, ForeignKey, String

from app.database.database import Base


class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)
    usuario_id = Column(Integer)
    produto_id = Column(Integer)
    quantidade = Column(Integer)
    total = Column(Float)

    status = Column(String(20), default="PENDENTE")
    