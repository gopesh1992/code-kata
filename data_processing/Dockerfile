FROM python:3.9-slim

WORKDIR /app

COPY generate_csv_data.py .
COPY data.csv .
COPY data_processing.py .
COPY requirements.txt .

RUN pip install -r requirements.txt

CMD ["python", "data_processing.py"]
