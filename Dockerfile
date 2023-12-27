FROM python:3.13
ENV APP_HOME /app
WORKDIR $APP_HOME
COPY pages ./
RUN pip install --no-cache-dir -r requirements.txt
CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 main:server
