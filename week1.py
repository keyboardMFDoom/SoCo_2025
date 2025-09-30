import math
class Shape:
    def __init__(self, name): ##automatically called if class is created
        self.name = name ##instanciated

    def perimeter(self):
        raise NotImplementedError("cannot compute perimeter")


    def area(self):
        raise NotImplementedError("cannot compute area")

class Square(Shape):
    def __init__(self, name,side):
        super().__init__(name)
        self.side = side

    def perimeter(self):
        return self.side*4
    def area(self):
        return self.side**2

class Circle(Shape):
    def __init__(self, name, radius):
        super().__init__(name)
        self.radius = radius
    def perimeter(self):
        return 2*math.pi*self.radius
    def area(self):
        return self.radius*math.pi**2


l = [Circle("circle", 2), Square("square", 20)]
#for element in l:
 #   n = element.name
  #  a = element.area()
   # p = element.perimeter()
    #print(f"{n} has area {a} and perimeter {p}")

##########                                      Part 2                                      ##########

a = 10

def example():
    print("in example")

alias = example
print(type(alias))

b = a
## in both cases: the variables b and alias point to the same memory as example an a


def example2():
    print("in example2")

lyst = [example(), example2()]
# a variable pointing to a lyst with two objects pointing to the functions example and example2

### CODE IS DATA AS WELL (SOMEWHERE IN MEMORY) ###

##########                                      Part 3                                      ##########
dict_of_funcs = {"func": example, "func2": example2}
for f in dict_of_funcs:
    dict_of_funcs[f]

##Object system implemented in the same way as dictionaries

def square_perimeter(obj):
    return obj["side"]*4
def square_area(obj):
    return obj["side"]**2


sq = {
    "name":"generic square",
    "side":10,
    "perimeter":square_perimeter,
    "area":square_area
}
#Now the object is not within a class/function, it's all bundled up in the dictionary "sq". How do we deal with this?

def call(obj, method_name):
    return obj[method_name](obj)

a = call(sq, "area") #equivalent to sq.area(sq), just now we engineered it ourselves
print(a)

#Problem arise if I want to create a new square. I.e. sq2 has to be copied.

#Solution
def square_new(name, side):
    return {
        "name": name,
        "side": side,
        "perimeter": square_perimeter,
        "area": square_area
    }
#Creation of new objects with same functions just different variables

#Define it ourselves for a circle
def circle_perimeter(obj):
    return obj["radius"]*2*math.pi
def circle_area(obj):
    return math.pi*obj["side"]**2

def circle_new(name, radius):
    return {
        "name": name,
        "radius": radius,
        "perimeter": 2*radius*math.pi,
        "area": math.pi*radius**2
    }

#With this we have to continuously update the constructor if we want to implement a new function.

#Solution: Separate functions from the data
Circle = { 
        "perimeter": circle_perimeter,
        "area": circle_area,
        "_class": "Circle"
    }

Square = {
    "perimeter": square_perimeter,
    "area": square_area,
    "_class": "Square"
}

Shape = {
    "density":"wait",
    "_classname": "Shape",
    "_parent": None
    }

def call(obj, method_name, *args):
    return obj["_class"][method_name](obj,*args)

#constructor is about the data not the functions