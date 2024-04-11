FROM python:3.11.9-slim

WORKDIR /usr/src/app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "./weather_api_wrapper.py"]
