# Django ORM Database Performance Benchmark

This project benchmarks and compares the performance of popular SQL databases using the Django ORM. It provides detailed metrics for common database operations across different database backends.

**Databases tested:**
- PostgreSQL
- MySQL
- MariaDB
- SQLite
- CockroachDB

## Overview

Measure and compare the speed of database operations (insert, bulk insert, delete, bulk delete, update, bulk update, select, and indexed select) using Django ORM on AWS T2 micro instances. Results include execution time and performance graphs for each operation and database.

## Benchmark Results

### Insert Performance Comparison
Tested 1000 row inserts in all databases and measured execution time.

![Insert](media/graphs/insert.png)

### Bulk Insert Performance Comparison
Tested 1000 row bulk inserts in all databases and measured execution time.

![Bulk Insert](media/graphs/bulk_insert.png)

### Delete Performance Comparison
Tested 1000 row deletes in all databases and measured execution time.

![Delete](media/graphs/delete.png)

### Bulk Delete Performance Comparison
Tested 1000 row bulk deletes in all databases and measured execution time.

![Bulk Delete](media/graphs/bulk_delete.png)

### Update Performance Comparison
Tested 1000 row updates in all databases and measured execution time.

![Update](media/graphs/update.png)

### Bulk Update Performance Comparison
Tested 1000 row bulk updates in all databases and measured execution time.

![Bulk Update](media/graphs/bulk_update.png)

### Select Performance Comparison (Non-Indexed Column)
Tested 1000 select queries on non-indexed columns in all databases and measured execution time.

![Select](media/graphs/select.png)

### Select Performance Comparison (Indexed Column)
Tested 1000 select queries on indexed columns in all databases and measured execution time.

![Select Index](media/graphs/select_index.png)

## How to Run the Benchmark

1. Install [Docker](https://docs.docker.com/engine/install/) and [Docker Compose](https://docs.docker.com/compose/install/).
2. Clone this repository:
   ```sh
   git clone https://github.com/yourusername/django-db-benchmark.git
   cd django-db-benchmark
   ```
3. Start the benchmark:
   ```sh
   ./start.sh
   ```
4. View the results in the `reports/graph` directory.

## Keywords

Django ORM, database benchmark, SQL performance, PostgreSQL, MySQL, MariaDB, SQLite, CockroachDB, database comparison, bulk insert, bulk update, bulk delete, select performance, indexed query, AWS T2 micro, Docker, Python, open source.

