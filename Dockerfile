FROM alpine:latest

RUN apk add --no-cache --update python3 py3-pip bash
ADD requirements.txt /tmp/requirements.txt
RUN pip3 install --no-cache-dir -q -r /tmp/requirements.txt


ADD . /webapp
WORKDIR /webapp

ENV FLASK_APP todo
ENV FLASK_ENV development
ENV FLASK_RUN_HOST 0.0.0.0

EXPOSE 5000
CMD ["flask", "run"]