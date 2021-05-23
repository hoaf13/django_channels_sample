FROM python:3.8

ADD . /code
WORKDIR  /code

RUN apt-get update
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 5000
CMD ["python3","manage.py","runserver","0.0.0.0:5000"]

