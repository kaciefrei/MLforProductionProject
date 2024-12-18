FROM python:3.9-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    libatlas-base-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

COPY . /app

RUN pip install numpy==1.23.5

RUN pip install --no-cache-dir -r requirements.txt

RUN pip install --no-cache-dir tflite-runtime==2.7.0

EXPOSE 5000

CMD ["python", "app.py"]
