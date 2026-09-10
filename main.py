import os
from dotenv import load_dotenv
name = "Zohaib"

user = {
    "name": "Zohaib",
    "age": 33
}

print(f"Hello, {user['name']}!")
print(f"age, {user['age']}!")
print("Welcome to Python for AI")


load_dotenv()

api_key = os.getenv("API_KEY")
app_name = os.getenv("APP_NAME")

print(app_name)
print(api_key)

if not api_key:
    print("Key not found")
else:
    print(f"API key: {api_key}")