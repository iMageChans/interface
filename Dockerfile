FROM python:3.12.1

WORKDIR /app

COPY . /app

COPY entrypoint.sh /entrypoint.sh

RUN chmod +x /entrypoint.sh

RUN apt-get update && apt-get install -y netcat-openbsd

RUN python -m pip install --upgrade pip

RUN pip install -r requirements.txt

ENV PYTHONUNBUFFERED 1

EXPOSE 8000

ENTRYPOINT ["/entrypoint.sh"]

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
