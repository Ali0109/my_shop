FROM python:3
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /my_shop
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
