# Comp3005_Project

Project done by Indumini Jayakody and Samar Hussein for Carleton University COMP3005

# Getting Started

- First insert DDL.sql, DDLInserts.sql, Triggers.sql (To insert all tables and data information, materielized views and triggers) to a new database 'bookstore' in postgresql UI 

- Enter DB login info after inserting DDL using with your postgres username and password in line 16 of bookstore.py

```python
conn = psycopg2.connect("dbname=bookstore user=postgres password=abcd123") -- line 16
```

## Installation

```bash
conda env create -f environment.yml
conda activate myenv
```

## To run

```bash
python3 bookstore.py
```



