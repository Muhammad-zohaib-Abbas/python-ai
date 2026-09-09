def check_price(price):
    if price > 100:
        return "Expensive"
    else:
        return "good price"


def format_product(name, price):
    return f"{name} - {price}"
