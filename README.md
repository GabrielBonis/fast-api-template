Modelo inicial completo para construção de APIs com FastAPI.

## Índice

- [🔧 Visão Geral](#-visão-geral)  
- [🚀 Tecnologias](#-tecnologias)  
- [⚙️ Instalação e Execução](#️-instalação-e-execução)  
- [🛠 Estrutura do Projeto](#-estrutura-do-projeto)  
- [📦 Configuração](#-configuração)  
- [🔐 Autenticação](#-autenticação)  
- [🧪 Testes e Qualidade](#-testes-e-qualidade)  
- [📈 Sugestões de melhorias](#-sugestões-de-melhorias)  

## 🔧 Visão Geral
Este projeto serve como ponto de partida para criar APIs REST escaláveis com FastAPI, integrado ao SQLModel (ou SQLAlchemy), Docker, testes com Pytest, migrações com Alembic e CI/CD via GitHub Actions.

## 🚀 Tecnologias
- **FastAPI** – framework principal
- **SQLModel** – ORM para Camada de banco de dados
- **PostgreSQL** – base de dados relacional
- **Docker & Docker Compose** – conteinerização
- **Alembic** – migrações de banco
- **Pytest** – testes automatizados
- **GitHub Actions** – integração contínua (CI)

## ⚙️ Instalação e Execução

1. Clone o repositório:
   ```bash
   git clone https://github.com/GabrielBonis/fast-api-template.git
   cd fast-api-template
   ```
2. Configure variáveis de ambiente (ex: `.env.example → .env`):
   ```env
   SECRET_KEY=...
   DATABASE_URL=postgresql://user:pass@db/fastapi
   ```
3. Execute com Docker:
   ```bash
   docker-compose up --build
   ```
4. Abra a documentação interativa:
   ```
   http://localhost:8000/docs
   ```

## 🛠 Estrutura do Projeto
```text
backend/
├── app/
│   ├── api/              # endpoints FastAPI
│   ├── crud.py           # funções CRUD
│   ├── models.py         # modelos SQLModel
│   ├── schemas.py        # Pydantic schemas
│   └── tests/            # testes unitários
├── alembic/              # migrações do banco
├── Dockerfile
└── pyproject.toml        # (ou requirements.txt)
```

## 📦 Configuração
Edite `.env` para personalizar:
- `SECRET_KEY`
- `DATABASE_URL`
- `FIRST_SUPERUSER_*` (usuário admin inicial)
- Outras variáveis específicas do ambiente e infraestrutura

## 🔐 Autenticação
- JWT-based auth (rotas de login, criação, refresh)
- Recuperação de senha por email
- Proteção de rotas através de dependências FastAPI

## 🧪 Testes e Qualidade
- **Pytest** com coverage
- Scripts em `scripts/` para execução de testes
- Configuração inicial de CI no GitHub Actions
- Migrações automáticas via Alembic