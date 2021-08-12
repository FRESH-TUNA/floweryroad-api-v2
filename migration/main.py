from data import *
from migration import *

if __name__ == "__main__":
    table_con = create_connection(**db_data)
    new_table_con = create_connection(**new_db_data)
    migration(table_con, new_table_con, old_data_tables, new_data_tables)
