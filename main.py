import math
class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def printpoint(self):
        return self.x, self.y
    def distance(a,b):
        return math.sqrt((b.x-a.x)**2+(b.y-a.y)**2)

a=Point(5,0)
print(Point.printpoint(a))
b=Point(2,0)
print(Point.distance(a,b))






