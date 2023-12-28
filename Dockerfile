FROM python:3.11-slim
ENV APP_HOME /app
WORKDIR $APP_HOME
COPY pages ./
RUN pip freeze > requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 8080
CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 app:server
