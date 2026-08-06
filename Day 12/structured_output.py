from pydantic import BaseModel, ValidationError
import json

# ----------------------------
# Pydantic Schema
# ----------------------------

class Product(BaseModel):
    name: str
    category: str
    price: float
    in_stock: bool


# ----------------------------
# Simulated AI Output
# ----------------------------

def ask_model(text):

    outputs = {

        "1": '{"name":"Laptop","category":"Electronics","price":850.5,"in_stock":true}',

        "2": '{"name":"Notebook","category":"Stationery","price":5.99,"in_stock":true}',

        "3": '{"name":"Headphones","category":"Electronics","price":49.99,"in_stock":false}',

        "4": '{"name":"Chair","category":"Furniture","price":"abc","in_stock":true}',

        "5": '{"name":"Bottle","category":"Kitchen","in_stock":true}'

    }

    return outputs[text]


# ----------------------------
# Validation + Retry
# ----------------------------

def extract(text, retries=2):

    for attempt in range(retries):

        try:

            raw = ask_model(text)

            data = json.loads(raw)

            product = Product(**data)

            return product

        except (ValidationError, json.JSONDecodeError):

            print("Retrying...")

    return None


tests = ["1","2","3","4","5"]

print("="*50)

for t in tests:

    result = extract(t)

    print("Input:",t)

    print(result)

    print("-"*50)