FROM python:3.11-slim

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN pip install --no-cache-dir fastapi uvicorn pydantic email-validator

COPY . .

EXPOSE 8000

CMD ["python", "src/entrypoint.py"]