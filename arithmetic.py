
friends = 10
friends += 1 #augmented assignment operator , can be -, *, /, ^
friends -= 1
friends ^=3
friends **=2
remainder = friends % 3

x = 3.34
y = -5
z = 6

result = round(x)

print(result)
print(abs(y)) #abs - absoute val is distance away from 0 as whole num
print(pow(z,2))
print(max(x,y,z))
print(min(x,y,z))

# math module
import math
print(math.pi) #3.141592653589793
print(math.e) #2.718281828459045
print(math.sqrt(16)) #4.0
print(math.ceil(9.1)) #10
print(math.floor(9.1)) #9

# Q. calculate circumference of circle
radius = float(input("Enter radius of circle: "))
circum =  2 * radius * math.pi 
#area = math.pi * radius**2
area = math.pi * pow(radius,2)
print(f"The circumference is {round(circum, 2)}cm")
print(f"The area is {round(area, 2)}cm2")

# hypotenuse of right triangle
a = float(input("Enter perpendicular: "))
b = float(input("Enter base: "))

c = math.sqrt(pow(a,2)+pow(b,2))
print(f"The Hypotenuse is: {c}cm")








