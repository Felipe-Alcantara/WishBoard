# Wishlist Project

Este projeto é uma aplicação simples para gerenciar wishlists utilizando Django e Django REST Framework no backend e uma interface em HTML/JS para exibição dos dados em formato Kanban.

## Estrutura do Projeto

```
wishlist_project/
├── manage.py
├── wishlist_project/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── wishlist/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── migrations/
│   │   └── __init__.py
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   └── urls.py
├── templates/
│   └── index.html
├── static/
│   ├── css/
│   │   └── style.css
│   └── js/
│       └── app.js
├── requirements.txt
└── README.md
```

## Funcionalidades

- **API REST:** Disponível em `/api/items/` para gerenciamento dos itens.
- **Interface Frontend:** Consome a API e exibe os itens em formato Kanban.
- **Endpoint Markdown:** Acesse `/api/items/markdown/` para obter uma representação em Markdown dos itens.