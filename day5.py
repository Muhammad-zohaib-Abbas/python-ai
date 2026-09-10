import json
import requests
import asyncio
product = {
    "name": "Watch",
    "price": 99,
    "in_stock": True
}

# product_json = '{"name": "Watch", "price": 99, "in_stock": True}'
product_json = '{"name": "Watch", "price": 99, "in_stock": true}'

json_data = json.dumps(product)

# print("From pythond dictionary to json")
# print(json_data)

# print("From josn to python dictionary")
# print(json.loads(product_json))



response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
print(response.status_code)
data = response.json()
print(data['body'])


data = {
    "title": "My Product",
    "body": "This is my product",
    "userId": 1
}

# response = requests.post(
#     "https://jsonplaceholder.typicode.com/posts",
#     json=data
# )

# print(response.status_code)
# print(response.json())




# 404 test / requests.RequestException
try:
    response = requests.get(
        "https://jsonplaceholder.typicode.com/invalid"
    )

    response.raise_for_status()

    data = response.json()

    print(data)
except requests.RequestException as error:
    print(f"Request failed: {error}")



# Error heandling 

try:
    number = int("hello")
except ValueError:
    print("That is not a valid number")

async def hello():
    print("Hello")

    await asyncio.sleep(2)

    print("World")


asyncio.run(hello())
# hello()

# exercise 1

user = {
    "name": "Zohaib",
    "age": 33,
    "skills": ["PHP", "JavaScript", "Python"]
}
# convert to json
user =json.dumps(user)
print(user);

# covert back to python dictionary
user = json.loads(user);
print(user);


# Exercise 2 — get

response = requests.get("https://jsonplaceholder.typicode.com/users/1");
# print(response.json()['address']['street'])
print(response.json()['address']['street'])


# Exercise 3 — get
product = {
    "name": "Watch",
    "price": 99,
    "in_stock": True
}


try:
    response = requests.post("https://jsonplaceholder.typicode.com/posts", json=product)
    print(response.json())
except requests.RequestException  as error:
    print(error)



# Exercise 4 — Error handling

try:
    response = requests.get("https://jsonplaceholder.typicode.com/invalid-url")
    response.raise_for_status()
    print(response.json())
except requests.RequestException  as error:
    error = f"Request field: {error}"
    print(error)


# Exercise 4 — Async
async def task(name, seconds):
    print(f"{name} started")
    await asyncio.sleep(seconds)
    print(f"{name} finished")

asyncio.run(task("Task1", 2))

