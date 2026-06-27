# Raízes do Nordeste API

API desenvolvida para o projeto multidisciplinar da trilha Back-End, com o objetivo de simular parte do sistema de pedidos da rede de lanchonetes **Raízes do Nordeste**.

A aplicação permite cadastro de usuários, autenticação com JWT, controle de acesso por perfil, gerenciamento de produtos, criação de pedidos, identificação do canal do pedido, pagamento mock e atualização de status.

## Tecnologias Utilizadas

* Python
* FastAPI
* PostgreSQL
* SQLAlchemy
* Pydantic
* JWT
* Uvicorn
* Swagger/OpenAPI

## Funcionalidades

* Cadastro de usuários.
* Login com autenticação JWT.
* Perfis de usuário: `CLIENTE` e `ADMIN`.
* Proteção de rotas por autenticação.
* Restrição de rotas administrativas para usuários `ADMIN`.
* CRUD de produtos.
* Criação e listagem de pedidos.
* Campo obrigatório `canalPedido`.
* Filtro de pedidos por canal.
* Pagamento mock aprovado ou recusado.
* Atualização de status do pedido.
* Tratamento padronizado de erros.
* Logs básicos de auditoria.

## Fluxo Principal

O fluxo principal implementado na API é:

```text
Cliente realiza pedido
→ Pedido é registrado com status PENDENTE
→ Pagamento mock é processado
→ Pedido é atualizado para PAGO ou RECUSADO
```

## Canais de Pedido

A API permite registrar pedidos pelos seguintes canais:

```text
APP
TOTEM
BALCAO
PICKUP
WEB
```

O campo `canalPedido` é obrigatório na criação de pedidos.

## Perfis de Usuário

### CLIENTE

Pode realizar login, consultar produtos e criar pedidos.

### ADMIN

Pode realizar login e gerenciar produtos, incluindo criação, edição e exclusão.

## Como Executar o Projeto

### 1. Clonar o repositório

```bash
git clone https://github.com/NicholasSouzaDEV/raizes-do-nordeste-backend.git
```

### 2. Entrar na pasta do projeto

```bash
cd raizes-do-nordeste-backend
```

### 3. Criar ambiente virtual

```bash
python -m venv venv
```

### 4. Ativar o ambiente virtual

No Windows:

```bash
venv\Scripts\activate
```

### 5. Instalar dependências

```bash
pip install -r requirements.txt
```

### 6. Configurar variáveis de ambiente

Crie um arquivo `.env` na raiz do projeto com base no arquivo `.env.example`.

Exemplo:

```env
DATABASE_URL=postgresql://usuario:senha@localhost:5432/nome_do_banco
```

### 7. Executar a aplicação

```bash
uvicorn main:app --reload
```

### 8. Acessar a documentação Swagger

Após iniciar o servidor, acesse:

```text
http://127.0.0.1:8000/docs
```

## Principais Endpoints

### Usuários e Autenticação

| Método | Rota     | Descrição                         |
| ------ | -------- | --------------------------------- |
| POST   | `/users` | Cadastra um usuário               |
| GET    | `/users` | Lista usuários                    |
| POST   | `/login` | Realiza login e retorna token JWT |

### Produtos

| Método | Rota                     | Descrição               |
| ------ | ------------------------ | ----------------------- |
| POST   | `/products`              | Cria produto            |
| GET    | `/products`              | Lista produtos          |
| GET    | `/products/{product_id}` | Consulta produto por ID |
| PUT    | `/products/{product_id}` | Atualiza produto        |
| DELETE | `/products/{product_id}` | Remove produto          |

### Pedidos

| Método | Rota                                    | Descrição                 |
| ------ | --------------------------------------- | ------------------------- |
| POST   | `/orders`                               | Cria pedido               |
| GET    | `/orders`                               | Lista pedidos             |
| GET    | `/orders?canalPedido=APP`               | Filtra pedidos por canal  |
| GET    | `/orders/{order_id}`                    | Consulta pedido por ID    |
| PUT    | `/orders/{order_id}/pay?aprovado=true`  | Simula pagamento aprovado |
| PUT    | `/orders/{order_id}/pay?aprovado=false` | Simula pagamento recusado |

## Exemplo de Criação de Pedido

```json
{
  "usuario_id": 1,
  "produto_id": 2,
  "quantidade": 3,
  "canalPedido": "APP"
}
```

Resposta esperada:

```json
{
  "id": 1,
  "usuario_id": 1,
  "produto_id": 2,
  "quantidade": 3,
  "total": 75.0,
  "status": "PENDENTE",
  "canalPedido": "APP"
}
```

## Exemplo de Pagamento Mock

Pagamento aprovado:

```text
PUT /orders/1/pay?aprovado=true
```

Resultado esperado:

```json
{
  "status": "PAGO"
}
```

Pagamento recusado:

```text
PUT /orders/1/pay?aprovado=false
```

Resultado esperado:

```json
{
  "status": "RECUSADO"
}
```

## Tratamento de Erros

A API possui tratamento padronizado de erros. Exemplo de erro para recurso inexistente:

```json
{
  "erro": true,
  "status_code": 404,
  "mensagem": "Produto não encontrado",
  "path": "/products/99999",
  "timestamp": "2026-06-26T00:00:00"
}
```

## Logs e Auditoria

A API registra logs básicos no terminal para ações importantes, como:

* criação de pedidos;
* pagamento aprovado ou recusado;
* consulta de pedidos inexistentes;
* criação, edição e remoção de produtos;
* consulta de produtos inexistentes.

Esses logs ajudam a acompanhar ações sensíveis e validar o funcionamento do sistema durante os testes.

## Plano de Testes

O plano de testes está documentado no arquivo:

```text
docs/plano_testes.md
```

Ele contém cenários positivos e negativos envolvendo autenticação, autorização, produtos, pedidos, canal do pedido, pagamento mock, erros padronizados e logs.

## Segurança

A API utiliza:

* autenticação JWT;
* hash de senha;
* controle de acesso por perfil;
* proteção de rotas administrativas;
* variáveis de ambiente para configuração sensível;
* `.env.example` para documentação sem expor credenciais reais.

## Status do Projeto

Projeto em desenvolvimento acadêmico, com foco nos requisitos principais da trilha Back-End:

* API REST;
* documentação Swagger;
* persistência em PostgreSQL;
* autenticação JWT;
* autorização por perfil;
* fluxo de pedido e pagamento mock;
* logs básicos;
* plano de testes.
