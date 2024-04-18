FROM python:3.11.9-slim

WORKDIR /usr/src/app

COPY requirements.txt .

COPY ./TP3/api/app.py .

EXPOSE 8081

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "./app.py"]
