FROM python:3.7-stretch
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .