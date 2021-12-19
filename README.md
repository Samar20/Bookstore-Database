# Comp3005_Project

Project done by Indumini Jayakody and Samar Hussein for Carleton University COMP3005

# Getting Started

- First insert DDL.sql, DDLInserts.sql, Triggers.sql (To insert all tables and data information, materielized views and triggers) to a new database 'bookstore' in postgresql UI 

- Enter DB login info after inserting DDL using either line 15 or 16 in bookstore.py

```python
conn = psycopg2.connect(host="localhost", port = 8080, database="bookstore", user="postgres", password=90210) -- line 15
#conn = psycopg2.connect("dbname=bookstore user=postgres password=abcd123") -- line 16
```

## Installation

```bash
conda env create -f environment.yml
conda activate myenv
```





