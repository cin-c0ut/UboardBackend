FROM python:3.10.12

RUN mkdir /app
RUN mkdir /init

# WORKDIR /app

RUN apt update
RUN apt-get install -y netcat-traditional

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN pip install --upgrade pip

COPY requirements.txt /init/

RUN pip install --no-cache-dir -r /init/requirements.txt

EXPOSE 8000

WORKDIR /app

RUN apt-get install -y libgl1

ENTRYPOINT ["sh", "entrypoint.sh"]
