from fastapi import FastAPI
from DAOStock import get_all_stock_price

app = FastAPI()

@app.get("/")
def get_all_stock_values():
    return get_all_stock_price()
