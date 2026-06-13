FROM python:3.11-slim

WORKDIR /app

RUN apt-get update && apt-get install -y curl wget unzip gnupg && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

RUN pip install --no-cache-dir torch==2.3.0+cpu --index-url https://download.pytorch.org/whl/cpu
RUN grep -v '^torch==' requirements.txt > /tmp/requirements-no-torch.txt && pip install --no-cache-dir -r /tmp/requirements-no-torch.txt

COPY app.py .
COPY templates ./templates
COPY tests ./tests

RUN mkdir -p /app/logs

EXPOSE 5000

CMD ["python", "app.py"]
