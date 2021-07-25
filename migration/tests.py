from data import *
from migration import *


def read_tests():
    datas = read_query(table_con, "public.core_flower")
    print(len(datas))
    print(datas)

def write_tests():
    datas = read_query(table_con, "public.core_flower")
    print(len(datas))
    print(datas)

if __name__ == "__main__":
    table_con = create_connection(**db_data)
    
