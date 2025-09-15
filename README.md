# Pactum - Sistema de Gestão de Projetos e Contratos

Sistema web desenvolvido em Django para gestão completa de projetos e contratos.

## 🚀 Instalação Rápida com Docker

Estas são as instruções para rodar o projeto de forma rápida e fácil usando Docker.

### Pré-requisitos
- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/) (geralmente já vem com o Docker Desktop)

**Nota:** Use o comando `docker compose` (com espaço), que é a versão mais recente. Se você tiver uma versão mais antiga, pode precisar usar `docker-compose` (com hífen).

### 1. Inicie os Serviços

Com o Docker em execução na sua máquina, execute o seguinte comando na raiz do projeto:

```bash
docker compose up -d
```

Este comando irá construir as imagens Docker, baixar as dependências e iniciar os serviços da aplicação (`web`) e do banco de dados (`db`) em segundo plano.

### 2. Acesse a Aplicação

Após a conclusão do comando, a aplicação estará disponível no seu navegador no seguinte endereço:

- **URL:** [http://localhost:5001](http://localhost:5001)

### 3. Crie um Superusuário

Para acessar a área administrativa, você precisa de um superusuário. O comando a seguir cria um usuário `admin` com a senha `admin`:

```bash
docker compose exec -e DJANGO_SETTINGS_MODULE=Pactum.settings web python -c "import django; django.setup(); from django.contrib.auth import get_user_model; User = get_user_model(); u, created = User.objects.get_or_create(username='admin'); u.set_password('admin'); u.is_staff = True; u.is_superuser = True; u.save()"
```

**Login:**
- **Usuário:** `admin`
- **Senha:** `admin`

**IMPORTANTE:** Por segurança, altere a senha do usuário `admin` após o primeiro login.

### 4. Popule o Banco de Dados (Opcional)

Para preencher o banco de dados com dados de exemplo, execute o seguinte comando:

```bash
docker compose exec web python manage.py import_legacy_data
```

Este comando irá ler o arquivo `inserts_postgres.sql` e popular as tabelas de projetos, requisições e ordens. Veja mais detalhes na seção "Comandos Úteis".

## 🔧 Comandos Úteis

### `import_legacy_data`

Este comando foi criado para popular o banco de dados com os dados do arquivo `inserts_postgres.sql`. O que ele faz:

1.  **Limpa as tabelas:** Apaga todos os dados existentes nas tabelas `Ordem`, `Requisicao` e `Projeto` para evitar duplicatas.
2.  **Lê o arquivo SQL:** Analisa o arquivo `inserts_postgres.sql`.
3.  **Importa os dados:** Insere os dados de projetos, requisições e ordens no banco de dados usando o ORM do Django, garantindo a compatibilidade com os modelos.

##  troubleshooting

### Erro de "Porta em Uso" (Port is already allocated)

Durante a execução do `docker compose up`, você pode encontrar um erro indicando que a porta `5001` ou `5434` já está em uso. Isso acontece se outro serviço na sua máquina estiver usando essas portas.

**Solução:**

1.  Abra o arquivo `docker-compose.yml`.
2.  Procure pela seção `ports` do serviço que está causando o conflito (`web` ou `db`).
3.  Altere o primeiro número (a porta do seu computador) para uma porta que esteja livre.

**Exemplo para o serviço `web` (se a porta 5001 estiver ocupada):**

Altere de:
```yaml
ports:
  - "5001:5000"
```
Para:
```yaml
ports:
  - "5002:5000" # Ou qualquer outra porta livre
```

**Exemplo para o serviço `db` (se a porta 5434 estiver ocupada):**

Altere de:
```yaml
ports:
  - "5434:5432"
```
Para:
```yaml
ports:
  - "5435:5432" # Ou qualquer outra porta livre
```

4. Salve o arquivo e execute `docker compose up -d` novamente.