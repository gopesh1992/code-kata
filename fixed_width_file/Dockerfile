FROM python:3.9-slim

WORKDIR /app

COPY spec.json .
COPY fixed_width_file_generator.py .
COPY fixed_width_file_parser.py .

RUN pip install -r requirements.txt

CMD ["python", "fixed_width_file_parser.py"]
