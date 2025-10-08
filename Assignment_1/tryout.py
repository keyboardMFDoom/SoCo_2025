def square_perimeter(thing):
    return 4 * thing["side"]

def square_area(thing):
    return thing["side"] ** 2

def square_new(name, side):
    return {
        "name": name,
        "side": side,
        "perimeter": square_perimeter,
        "area": square_area
    }

def call(thing, method_name):
    print(thing[method_name])
    return thing[method_name](thing)

sq= square_new("sq", 2)
print(call(sq, "perimeter"))




