FROM python:3.11-slim

WORKDIR /app

COPY pyproject.toml /app/
RUN pip install --no-cache-dir pydantic pytest && pip install -e .

COPY . /app

CMD ["python", "-m", "src.agent_framework.cli", "demo"]
