FROM python:latest

WORKDIR /FLASK_API

COPY ./requirements.txt /FLASK_API
RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY . /FLASK_API

CMD ["python3", "rest_api.py"]