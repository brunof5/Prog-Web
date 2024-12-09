# Prog-Web

## Modelo do Banco de Dados

    Cliente {
        int id PK
        string nome
        int idadezz
        string endereco
        string email
        string telefone
    }

    Fornecedor {
        int id PK
        string nome
        string endereco
        string email
    }

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

    Compras {
        int id PK
        int cliente FK
        date data
        float valor_total
        string status
    }
    
    Compras ||--|{ Cliente: feita_por
    
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

    Compras }|--|| Pagamento: tem

## Estrutura de Diretórios

``` bash
meuprojeto/
├── manage.py
├── db.sqlite3
├── exposicao_venda/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── my_site/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── tests.py
|   └── templates/
|       └── base_my_site.html
├── cliente/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── views.py
│   ├── urls.py
<<<<<<< HEAD
<<<<<<< HEAD
│   ├── tests.py
|   └── templates/
|       └── cliente/
|           └── atualizar.html
|           └── base_cliente.html
|           └── criar.html
|           └── deletar.html
|           └── listar.html
|           └── perfil.html
=======
│   ├── forms.py
│   └── templates/
│       └── perfil.html
>>>>>>> 2df6afff5b79fd107a846f3c554bb7251d0b7866
=======
│   ├── forms.py
│   └── templates/
│       └── perfil.html
>>>>>>> 2df6afff5b79fd107a846f3c554bb7251d0b7866
├── fornecedor/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── views.py
│   ├── urls.py
<<<<<<< HEAD
<<<<<<< HEAD
│   ├── tests.py
|   └── templates/
=======
│   ├── forms.py
│   └── templates/
│       └── produtos.html
>>>>>>> 2df6afff5b79fd107a846f3c554bb7251d0b7866
=======
│   ├── forms.py
│   └── templates/
│       └── produtos.html
>>>>>>> 2df6afff5b79fd107a846f3c554bb7251d0b7866
├── produtos/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── views.py
│   ├── urls.py
<<<<<<< HEAD
<<<<<<< HEAD
│   ├── tests.py
|   └── templates/
=======
=======
>>>>>>> 2df6afff5b79fd107a846f3c554bb7251d0b7866
│   ├── forms.py
│   └── templates/
│       ├── lista_produtos.html
│       └── detalhe_produto.html
>>>>>>> 2df6afff5b79fd107a846f3c554bb7251d0b7866
├── compras/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── views.py
│   ├── urls.py
<<<<<<< HEAD
<<<<<<< HEAD
│   ├── tests.py
|   └── templates/
├── itens_compra/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── tests.py
|   └── templates/
├── pagamento/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── tests.py
|   └── templates/
├── web (venv)
├── templates/
|   └── base.html
├──  static/
|   ├── css/
|   ├── js/
|   └── images/
└── README.md 
=======
=======
>>>>>>> 2df6afff5b79fd107a846f3c554bb7251d0b7866
│   ├── forms.py
│   └── templates/
│       └── carrinho.html
└── static/
    ├── css/
    ├── js/
    └── images/
>>>>>>> 2df6afff5b79fd107a846f3c554bb7251d0b7866
```
