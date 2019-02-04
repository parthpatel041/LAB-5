import math

class Point:
	
	def __init__(self):
		self.x = 0
		self.y = 0
	

def dist_btw_points(a,b):
	d1 = a.x - b.x
	d2 = a.y - b.y
	dist = math.sqrt(d1**2 + d2**2)
	return dist

x = Point()   
y = Point()         
print(x)
print(y)
print(x != y)

p0 = Point()
p0.x = 5
p0.y = 7

p1 = Point()
p1.x = 10
p1.y = 15
print('Distance')
print(dist_btw_points(p1, p0))
print('')

