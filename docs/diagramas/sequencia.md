# Diagrama de Sequência - Fluxo Principal

Este documento apresenta o Diagrama de Sequência do fluxo principal da API Raízes do Nordeste, contemplando a criação de pedido, validação do produto, cálculo do total, registro do pedido, processamento do pagamento mock e atualização do status.

## Fluxo Representado

O fluxo principal implementado segue a sequência:

1. Cliente realiza login e obtém token JWT.
2. Cliente cria um pedido informando usuário, produto, quantidade e canal do pedido.
3. API valida os dados recebidos.
4. API consulta o produto no banco de dados.
5. API calcula o total do pedido.
6. Pedido é registrado com status `PENDENTE`.
7. Cliente aciona o pagamento mock.
8. API processa o pagamento como aprovado ou recusado.
9. Status do pedido é atualizado para `PAGO` ou `RECUSADO`.

## Diagrama

```mermaid
sequenceDiagram
    actor Cliente
    participant Swagger as Swagger/Postman
    participant API as FastAPI
    participant Auth as JWT/Auth
    participant DB as PostgreSQL
    participant Pagamento as Pagamento Mock

    Cliente->>Swagger: Informa login e senha
    Swagger->>API: POST /login
    API->>DB: Busca usuário pelo e-mail
    DB-->>API: Retorna usuário
    API->>Auth: Valida senha e gera token JWT
    Auth-->>API: Token gerado
    API-->>Swagger: Retorna access_token
    Swagger-->>Cliente: Exibe token JWT

    Cliente->>Swagger: Cria pedido
    Swagger->>API: POST /orders com token JWT
    API->>Auth: Valida token JWT
    Auth-->>API: Token válido

    API->>DB: Consulta produto pelo produto_id
    DB-->>API: Retorna produto

    API->>API: Calcula total = preço x quantidade
    API->>DB: Salva pedido com status PENDENTE e canalPedido
    DB-->>API: Retorna pedido criado
    API-->>Swagger: Retorna pedido criado
    Swagger-->>Cliente: Exibe pedido PENDENTE

    Cliente->>Swagger: Solicita pagamento
    Swagger->>API: PUT /orders/{id}/pay?aprovado=true/false
    API->>Auth: Valida token JWT
    Auth-->>API: Token válido

    API->>DB: Busca pedido pelo ID
    DB-->>API: Retorna pedido

    API->>Pagamento: Processa pagamento mock
    Pagamento-->>API: Resultado aprovado ou recusado

    alt Pagamento aprovado
        API->>DB: Atualiza status para PAGO
        DB-->>API: Pedido atualizado
        API-->>Swagger: Retorna pedido com status PAGO
    else Pagamento recusado
        API->>DB: Atualiza status para RECUSADO
        DB-->>API: Pedido atualizado
        API-->>Swagger: Retorna pedido com status RECUSADO
    end

    Swagger-->>Cliente: Exibe resultado do pagamento
```

## Observação

O pagamento utilizado no projeto é uma simulação, também chamado de pagamento mock. Ele não se comunica com um gateway real de pagamento. A API recebe o parâmetro `aprovado`, e com base nele altera o status do pedido para `PAGO` ou `RECUSADO`.

Esse fluxo representa o principal processo de negócio da aplicação: criação do pedido, registro no banco de dados, pagamento simulado e atualização do status.
