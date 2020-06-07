FROM python:latest
RUN mkdir /opt/SFIA2/
COPY . /opt/SFIA2/
WORKDIR /opt/SFIA2/
RUN apt-get update -y
RUN apt-get install python3-venv -y
RUN python3 -m venv venv
RUN . venv/bin/activate
RUN pip3 install -r requirements.txt
ENTRYPOINT ["python3", "app.py"]
