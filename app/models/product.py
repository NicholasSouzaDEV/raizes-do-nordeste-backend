from sqlalchemy import Column, Integer, String, Float

from app.database.database import Base


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(100))
    descricao = Column(String(255))
    preco = Column(Float)