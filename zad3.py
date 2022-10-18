import math
class SodaCan:
    def __init__(self,high,radius):
        self.high=high
        self.radius=radius
    def get_surface_area(self):
        return 2*math.pi*self.radius**2+2*math.pi*self.radius*self.high
    def get_volume(self):
        return math.pi*self.high*self.radius**2
cocacola=SodaCan(2,2)
print(SodaCan.get_surface_area(cocacola))