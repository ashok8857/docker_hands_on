# Dockerfile
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY api_fetcher.py .

CMD ["python", "api_fetcher.py"]
