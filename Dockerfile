FROM python:3.12-slim
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# direct all output to the terminal
ENV PYTHONUNBUFFERED=1
# prevents python creating .pyc files
ENV PYTHONDONTWRITEBYTECODE=1

# Set the working directory
WORKDIR /app

# Install dependencies
COPY pyproject.toml .
RUN uv sync

# Copy src
COPY ./src src
# Copy entrypoint
COPY main.py .

EXPOSE 80

CMD ["uv", "run", "fastapi", "run", "main.py", "--port", "80"]