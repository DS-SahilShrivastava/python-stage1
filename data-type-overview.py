from numpy.ma.extras import ndenumerate


def complex_num():
    # Checking on the complex numbers
    x = '1+2j'  # if you give space between the number ,+ sign and imaginary character then it wil throw an error
    y = complex(x)
    print(type(x), type(y))



def div_data_type():
    # Testing that the / operator always give output as a float only
    x = 12
    y = 2
    c = x / y
    print(c, type(c))  # the output type is going to be float only



#using math module for doing operations
import math
def math_class():
    angle_degrees = 60
    angle_radians = math.radians(angle_degrees)
    print(angle_radians)
    print("value of sin x:", math.sin(angle_radians), "\n", "value of cos x:", math.cos(angle_radians), "\n",
          "value of tan x:", math.tan(angle_radians))

    x = 3.4  # interpreted as (x,0)
    y = 9.8  # interpreted as (0,y)
    print("Eucledian distance between these two points on their respective axis is ", math.hypot(x, y))


#Random Library Usage
import random
def random_class():
    x, y = 0, 6
    dice_roll = random.randint(x, y)
    print("The digit on the dice will be ", dice_roll)
    rand_num = random.randrange(x, y)  # return s a randomly selected number from the sequence
    print(rand_num)
    print(random.random())  # returns a random number between 0 and 1 , is double


#Boolean and comparison operator testing
def bool_and_comp():
    a = "1"
    b = 1
    print("is a equals to b", a == b, '\n', 'checking is a IS b ',
          a is b)  # both conditions holds true , but if you even add an extra space in any of them the object changes , the value doesnt, but the id does (you can check this by print(id(' ')))

    print(a and b)
    print(a!=b)

    #flow control statement
    x=33
    y=43
    threshold=30
    if x > threshold and y >threshold:
        print("in the if block",(x+y)/2)
    elif threshold>=30: #If the flow entered the 'IF' block then it will not enter in any other 'ELIF' block
        print("also in the elif block")

    #match/case operations
    my_operations='Hello World'
    match my_operations:
        case "Read":
            pass
        case 'Div':
            pass
        case "hello world": # Match-case is case sensitive
            print('hello world in caps lock off')
        case "Hello World":
            print("Hello Lock in Caps on")


    # Ternary Operator conditions
    fruit ="apple"
    is_apple= "yes" if fruit=='apple' else "no"
    print(is_apple)

    #Checking the type of None Keyword
    print(type(None))


#Checking the operations and basics of loops in python
def loops():
    #while loops
    i=0
    while i<5:
        print('number is still growing in a WHILE LOOP',i)
        i+=1

    #for loop
    x=[1,2,3,4,5,6,7]
    print(x.__getitem__(3))
    print(x.__iter__()) #list iterator used to do iteration on a specified range of a number
    for num in x:
        print('FOR num IN x :',num)

    for i in range(0,4):
        print("All the number within FOR LOOP and range 0 to 5",i)

    #while-else loops
    q=15
    while q<21:#LEgal age to drink alcohol
        print('Yet too small for drinking alcohol, Age:',q)
        q+=1
    else:
        print('Now Big enough to drink, Age:',q)








