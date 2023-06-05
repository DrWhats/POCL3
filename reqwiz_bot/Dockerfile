FROM python:3.9-slim

WORKDIR /reqwiz_bot

RUN apt-get update -y && \
    apt-get install -y --no-install-recommends build-essential python3-dev libffi-dev libssl-dev && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

COPY req.txt req.txt

RUN pip install --no-cache-dir -r req.txt

COPY . .

CMD ["python", "reqwiz.py"]