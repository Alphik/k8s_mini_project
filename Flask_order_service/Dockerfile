FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .

RUN pip3 install -r requirements.txt

COPY . .

EXPOSE 5003

CMD ["python3", "order_srvice.py"]
