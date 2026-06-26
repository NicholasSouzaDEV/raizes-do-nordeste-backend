from fastapi import FastAPI, Depends
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app.database.database import (
    engine,
    Base,
    get_db
)

# ==========================
# Models
# ==========================
from app.models.user import User
from app.models.product import Product
from app.models.order import Order

# ==========================
# Schemas
# ==========================
from app.schemas.user_schema import (
    UserCreate,
    UserResponse,
    TokenResponse
)

from app.schemas.product_schema import (
    ProductCreate,
    ProductResponse
)

from app.schemas.order_schema import (
    OrderCreate,
    OrderResponse
)

# ==========================
# CRUD
# ==========================
from app.crud.user_crud import (
    create_user,
    get_users,
    login_user
)

from app.crud.product_crud import (
    create_product,
    get_products,
    get_product_by_id,
    update_product,
    delete_product
)

from app.crud.order_crud import (
    create_order,
    get_orders,
    get_order_by_id,
    pay_order
)

# ==========================
# Security
# ==========================
from app.services.security import (
    get_current_user,
    get_current_admin
)


Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Raízes do Nordeste API",
    version="1.0.0"
)

# ======================================================
# HOME
# ======================================================

@app.get("/")
def home():
    return {
        "message": "API Raízes do Nordeste funcionando"
    }


# ======================================================
# USUÁRIOS / AUTENTICAÇÃO
# ======================================================

@app.post(
    "/users",
    response_model=UserResponse
)
def create_new_user(
    user: UserCreate,
    db: Session = Depends(get_db)
):
    return create_user(
        db,
        user.nome,
        user.email,
        user.senha,
        user.perfil
    )


@app.get(
    "/users",
    response_model=list[UserResponse]
)
def list_users(
    db: Session = Depends(get_db)
):
    return get_users(db)


@app.post(
    "/login",
    response_model=TokenResponse
)
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):
    result = login_user(
        db,
        form_data.username,
        form_data.password
    )

    if not result:
        return {
            "access_token": "",
            "token_type": "invalid"
        }

    return result


# ======================================================
# PRODUTOS
# ======================================================

@app.post(
    "/products",
    response_model=ProductResponse
)
def create_new_product(
    product: ProductCreate,
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_admin)
):
    return create_product(
        db,
        product.nome,
        product.descricao,
        product.preco
    )


@app.get(
    "/products",
    response_model=list[ProductResponse]
)
def list_products(
    db: Session = Depends(get_db)
):
    return get_products(db)


@app.get(
    "/products/{product_id}",
    response_model=ProductResponse
)
def get_product(
    product_id: int,
    db: Session = Depends(get_db)
):
    return get_product_by_id(
        db,
        product_id
    )


@app.put(
    "/products/{product_id}",
    response_model=ProductResponse
)
def edit_product(
    product_id: int,
    product: ProductCreate,
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_admin)
):
    return update_product(
        db,
        product_id,
        product.nome,
        product.descricao,
        product.preco
    )


@app.delete("/products/{product_id}")
def remove_product(
    product_id: int,
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_admin)
):
    return delete_product(
        db,
        product_id
    )


# ======================================================
# PEDIDOS
# ======================================================

@app.post(
    "/orders",
    response_model=OrderResponse
)
def create_new_order(
    order: OrderCreate,
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user)
):
    return create_order(
    db,
    order.usuario_id,
    order.produto_id,
    order.quantidade,
    order.canalPedido
)


@app.get(
    "/orders",
    response_model=list[OrderResponse]
)
def list_orders(
    canalPedido: str | None = None,
    db: Session = Depends(get_db)
):
    return get_orders(
        db,
        canalPedido
    )


@app.get(
    "/orders/{order_id}",
    response_model=OrderResponse
)
def get_order(
    order_id: int,
    db: Session = Depends(get_db)
):
    return get_order_by_id(
        db,
        order_id
    )


@app.put(
    "/orders/{order_id}/pay",
    response_model=OrderResponse
)
def payment_order(
    order_id: int,
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user)
):
    return pay_order(
        db,
        order_id
    )
    