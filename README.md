# Prog-Web

## Modelo do Banco de Dados

    Cliente {
        int id PK
        string nome
        int idade
        string endereco
        string email
        string telefone
        bool usuario
    }
    
    Usuario ||--|| Cliente: pertence_a
    Usuario ||--|| Fornecedor: pertence_a

    Produto {
        int id PK
        int fornecedor FK
        string nome
        float valor
        string descricao
        int estoque
        bool disponivel
    }
    
    Produto }|--|| Fornecedor: fornecido_por
    
    Fornecedor {
        int id PK
        string nome
        string endereco
        string email
    }

    Compras {
        int id PK
        int cliente FK
        date data
        float valor_total
        string status
    }
    
    Compras ||--|{ Cliente: feita_por
    Compras }|--|| Pagamento: tem
    
    ItensCompra {
        int id PK
        int compra_id FK
        int produto_id FK
        int quantidade
        float preco_unitario
    }
    
    Compras ||--|{ ItensCompra: contem
    ItensCompra ||--|{ Produto: inclui
    
    Pagamento {
        int id PK
        int compra_id FK
        string metodo
        date data_pagamento
        string status
    }

## Estrutura de Diretórios

``` bash
meuprojeto/
├── manage.py
├── exposicao_venda/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── cliente/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── forms.py
|   └── templates/
|       └── perfil.html
├── fornecedor/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── forms.py
|   └── templates/
|       └── produtos.html
├── produtos/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── forms.py
|   └── templates/
|       ├── lista_produtos.html
│       └── detalhe_produto.html
├── compras/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── forms.py
|   └── templates/
|       └── carrinho.html
└── static/
    ├── css/
    ├── js/
    └── images/
```
