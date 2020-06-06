FROM python:latest
WORKDIR /service2
COPY . /service2/
RUN apt-get update -y && apt-get install python3-venv -y
RUN python3 -m venv venv && . venv/bin/activate
RUN pip3 install -r requirements.txt
ENTRYPOINT ["/usr/local/bin/python3", "app.py"]