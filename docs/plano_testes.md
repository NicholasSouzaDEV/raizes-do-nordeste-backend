# Plano de Testes - Raízes do Nordeste API

Este documento apresenta os principais cenários de teste utilizados para validar a API Raízes do Nordeste. Os testes foram realizados por meio da documentação interativa Swagger, disponível em `/docs`, considerando autenticação JWT, controle de perfil, CRUD de produtos, criação de pedidos, pagamento mock, validação de canal do pedido e tratamento padronizado de erros.

## Objetivo

Validar se a API atende aos requisitos funcionais e não funcionais principais do projeto, garantindo que os recursos implementados funcionem corretamente, que as regras de autenticação e autorização sejam respeitadas e que erros sejam retornados de forma padronizada.

## Ambiente de Teste

* Backend: FastAPI
* Banco de dados: PostgreSQL
* Documentação/Testes: Swagger UI
* Autenticação: JWT Bearer Token
* Perfis utilizados: CLIENTE e ADMIN

## Cenários de Teste

| Nº | Cenário                          | Tipo     | Entrada / Ação                                                                           | Resultado Esperado                                             | Status    |
| -- | -------------------------------- | -------- | ---------------------------------------------------------------------------------------- | -------------------------------------------------------------- | --------- |
| 1  | Cadastro de usuário válido       | Positivo | Enviar nome, e-mail, senha e perfil em `POST /users`                                     | Usuário cadastrado com sucesso e retorno dos dados sem a senha | Executado |
| 2  | Login válido                     | Positivo | Enviar e-mail e senha corretos em `POST /login`                                          | Retorno de `access_token` e `token_type` como `bearer`         | Executado |
| 3  | Login inválido                   | Negativo | Enviar e-mail ou senha incorretos em `POST /login`                                       | Login não autorizado ou retorno inválido                       | Executado |
| 4  | Criar produto como ADMIN         | Positivo | Usuário ADMIN autenticado envia dados em `POST /products`                                | Produto criado com sucesso                                     | Executado |
| 5  | Criar produto como CLIENTE       | Negativo | Usuário CLIENTE tenta acessar `POST /products`                                           | API retorna erro `403`, pois apenas ADMIN pode criar produto   | Executado |
| 6  | Listar produtos                  | Positivo | Acessar `GET /products`                                                                  | API retorna lista de produtos cadastrados                      | Executado |
| 7  | Consultar produto inexistente    | Negativo | Acessar `GET /products/99999`                                                            | API retorna erro `404` com mensagem padronizada                | Executado |
| 8  | Criar pedido com canal válido    | Positivo | Enviar `usuario_id`, `produto_id`, `quantidade` e `canalPedido` válido em `POST /orders` | Pedido criado com status inicial `PENDENTE`                    | Executado |
| 9  | Criar pedido com canal inválido  | Negativo | Enviar `canalPedido` inválido, como `"6"`                                                | API retorna erro `422` de validação                            | Executado |
| 10 | Filtrar pedidos por canal        | Positivo | Acessar `GET /orders?canalPedido=APP`                                                    | API retorna apenas pedidos do canal informado                  | Executado |
| 11 | Pagamento mock aprovado          | Positivo | Acessar `PUT /orders/{id}/pay?aprovado=true`                                             | Status do pedido alterado para `PAGO`                          | Executado |
| 12 | Pagamento mock recusado          | Positivo | Acessar `PUT /orders/{id}/pay?aprovado=false`                                            | Status do pedido alterado para `RECUSADO`                      | Executado |
| 13 | Consultar pedido inexistente     | Negativo | Acessar `GET /orders/99999`                                                              | API retorna erro `404` com mensagem padronizada                | Executado |
| 14 | Acessar rota protegida sem token | Negativo | Tentar acessar rota protegida sem autenticação                                           | API retorna erro de autenticação                               | Executado |

## Validações Realizadas

Durante os testes, foram validados os seguintes pontos:

* Funcionamento do cadastro de usuários.
* Funcionamento do login com JWT.
* Proteção de rotas por autenticação.
* Restrição de ações administrativas ao perfil ADMIN.
* Criação, listagem, edição e exclusão de produtos.
* Criação de pedidos com cálculo automático do total.
* Uso obrigatório do campo `canalPedido`.
* Validação dos canais permitidos: `APP`, `TOTEM`, `BALCAO`, `PICKUP` e `WEB`.
* Filtro de pedidos por canal.
* Fluxo de pagamento mock aprovado e recusado.
* Atualização de status do pedido.
* Retorno padronizado de erros.
* Geração de logs básicos de auditoria.

## Evidências Esperadas

As evidências dos testes podem ser registradas por meio de capturas de tela do Swagger, mostrando:

* Requisições executadas.
* Códigos de status HTTP retornados.
* Corpo da resposta da API.
* Token JWT sendo utilizado no botão Authorize.
* Logs exibidos no terminal do Uvicorn durante criação de pedidos, pagamentos e ações administrativas.

## Conclusão

Os testes realizados demonstram que a API Raízes do Nordeste atende ao fluxo principal definido para o projeto, contemplando autenticação, autorização, gerenciamento de produtos, criação de pedidos, identificação do canal do pedido, pagamento mock e tratamento padronizado de erros. Os cenários positivos e negativos ajudam a comprovar a estabilidade básica da aplicação e o atendimento aos requisitos definidos para a trilha Back-End.
