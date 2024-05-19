FROM alpine

COPY requirements.txt /requirements.txt
RUN apk add python3 py3-pip bash && python -m venv venv && source venv/bin/activate && pip3 install -r /requirements.txt
COPY ./src /src
RUN chmod +x /src/entrypoint.sh
ENTRYPOINT bash /src/entrypoint.sh
