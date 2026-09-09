# Modules
# from day3 import Product
import math
import random
from calculator import add, multiply
from product_utils import check_price, format_product

import requests



# watch = Product("Watch", 99, 'xxxx')

# print(watch.display())

# print(math.sqrt(25))

number = random.randint(1, 10)

# print(number)

# print(requests.__version__)


print(add(10, 20))
print(multiply(5, 10))

print(check_price(120));
print(check_price(90));
print(format_product("watch", 120));
print(format_product("Ring", 90));
