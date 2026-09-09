from day2 import add
import math
class Product:
    def __init__(self, name, price, sku):
        self.name = name
        self.price = price
        self.sku = sku

    def display(self):
        return f"{self.name} - ${self.price}"

    def check_price(self):
        if self.price > 100:
            return "Expensive"
        else:
            return "Good price"


product = Product("Watch", 99, 'xxx')

# print(product.name)
# print(product.price)

watch = Product("Watch", 99, 'xxxx')

print(watch.display())
print(watch.check_price())

# Excercise

class Student:
    def __init__(self, name, age, course):
        self.name = name
        self.age= age
        self.course = course
    def introduce(self):
        return f"My name is {self.name}. I am {self.age} years old and studying {self.course}."


student = Student("zohaib", "33", "Python for AI")

# print(student.name.title())
# print(student.age)
# print(student.course)

# Exercise 2 — Student method

print(student.introduce())


# Exercise 5 — AI-style class

class AIMessage:
    def __init__(self, role, content):
        self.role = role
        self.content = content
    def display(self):
        return f"{self.role}: {self.content}"

message = AIMessage(
    "user",
    "Explain what an API is"
)
print(message.display())
message = AIMessage(
    "assistant",
    "An API allows applications to communicate with each other."
)

print(message.display())

print(add(20,22))
print(math.sqrt(25))