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

#####################################################

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

####################################################################################
