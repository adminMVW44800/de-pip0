FROM python:3.9-slim

WORKDIR /app

COPY . .

RUN pip install pandas

CMD ["python", "scripts/process.py"]