FROM ubuntu:16.04
RUN apt-get update \
    && apt-get install -yq --no-install-recommends \
    python3-dev \
    python3-pip

ADD . /app
WORKDIR /app

EXPOSE 8081

RUN pip3 install --upgrade pip
RUN pip3 install setuptools
RUN pip3 install -r requirements.txt

CMD python3 app.py