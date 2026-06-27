# Diagrama de Casos de Uso

Este documento apresenta o Diagrama de Casos de Uso da API Raízes do Nordeste. O objetivo é representar as principais interações entre os atores do sistema e as funcionalidades implementadas.

## Atores

### CLIENTE

Representa o usuário comum do sistema. Pode realizar login, consultar produtos, criar pedidos e realizar pagamento mock.

### ADMIN

Representa o usuário administrador. Além das funcionalidades básicas, pode gerenciar os produtos cadastrados no sistema.

## Casos de Uso

- Cadastrar usuário.
- Realizar login.
- Consultar produtos.
- Criar pedido.
- Filtrar pedidos por canal.
- Consultar pedido.
- Realizar pagamento mock.
- Gerenciar produtos.
- Consultar logs básicos pelo terminal durante a execução da API.

## Diagrama

```mermaid
flowchart LR
    CLIENTE([CLIENTE])
    ADMIN([ADMIN])

    UC1((Cadastrar usuário))
    UC2((Realizar login))
    UC3((Consultar produtos))
    UC4((Criar pedido))
    UC5((Filtrar pedidos por canal))
    UC6((Consultar pedido))
    UC7((Realizar pagamento mock))
    UC8((Gerenciar produtos))
    UC9((Criar produto))
    UC10((Editar produto))
    UC11((Remover produto))
    UC12((Consultar usuários))

    CLIENTE --> UC1
    CLIENTE --> UC2
    CLIENTE --> UC3
    CLIENTE --> UC4
    CLIENTE --> UC5
    CLIENTE --> UC6
    CLIENTE --> UC7

    ADMIN --> UC2
    ADMIN --> UC3
    ADMIN --> UC8
    ADMIN --> UC12

    UC8 --> UC9
    UC8 --> UC10
    UC8 --> UC11