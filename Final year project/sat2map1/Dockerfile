FROM python:3

ENV PYTHONBUFFERED 1
ENV PYTHONWARNINGS="ignore:Unverified HTTPS request"

RUN mkdir /GAN-django

WORKDIR /GAN-django

COPY . /GAN-django

RUN pip install --upgrade pip

RUN pip install -r req.txt

RUN python manage.py makemigrations
RUN python manage.py migrate


