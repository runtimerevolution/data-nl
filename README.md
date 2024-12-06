# Data-NL

## Setup

1. Install and sync `uv`, available at https://github.com/astral-sh/uv

```bash
uv sync
```

2. Create a copy of .env.sample and fill in the gaps

```bash
cp .env.sample .env.local
```

3. Run the command below and navigate to "http://localhost"

```bash
 docker compose up -d --build
```
