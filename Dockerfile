FROM python:latest

WORKDIR /FLASK_API

COPY .requirements.txt /FLASK_API
RUN pip install --no-cache-dir --upfrade -r requirements.txt

COPY . /FLASK_API

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]