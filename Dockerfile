FROM python:3.11-slim

# Copy local code to the container image
COPY . /app

# Sets the working directory
WORKDIR /app

# Upgrade PIP
RUN pip install --upgrade pip
RUN pip freeze > requirements.txt
#Install python libraries from requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Run the web service on container startup
CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 main:app
