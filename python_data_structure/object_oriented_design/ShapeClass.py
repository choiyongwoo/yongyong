#ShapeClass.py
import math

class Point(object):
    def  __init__(self, x=0, y=0):
        self.x= x #데이터 속성
        self.y= y
        
    def distance_from_origin(self): #메서드 속성
        #math.hypot (직각 삼각형의 빗변의 길이 구하는 식과 똑같음)
        return math.hypot(self.x, self.y)
    
    def __eq__(self, other):
        return self.x== other.x and self.y== other.y
    
    def __repr__(self):
        return 'point ({0.x!r}, {0.y!r})'.format(self)
    
    def __str__(self):
        return '({0.x!r}, {0.y!r})'.format(self)
class Circle(Point):
    def __init__(self, radius, x=0, y=0):
        super().__init__(x, y) #생성 및 초기화
        self.radius= radius
        
    def edge_distance_from_origin(self):
        return abs(self.distance_from_origin()- self.radius)
    
    def area(self):
        return math.pi*(self.radius**2)
    
    def circumference(self):
        return 2*math.pi*self.radius
    
    def __eq__(self, other):
        return self.radius== other.radius and super().__eq__(other)
    
    def __repr__(self):
        return 'circle ({0.radius!r}, {0.x!r})'.format(self)
    
    def __str__(self):
        return repr(self)