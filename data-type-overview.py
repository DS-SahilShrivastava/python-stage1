#Checking on the complex numbers
x='1+2j' #if you give space between the number ,+ sign and imaginary character then it wil throw an error
y= complex(x)
print(type(x),type(y))

#Testing that the / operator always give output as a float only
x=12
y=2
c=x/y
print(c,type(c))
