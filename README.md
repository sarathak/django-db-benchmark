# Comparing Database performance with Django ORM

- Postgresql 
- MySQL
- MariaDB
- SQLite

Comparing database operation performance using django ORM.

PostgreSQL vs MySQL vs MariaDB vs SQLite



## Insert performance comparison 
Tested 1000 row insert in all databases and calculated time is taken.

![Insert](media/graphs/insert.png)

## Bulk Insert performance comparison 
Tested 1000 row bulk insert in all databases and calculated time is taken.

![Insert](media/graphs/bulk_insert.png)

## Bulk Delete performance comparison 
Tested 1000 row delete in all databases and calculated time is taken.

![Insert](media/graphs/delete.png)

## Bulk Delete performance comparison 
Tested 1000 row bulk delete in all databases and calculated time is taken.

![Insert](media/graphs/bulk_delete.png)

## Update performance comparison 
Tested 1000 row update in all databases and calculated time is taken.

![Insert](media/graphs/update.png)


## Bulk update performance comparison 
Tested 1000 row bulk update in all databases and calculated time is taken.

![Insert](media/graphs/bulk_update.png)



## Select performance comparison 
Tested 1000 in 1000 rows select operation in non indexed column in all databases and calculated time is taken.

![Insert](media/graphs/select.png)


## Select index performance comparison 
Tested 1000 in 1000 rows select operation in indexed column in all databases and calculated time is taken.

![Insert](media/graphs/select_index.png)

## Installation 

- install [docker](https://docs.docker.com/engine/install/) and [docker compose](https://docs.docker.com/compose/install/) 
- clone repository
- run ./start.sh
- result will be stored in reports/graph

