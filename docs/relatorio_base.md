# Relatório Base - Projeto Raízes do Nordeste API

## Capa

**Projeto:** Raízes do Nordeste API
**Trilha:** Back-End
**Aluno:** Nicholas Souza de Souza
**Curso:** Projeto Multidisciplinar
**Tecnologia principal:** FastAPI com PostgreSQL

---

## 1. Introdução

Este relatório apresenta o desenvolvimento da API **Raízes do Nordeste**, criada como parte do projeto multidisciplinar da trilha Back-End. O objetivo da aplicação é simular parte do funcionamento de um sistema de pedidos para uma rede de lanchonetes, permitindo cadastro de usuários, autenticação, gerenciamento de produtos, criação de pedidos, identificação do canal do pedido, pagamento mock e atualização de status.

A API foi desenvolvida com foco em boas práticas básicas de desenvolvimento back-end, incluindo persistência em banco de dados, autenticação JWT, controle de acesso por perfil, documentação via Swagger, tratamento padronizado de erros, logs de auditoria e plano de testes.

---

## 2. Análise do Problema

A rede Raízes do Nordeste necessita de uma solução capaz de registrar pedidos realizados por diferentes canais, como aplicativo, totem, balcão, pickup e web. Além disso, o sistema precisa permitir que usuários se autentiquem, que administradores gerenciem produtos e que pedidos tenham seu status atualizado conforme o resultado do pagamento.

O problema central resolvido pela API é organizar o fluxo básico de pedido, garantindo que os dados sejam persistidos no banco e que o processo principal possa ser acompanhado por meio de status e logs.

---

## 3. Requisitos Funcionais

Os principais requisitos funcionais implementados foram:

* Cadastro de usuários.
* Login com autenticação JWT.
* Controle de perfil de usuário: `CLIENTE` e `ADMIN`.
* Cadastro, listagem, consulta, edição e remoção de produtos.
* Proteção de rotas administrativas para usuários com perfil `ADMIN`.
* Criação de pedidos.
* Registro do canal do pedido por meio do campo `canalPedido`.
* Filtro de pedidos por canal.
* Pagamento mock aprovado ou recusado.
* Atualização de status do pedido.
* Consulta de pedidos.
* Tratamento de erros para recursos inexistentes ou dados inválidos.

---

## 4. Requisitos Não Funcionais

Os principais requisitos não funcionais considerados foram:

* Utilização de API REST.
* Persistência real em banco PostgreSQL.
* Documentação automática com Swagger/OpenAPI.
* Uso de variáveis de ambiente para dados sensíveis.
* Armazenamento de senha com hash.
* Autenticação com JWT.
* Controle de autorização por perfil.
* Logs básicos de auditoria.
* Padrão consistente de resposta para erros.
* Organização do projeto em camadas simples: models, schemas, crud, services e database.
* Versionamento com Git e repositório público no GitHub.

---

## 5. Tecnologias Utilizadas

O projeto foi desenvolvido utilizando as seguintes tecnologias:

* Python
* FastAPI
* PostgreSQL
* SQLAlchemy
* Pydantic
* Uvicorn
* JWT
* Passlib
* Swagger/OpenAPI
* Git e GitHub
* Postman

---

## 6. Arquitetura da Aplicação

A API foi organizada em uma estrutura simples e modular, separando responsabilidades em diferentes pastas.

Estrutura principal:

```text
app/
├── crud/
│   ├── user_crud.py
│   ├── product_crud.py
│   └── order_crud.py
├── database/
│   └── database.py
├── models/
│   ├── user.py
│   ├── product.py
│   └── order.py
├── schemas/
│   ├── user_schema.py
│   ├── product_schema.py
│   └── order_schema.py
└── services/
    └── security.py
```

A camada `models` representa as tabelas do banco de dados.
A camada `schemas` define os formatos de entrada e saída da API.
A camada `crud` concentra as operações de banco de dados.
A camada `services` contém regras auxiliares, como autenticação, hash de senha e geração de token JWT.
O arquivo `main.py` concentra a criação da aplicação FastAPI e a definição das rotas.

---

## 7. Modelagem de Dados

O banco de dados possui três entidades principais:

### users

Representa os usuários cadastrados no sistema.

Campos principais:

* `id`
* `nome`
* `email`
* `senha`
* `perfil`

### products

Representa os produtos disponíveis para venda.

Campos principais:

* `id`
* `nome`
* `descricao`
* `preco`

### orders

Representa os pedidos realizados pelos usuários.

Campos principais:

* `id`
* `usuario_id`
* `produto_id`
* `quantidade`
* `total`
* `status`
* `canal_pedido`

O relacionamento lógico definido é:

* Um usuário pode realizar vários pedidos.
* Um produto pode estar presente em vários pedidos.
* Um pedido está associado a um usuário e a um produto.

O DER foi documentado no arquivo:

```text
docs/diagramas/der.md
```

---

## 8. Diagramas

Os diagramas do projeto foram documentados na pasta:

```text
docs/diagramas/
```

Arquivos criados:

* `der.md`: Diagrama Entidade-Relacionamento.
* `casos_uso.md`: Diagrama de Casos de Uso.
* `classes.md`: Diagrama de Classes.
* `sequencia.md`: Diagrama de Sequência do fluxo principal.

Esses diagramas representam a estrutura de dados, os atores do sistema, as classes principais e o fluxo de criação de pedido com pagamento mock.

---

## 9. Autenticação e Autorização

A API utiliza autenticação baseada em JWT. O usuário realiza login por meio da rota:

```text
POST /login
```

Após o login, a API retorna um token do tipo `bearer`, que deve ser utilizado no botão **Authorize** do Swagger para acessar rotas protegidas.

O sistema possui dois perfis principais:

