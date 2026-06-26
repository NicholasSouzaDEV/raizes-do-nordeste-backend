from sqlalchemy import Column, Integer, Float, String

from app.database.database import Base


class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)
    usuario_id = Column(Integer)
    produto_id = Column(Integer)
    quantidade = Column(Integer)
    total = Column(Float)

    status = Column(String(20), default="PENDENTE")

    canal_pedido = Column(String(20), nullable=False, default="WEB")

    @property
    def canalPedido(self):
        return self.canal_pedido