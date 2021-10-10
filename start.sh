#!/usr/bin/env bash
cd docker/mysql
docker-compose run django
docker-compose down
cd ../../
#cd docker/postgresql
#docker-compose run django
#docker-compose down
