#!/bin/bash
. ~/.bashrc
env SFIA2_DB_URI="${SFIA2_DB_URI}" 
env SECRET_KEY="${SECRET_KEY}"
docker stack deploy -c docker-compose.yaml sfia2