# Data-NL

## Setup

### 1. Install and sync `uv`, available at [https://github.com/astral-sh/uv](https://github.com/astral-sh/uv)

```bash
uv sync
```

### 2. Create a copy of `.env.sample` and fill in the gaps

```bash
cp .env.sample .env.local
```

After copying the `.env.sample` to `.env.local`, you'll need 
to fill in the necessary environment variables. Below is a table explaining each variable:

| **Variable Name**      | **Description**                                                      |
|------------------------|----------------------------------------------------------------------|
| `API_TITLE`            | The title of your API project.                                       |
| `OPENAI_API_KEY`       | Your OpenAI API key for accessing OpenAI services.                   |
| `DATABASE_INIT_FILE`   | The database initialization file to use (`*.tar` or `*.sql`).        |
| `POSTGRES_USER`        | The username for the PostgreSQL database.                            |
| `POSTGRES_PASSWORD`    | The password for the PostgreSQL database.                            |
| `DB_HOST`              | The hostname for the PostgreSQL database.                            |
| `DB_PORT`              | The port on which PostgreSQL listens inside the Docker container.    |
| `POSTGRES_DB`          | The name of the PostgreSQL database.                                 |

### 3. Run the command below and navigate to [http://localhost](http://localhost)

```bash
docker compose --env-file .env.local up -d --build
```
