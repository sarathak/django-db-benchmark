#!/bin/bash
set -e
CONF=docker/mariadb/docker-compose.yml
docker-compose -p ddbench -f $CONF run django
docker-compose -p ddbench -f $CONF down
CONF=docker/mysql/docker-compose.yml
docker-compose -p ddbench -f $CONF run django
docker-compose -p ddbench -f $CONF down
CONF=docker/postgres/docker-compose.yml
docker-compose -p ddbench -f $CONF run django
docker-compose -p ddbench -f $CONF down
python create_graph.py