* `CLIENTE`
* `ADMIN`

Rotas administrativas, como criação, edição e exclusão de produtos, exigem perfil `ADMIN`. Caso um usuário com perfil `CLIENTE` tente acessar uma rota restrita, a API retorna erro de autorização.

---

## 10. Principais Endpoints

### Usuários

| Método | Rota     | Descrição        |
| ------ | -------- | ---------------- |
| POST   | `/users` | Cadastra usuário |
| GET    | `/users` | Lista usuários   |
| POST   | `/login` | Realiza login    |

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

---

## 11. Fluxo Principal Implementado

O fluxo principal escolhido foi:

```text
Pedido → Pagamento mock → Atualização de status
```

O processo funciona da seguinte forma:

1. O usuário autenticado cria um pedido.
2. A API consulta o produto informado.
3. O valor total é calculado com base no preço do produto e na quantidade.
4. O pedido é salvo no banco com status `PENDENTE`.
5. O pagamento mock é processado.
6. Se aprovado, o pedido recebe status `PAGO`.
7. Se recusado, o pedido recebe status `RECUSADO`.

Esse fluxo foi documentado também no diagrama de sequência.

---

## 12. Canal do Pedido

O campo `canalPedido` foi implementado como obrigatório na criação de pedidos.

Canais aceitos:

* `APP`
* `TOTEM`
* `BALCAO`
* `PICKUP`
* `WEB`

Também foi implementado filtro por canal na rota:

```text
GET /orders?canalPedido=APP
```

Caso seja enviado um canal inválido, a API retorna erro de validação.

---

## 13. Tratamento Padronizado de Erros

A API possui tratamento padronizado para erros HTTP e erros de validação.

Exemplo de erro para recurso inexistente:

```json
{
  "erro": true,
  "status_code": 404,
  "mensagem": "Produto não encontrado",
  "path": "/products/99999",
  "timestamp": "2026-06-26T00:00:00"
}
```

Exemplo de erro de validação:

```json
{
  "erro": true,
  "status_code": 422,
  "mensagem": "Erro de validação dos dados enviados",
  "detalhes": [],
  "path": "/orders",
  "timestamp": "2026-06-26T00:00:00"
}
```

Esse padrão facilita a leitura dos erros e melhora a consistência das respostas da API.

---

## 14. Segurança, LGPD e Auditoria

Foram aplicadas medidas básicas de segurança, como:

* Hash de senha antes do armazenamento.
* Autenticação via JWT.
* Controle de acesso por perfil.
* Proteção de rotas administrativas.
* Uso de `.env` para variáveis sensíveis.
* Uso de `.env.example` para documentação sem expor credenciais.
* Logs básicos de auditoria.

A API registra logs no terminal para ações importantes, como:

* Criação de pedidos.
* Pagamento mock aprovado ou recusado.
* Tentativas de consultar pedidos inexistentes.
* Criação, edição e remoção de produtos.
* Tentativas de consultar produtos inexistentes.

Esses logs auxiliam no acompanhamento de ações sensíveis durante a execução da aplicação.

---

## 15. Plano de Testes

Foi criado o arquivo:

```text
docs/plano_testes.md
```

O plano de testes contém cenários positivos e negativos, incluindo:

* Cadastro de usuário.
* Login válido.
* Login inválido.
* Criação de produto como ADMIN.
* Tentativa de criação de produto como CLIENTE.
* Criação de pedido com canal válido.
* Criação de pedido com canal inválido.
* Pagamento mock aprovado.
* Pagamento mock recusado.
* Consulta de produto inexistente.
* Consulta de pedido inexistente.
* Filtro de pedidos por canal.

Os testes foram realizados principalmente pelo Swagger UI e também documentados para uso em Postman.

---

## 16. Coleção Postman

Foi criada uma coleção Postman no arquivo:

```text
docs/postman_collection.json
```

A coleção contém requisições para testar os principais recursos da API, incluindo login, usuários, produtos, pedidos, pagamento mock e cenários de erro.

---

## 17. Versionamento

O projeto foi versionado com Git e hospedado em repositório público no GitHub.

Foram realizados commits ao longo do desenvolvimento, registrando a evolução da API, incluindo autenticação, pedidos, pagamento mock, logs, tratamento de erros, documentação, plano de testes, coleção Postman e diagramas.

---

## 18. Conclusão

O desenvolvimento da API Raízes do Nordeste permitiu aplicar conceitos importantes da trilha Back-End, como criação de API REST, persistência em banco de dados, autenticação, autorização, validação de dados, documentação automática, tratamento de erros e logs.

A aplicação atende ao fluxo principal definido para o projeto, permitindo que usuários criem pedidos, informem o canal de origem, simulem pagamentos e acompanhem a atualização do status. Além disso, o projeto conta com documentação técnica, plano de testes, coleção Postman e diagramas de apoio.

Como melhoria futura, poderiam ser implementadas funcionalidades como controle de estoque, relacionamento físico com chaves estrangeiras no banco, migrations com Alembic, painel administrativo, envio de notificações e integração com gateway real de pagamento.

---

## 19. Declaração de Uso de IA

Durante o desenvolvimento do projeto, foi utilizada uma ferramenta de inteligência artificial como apoio para organização de ideias, revisão de textos, estruturação da documentação, explicações conceituais e auxílio na resolução de erros.

A implementação foi conduzida pelo aluno, com testes realizados no ambiente local, ajustes no código, versionamento em GitHub e validação dos endpoints por meio do Swagger.

Exemplos de uso da IA:

* Organização do README.
* Apoio na criação do plano de testes.
* Sugestões de estrutura para diagramas.
* Explicação de erros encontrados durante os testes.
* Apoio na redação do relatório.

O conteúdo final deve ser revisado pelo aluno antes da entrega.
