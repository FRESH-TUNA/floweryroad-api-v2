import os
import psycopg2
from psycopg2 import OperationalError

def execute_read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"The error '{e}' occurred")

def create_connection(db_name, db_user, db_password, db_host, db_port):
    connection = None
    try:
        connection = psycopg2.connect(
            database=db_name,
            user=db_user,
            password=db_password,
            host=db_host,
            port=db_port,
        )
        print("Connection to PostgreSQL DB successful")
    except OperationalError as e:
        print(f"The error '{e}' occurred")
    return connection

def migration(table_con, new_table_con, tables, new_tables):
    for i in range(len(tables)):
        datas = read_query(table_con, tables[i])
        insert_query(new_table_con, new_tables[i], datas)

# read datas form table
def read_query(connection, table_name):
    select_query = f"SELECT * from {table_name}"
    return execute_read_query(connection, select_query)

# read datas form table
def insert_query(connection, table_name, datas):
    if len(datas) != 0:
        records = ", ".join(["%s"] * len(datas))
        insert_query = (
            f"INSERT INTO {table_name} VALUES {records}"
        )
        connection.autocommit = True
        cursor = connection.cursor()
        cursor.execute(insert_query, datas)


# truncate some values
def slicing_users(connection, user_datas):
    return list(
        map(lambda x: tuple(x[0:7] + x[-1]), user_datas))
