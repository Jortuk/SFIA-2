#!/bin/bash
. ~/.bashrc
env SFIA2_DB_URI="${SFIA2_DB_URI}" 
env SECRET_KEY="${SECRET_KEY}"
docker-compose build
docker push jortuk/service_1:latest
docker push jortuk/service_2:latest
docker push jortuk/service_3:latest
docker push jortuk/service_4:latest
docker stack deploy -c docker-compose.yaml sfia2