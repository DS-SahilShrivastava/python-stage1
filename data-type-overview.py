from asyncio import new_event_loop


def complex_num():
    # Checking on the complex numbers
    x = '1+2j'  # if you give space between the number ,+ sign and imaginary character then it wil throw an error
    y = complex(x)
    print(type(x), type(y))

#----------------------------------------------------------------------NEW FUNCTION-----------------------------------------------------------------------------------------------------------------------------------


def div_data_type():
    # Testing that the / operator always give output as a float only
    x = 12
    y = 2
    c = x / y
    print(c, type(c))  # the output type is going to be float only

#----------------------------------------------------------------------NEW FUNCTION-----------------------------------------------------------------------------------------------------------------------------------


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


#----------------------------------------------------------------------NEW FUNCTION-----------------------------------------------------------------------------------------------------------------------------------


#Random Library Usage
import random
def random_class():
    x, y = 0, 6
    dice_roll = random.randint(x, y)
    print("The digit on the dice will be ", dice_roll)
    rand_num = random.randrange(x, y)  # return s a randomly selected number from the sequence
    print(rand_num)
    print(random.random())  # returns a random number between 0 and 1 , is double



#----------------------------------------------------------------------NEW FUNCTION-----------------------------------------------------------------------------------------------------------------------------------


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
        case "hello world": # Match-case is case-sensitive
            print('hello world in caps lock off')
        case "Hello World":
            print("Hello Lock in Caps on")


    # Ternary Operator conditions
    fruit ="apple"
    is_apple= "yes" if fruit=='apple' else "no"
    print(is_apple)

    #Checking the type of None Keyword
    print(type(None))



#----------------------------------------------------------------------NEW FUNCTION-----------------------------------------------------------------------------------------------------------------------------------

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


#----------------------------------------------------------------------NEW FUNCTION-----------------------------------------------------------------------------------------------------------------------------------

#testing the properties and operations in string
def string_ops():
    print("Yes all of them belongs to str class" if type('a')==type("a")==type('''a''')==type("""a""") else "No from different classes")#the type of all these is string only
    print('hello guys my name is: \t \n \"Sahil Shrivastava\" ') # (\'\') used for quoting inside the string
    print('not this \r Only this \r Now this ') #only the string after the \r will be used and rest of the string prior to the \r will be discarded

    #using slice operations in strings
    my_str="Hello-World"
    slice_object=slice(1,3,-1) # this is a slicer object that helps in slicing the string, it can be used as a index of the string
    print(slice_object)
    print("Slicing by slice() function :",my_str[slice_object],'\n',"Slicing the string by [:]",my_str[1:3])
    for i in my_str.split("-"):
        print("Splitting the ",i)
    print(my_str.upper())
    print(my_str.find("rl"))

    #using format keyword
    name='Sahil'
    age='12'
    company='EPAM System'
    print('Hi , my name is {} and my age is {}. I work for {} as a Data Scientist'.format(name,age,company))
    print(f"Hi, My name is {name}, and my age is {age}. And I work for Data Scientist {company}")

    message=input("Input any 3 words, you will win you can guess it correct:")
    if 'Sahil' or 'friend' or 'bottle' in message:
        print(f"Hurrayy , You guessed the correct word {message}!!")


#----------------------------------------------------------------------NEW FUNCTION-----------------------------------------------------------------------------------------------------------------------------------

#checking for operations and functions used in list
def list_ops():
    my_list=['hello',32,True,'string',2.928]
    print('Original list is ',my_list)
    #change list by index
    my_list[1]=45
    print('Updated list is :',my_list)
    #adding new items in the list
    my_list.append("Appended object")
    print("List after using append function :",my_list)
    #doing slicing and iteration i the list
    step=2
    itr_list=my_list[::step]
    print(itr_list)

    #LIST MANIPULATION
    int_list=[3,6,1,45,8,432,0,221]
    print('Integral list is :',int_list)
    sorted_my_list=sorted(int_list)
    int_list.sort()
    print('Integral list after sorting using .sort() keyword as :',int_list)
    print('Integral list after sorting using "sorted" keyword is as : ',sorted_my_list)
    print('length of the list is as :',len(int_list))
    #The extend method allows you to add all the items from another iterable object, for example, from another list or string:
    some_str='23.45423'
    my_list.extend(some_str)
    print(f"my_list after using the extend function and {type(some_str)} {some_str} in between ",my_list)
    #the count method allows you to count the number of times something appears in the list
    print(my_list.count('4'))
    #The pop method allows the removal and returning of items from a list by the given index. If an index is not specified, it removes and returns the last item in a list.
    print("Last element has been popped out of the list :",my_list.pop(),' \n list after doing the pop operation: ',my_list)
    idx=5
    print(f"Element at the {idx} index has been popped from my_list : ",my_list.pop(idx),' \n list after doing the pop operation: ',my_list)

    #using list comprehension
    n=20
    even_number=[]
    for i in range (0,n):
        if i%2==0 or (not i%2):
            even_number.append(i)
    print("List without using list comprehension method:",even_number)

    # new_list = [expression for item in iterable if condition == True]
    new_even_list=[i for i in range (0,n) if not i%2]
    print("List using list comprehension method:",new_even_list)


