print("Exercise 1")

name ="Zohaib"; age=33; job="web developer"; yearsOfExperience = 8;
message = f"My name is {name}. I am a {job} with {yearsOfExperience} years of experience."

print(message)


print("------------------------------------");
print("Exercise 2")

skilles = ["php","javascript","reactjs","nodeJs"]

skilles.append("python")
print(skilles)

print("------------------------------------");
print("Exercise 3")

product = {
    "name": "watch",
    "price": 30,
    "sku": "xxx",
    "instock": "Yes",
}

for key, value in product.items():
    message = f"{key}: {value}"
    print(message)


print("------------------------------------");
print("Exercise 4")
products = [
    {
        "name": "watch",
        "price": 99,
        "sku": "xxx",
        "instock": "Yes",
    },
    {
        "name": "Ring ",
        "price": 149,
        "sku": "xxx",
        "instock": "Yes",
    },
    {
        "name": "Necklace ",
        "price": 199,
        "sku": "xxx",
        "instock": "Yes",
    }
]

for product in products:
    message = f"{product['name']} - ${product['price']}" 
    print(message);
    if product['price'] > 100:
        print("Expensive")
    else:
        print("Good price")
