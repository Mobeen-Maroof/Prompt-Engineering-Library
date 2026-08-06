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
# Stage 1: Extract
# ----------------------------

def extract(record):

    return record


# ----------------------------
# Stage 2: Self Critique
# ----------------------------

def critique(data):

    errors=[]

    if "price" not in data:

        errors.append("Missing price.")

    elif not isinstance(data["price"],(int,float)):

        errors.append("Price must be numeric.")

    return errors


# ----------------------------
# Stage 3: Correct
# ----------------------------

def correct(data,errors):

    if "Missing price." in errors:

        data["price"]=0

    if "Price must be numeric." in errors:

        data["price"]=0

    return data


# ----------------------------
# Stage 4: Validate
# ----------------------------

def validate(data):

    try:

        product=Product(**data)

        return product

    except ValidationError as e:

        return e


# ----------------------------
# Test Data
# ----------------------------

documents=[

{"name":"Laptop","category":"Electronics","price":850.5,"in_stock":True},

{"name":"Notebook","category":"Stationery","price":5.99,"in_stock":True},

{"name":"Headphones","category":"Electronics","price":49.99,"in_stock":False},

{"name":"Chair","category":"Furniture","price":"ABC","in_stock":True},

{"name":"Bottle","category":"Kitchen","in_stock":True},

{"name":"Mouse","category":"Electronics","price":20.99,"in_stock":True},

{"name":"Keyboard","category":"Electronics","price":35.5,"in_stock":False}

]

print("="*60)

for doc in documents:

    extracted=extract(doc)

    issues=critique(extracted)

    corrected=correct(extracted,issues)

    result=validate(corrected)

    print(result)

    print("-"*60)