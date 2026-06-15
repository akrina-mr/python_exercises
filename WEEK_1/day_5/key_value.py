# Iterate through the following dictionary and print each key and value

product = {
    "name": "laptop",
    "price": 1500,
    "stock": 10,
}

for key, value in product.items():
    print(f"{key}: {value}")