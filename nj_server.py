from tkinter import UNITS
from fastapi import FastAPI

app = FastAPI (title = "New Jersey API Server")


catalog = {
    "tomatoes":{
        "units": "boxes",
        "qty": 1000
    },
    "wine":{
        "units": "bottles",
        "qty": 500
    }
}    
@app.get("/warehouse/{product}")
async def load_truck(product, order_qty):
    print("Loading truck with product: ", product,"and order quantity: ", order_qty)
    return{
        "product": product,
        "order_qty": order_qty,
        "units": catalog[product]["units"]
    }


