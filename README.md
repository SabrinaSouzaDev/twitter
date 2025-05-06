# 🐦 Mini Twitter

Application ID 86a83nfjn

Projeto de rede social minimalista inspirado no Twitter. Permite autenticação de usuários, publicação de posts (tweets), curtidas, seguidores e geração de feed.

## 📁 Estrutura do Projeto

```
.
├── apps
│   ├── accounts
│   ├── feeds
│   ├── follows
│   ├── __init__.py
│   ├── posts
│   └── __pycache__
├── cspell.json
├── docker
│   └── Dockerfile
├── docker-compose.yml
├── manage.py
├── mini_twitter
│   ├── asgi.py
│   ├── docs
│   ├── __init__.py
│   ├── pagination.py
│   ├── __pycache__
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── README.md
├── requirements.txt
├── setup.cfg
├── staticfiles
│   ├── admin
│   ├── drf-yasg
│   └── rest_framework
└── venv
    ├── bin
    ├── include
    ├── lib
    ├── lib64 -> lib
    └── pyvenv.cfg
```

DESCRIPTION

You are tasked with implementing a scalable REST API for a simple social media platform ("Mini-Twitter"), where users can:

Register and authenticate themselves.

Create, edit, delete, and like posts.

Follow and unfollow other users.

View their feed, which should display posts from the users they follow.

The project should demonstrate your ability to build a scalable, secure, and well-tested system using modern backend development practices.



### Diagrama
```bash
MINI-TWITTER ERD
───────────────────────────────────────────────────────────────────

USER
+-------------+--------------+-------------------------------+
| PK | id     | SERIAL       | Primary Key                  |
|    | username | VARCHAR(150) | Unique, Not Null            |
|    | email   | VARCHAR(254) | Unique, Not Null            |
|    | password | VARCHAR(128) | Hashed, Not Null            |
|    | bio     | TEXT         | Optional                     |
|    | created_at | TIMESTAMP | auto_now_add                |
|    | updated_at | TIMESTAMP | auto_now                    |
+-------------+--------------+-------------------------------+

       ▲
       │
       │ 1
       │
       │
       ▼
POST
+-------------+--------------+---------------------------------------------+
| PK | id     | SERIAL       | Primary Key                                |
| FK | author_id | INTEGER   | ForeignKey → USER(id), CASCADE on delete  |
|    | content | TEXT         | Not Null                                  |
|    | image   | VARCHAR(255) | Optional (image path)                     |
|    | created_at | TIMESTAMP | auto_now_add                              |
|    | updated_at | TIMESTAMP | auto_now                                  |
+-------------+--------------+---------------------------------------------+

       ▲
       │
       │ *
       │
       ▼
POST_LIKE (Junction Table)
+----------------+----------------+
| PK | post_id    | FK → POST.id |
| PK | user_id    | FK → USER.id |
|    | created_at | TIMESTAMP     |
+----------------+----------------+

FOLLOW
+----------------+----------------------------+
| PK | id         | SERIAL                    |
| FK | from_user  | INTEGER → USER.id         |
| FK | to_user    | INTEGER → USER.id         |
|    | created_at | TIMESTAMP                 |
+----------------+----------------------------+
* Evitar duplicidade com constraint única (from_user, to_user)

```

## 🚀 Funcionalidades

- Registro e login de usuários (autenticação via JWT)
- Criação, visualização e edição de posts (tweets)
- Curtidas em posts
- Sistema de seguidores (follow/unfollow)
- Feed cronológico dos usuários seguidos
- Documentação da API via Swagger/OpenAPI (drf-spectacular)
- Proteção com throttling, paginação e permissões

## 🛠️ Tecnologias Utilizadas

- **Backend**: Django, Django REST Framework, Simple JWT
- **Banco de Dados**: PostgreSQL
- **Documentação da API**: drf-spectacular
- **Containerização**: Docker & Docker Compose
- **CI/CD**: GitHub Actions


⚙️ Como Executar
✅ Usando Docker
```bash
git clone https://github.com/seu-usuario/mini_twitter.git
cd mini_twitter
cp .env.example .env

docker-compose up --build
```
Swagger: http://localhost:8000/swagger/


Contribuições são bem-vindas! Siga os passos abaixo:

1. Faça um fork do projeto.
2. Crie uma branch para sua feature:
    ```bash
    git checkout -b minha-feature
    ```
3. Commit suas alterações:
    ```bash
    git commit -m "Minha nova feature"
    ```
4. Envie para o repositório remoto:
    ```bash
    git push origin minha-feature
    ```
5. Abra um Pull Request.

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).