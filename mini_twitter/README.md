# Mini Twitter

Este é um projeto simples que simula funcionalidades básicas de uma rede social como o Twitter.

## Estrutura do Projeto

```
mini-twitter/
├── .github/workflows/       # CI/CD workflows (GitHub Actions)
├── apps/                     # Main application code
│   ├── accounts/            # User authentication app
│   ├── posts/               # Posts functionality
│   ├── feeds/               # Feed generation
│   ├── core/                # Core configurations
│   └── utils/               # Utility functions
├── docker/                  # Docker configurations
├── docs/                    # API documentation
├── scripts/                 # Utility scripts
├── tests/                   # Test cases
├── docker-compose.yml       # Docker compose file
├── Dockerfile               # Dockerfile
├── requirements.txt         # Python dependencies
└── README.md                # Project documentation
```

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

### Diretórios

- **src/controllers/**: Contém os controladores responsáveis por gerenciar as requisições e respostas.
- **src/models/**: Contém os modelos de dados da aplicação.
- **src/routes/**: Define as rotas da aplicação.
- **src/services/**: Contém a lógica de negócios e serviços auxiliares.
- **src/utils/**: Funções utilitárias reutilizáveis.
- **tests/**: Testes automatizados para a aplicação.
- **public/**: Arquivos estáticos como imagens, CSS e JavaScript.
- **views/**: Templates de visualização para renderização no lado do servidor.

## Tecnologias Utilizadas

- Django
- Python
- PostgreSQL
- Docker
- Docker-Compose

## Como Executar

1. Clone o repositório:
    ```bash
    git clone https://github.com/seu-usuario/mini_twitter.git
    ```
2. Instale as dependências:
    ```bash
    cd mini_twitter
    npm install
    ```
3. Configure as variáveis de ambiente no arquivo `.env`.
4. Inicie o servidor:
    ```bash
    npm start
    ```
5. Acesse a aplicação em `http://localhost:3000`.

## Funcionalidades

- Cadastro e login de usuários.
- Publicação de tweets.
- Curtidas e comentários em tweets.
- Seguir e deixar de seguir outros usuários.

## Testes

Para rodar os testes, utilize o comando:
```bash
npm test
```

## Contribuição

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