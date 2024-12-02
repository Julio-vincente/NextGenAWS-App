FROM python:3.11-slim

WORKDIR /app

COPY app/requirements.txt requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

COPY app/ .

EXPOSE 80

ENV FLASK_APP=app:app
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=80

CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:80", "app:app"]