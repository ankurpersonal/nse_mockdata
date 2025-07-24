import time
import random
from datetime import datetime
import json
from utillity import get_db_file

class StockPrice:

    def generate_stock_price(self):
        db_file = get_db_file()
        while(True):
            stock_data = dict()
            new_stock_price = {int(datetime.now().strftime('%Y%m%d%H%M%S')): random.randint(1, 100)}
            with open(db_file, 'r') as stock_db_file:
                price_list = stock_db_file.read().strip()
                if price_list:
                    stock_data = json.loads(price_list)
            
            stock_data.update(new_stock_price)

            with open(db_file, 'w') as stock_db_file:
                json.dump(stock_data, stock_db_file, indent=4)
            time.sleep(2)

if __name__ == '__main__':
    stock = StockPrice()
    stock.generate_stock_price()
