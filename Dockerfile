FROM python:3
ENV PYTHONUNBUFFERED 1
WORKDIR /web
COPY . .
RUN pip install -r requirements.txt
COPY start-dev.sh ./start-dev.sh
RUN chmod +x ./start-dev.sh