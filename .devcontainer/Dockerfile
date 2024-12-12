# See here for image contents: https://github.com/microsoft/vscode-dev-containers/tree/v0.192.0/containers/python-3/.devcontainer/base.Dockerfile

# [Choice] Python version: 3, 3.9, 3.8, 3.7, 3.6
ARG PYTHON_VERSION
FROM mcr.microsoft.com/vscode/devcontainers/python:1-${PYTHON_VERSION}

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

WORKDIR /workspace

COPY . /workspace

RUN uv sync

