
# Exercise 1
def greet():
    print("Hello Zohaib")


greet()

# Excercise 2
def greet(name):
    print(f"Hello {name}")

greet("Zohaib")

# Excersise 3

def add(a, b):
    return a + b

print(add(10, 20))

#  exercise 4 

def greet(name, message="Hello"):
    print(f"{message}, {name}")

greet("Umer")
greet("Umer", "Good morning")

# exercise 5

def check_price(price):
    if price > 100:
        return "Expensive"
    else:
        return "Good price"

print(check_price(110))
print(check_price(80))


# exercise 6

products = [
    {
        "name": "watch",
        "price": 99
    },
    {
        "name": "ring",
        "price": 149
    },
    {
        "name": "necklace",
        "price": 199
    }
]

def show_product(product):
    product_type = check_price(product['price'])
    return f"{product['name'].title()}, price: {product['price']} - {product_type}"


for product in products:
    print(show_product(product))



# python bonus 

prices = [50, 100, 150, 200]

# normal
expensive_prices = []

for price in prices:
    if price > 100:
        expensive_prices.append(price)

print(expensive_prices)

# Python also allows:

expensive_prices = [price for price in prices if price > 100]

print(expensive_prices)


# Day 2 challenge

# products
#     ↓
# show_product()
#     ↓
# check_price()
#     ↓
# formatted output


# Watch - $99 - Good price
# Ring - $149 - Expensive
# Necklace - $199 - Expensive


products = [
    {
        "name": "watch",
        "price": 99
    },
    {
        "name": "ring",
        "price": 149
    },
    {
        "name": "necklace",
        "price": 199
    }
]

for product in products:
    print(show_product(product))