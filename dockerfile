FROM python:3.7-slim-buster

WORKDIR /flaskapp

COPY requirements.txt . 
COPY app.py . 

RUN apt-get update -y && \
    pip3 install -r requirements.txt 

EXPOSE 8080 

CMD ["gunicorn", "-b", "0.0.0.0:8000", "app:app"]
