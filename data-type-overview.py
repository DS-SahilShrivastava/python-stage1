#Checking on the complex numbers
from math import acosh

x='1+2j' #if you give space between the number ,+ sign and imaginary character then it wil throw an error
y= complex(x)
print(type(x),type(y))

#Testing that the / operator always give output as a float only
x=12
y=2
c=x/y
print(c,type(c)) #the output type is going to be float only

#using math module for doing operations
import math
angle_degrees=60
angle_radians=math.radians(angle_degrees)
print(angle_radians)
print("value of sin x:",math.sin(angle_radians),"\n","value of cos x:",math.cos(angle_radians),"\n","value of tan x:",math.tan(angle_radians))

x=3.4 #interpreted as (x,0)
y=9.8 #interpreted as (0,y)
print("Eucledian distance between these two points on their respective axis is ",math.hypot(x,y))