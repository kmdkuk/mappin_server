FROM ubuntu:latest

ENV APP_ROOT /usr/src/mappin_server

WORKDIR $APP_ROOT


RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential
COPY . $APP_ROOT
RUN pip install -r requirements.txt
# ENTRYPOINT ["python"]
# CMD ["app.py"]
