import json
from utillity import get_db_file

db_file = get_db_file()

def get_all_stock_price():
    with open(db_file, 'r') as stock_data:
        all_stock_data = json.load(stock_data)
    return all_stock_data

def get_stock_price_by_time(time_ymdhms: int):
    with open(db_file, 'r') as stock_data:
        all_stock_data = json.load(stock_data)
    return all_stock_data[time_ymdhms]

if __name__ == '__main__':
    # print(get_all_stock_price())
    # print(get_stock_price_by_time('20250724163340'))
    pass
