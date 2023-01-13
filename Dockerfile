# Use the official Python image.
# https://hub.docker.com/_/python
FROM python:3.7

COPY requirements.txt requirements.txt

RUN apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y gconf-service \
    libasound2 libatk1.0-0 libcairo2 libcups2 libfontconfig1 \
    libgdk-pixbuf2.0-0 libgtk-3-0 libnspr4 libpango-1.0-0 libxss1 \
    fonts-liberation libnss3 lsb-release xdg-utils libappindicator1 \
    chromium chromium-driver && \
    pip install -r requirements.txt

# Copy local code to the container image.
ENV APP_HOME /app
WORKDIR $APP_HOME
COPY . .

# Run the web service on container startup. Here we use the gunicorn
# webserver, with one worker process and 8 threads.
# For environments with multiple CPU cores, increase the number of workers
# to be equal to the cores available.
CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 main:app
