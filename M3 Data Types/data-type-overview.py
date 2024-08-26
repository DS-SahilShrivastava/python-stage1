from asyncio import new_event_loop
from tempfile import tempdir


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


#----------------------------------------------------------------------NEW FUNCTION-----------------------------------------------------------------------------------------------------------------------------------

#checking on the operation in the tuple data-type
def tuple_ops():
    #initialisation of tuple can be done with or without parenthesis
    my_colors=('blue','naragi','baingani','aakashi')
    my_food='roti','rice','daal','vegetable'
    print('Initialisation of the tuple ','\n with parenthesis:',type(my_colors),'\n without parenthesis',type(my_food))

    # To create a tuple with one element, you must add an extra comma at the end:
    it_should_be_tuple = 1,
    print("Length of a tuple initialised as 1, ",len(it_should_be_tuple))

    #packing and unpacking
    #packing means assigning values to the tuple
    #unpacking means extracting values of a tuple
    (a,b,c)=(40,50,60)
    print('packing the tuple into 3 variable a,b,c',a,b,c)
    print(b)

    cars=('audi','mercedes','BMW')
    car1,car2,car3=cars
    print(car1,car2,car3)

    # Asterisk are used when the number of variables are less than the value of the tuple
    car1, *rest_cars = cars
    print('Unpacking the values in tuple using asterisk to the element at the end :',car1,rest_cars)

    *car1, rest_cars,car3,car4 = cars
    print('Unpacking the values by changing the position of the asterisk :',car1,rest_cars,car3,car4)

    #Swapping the variables
    #using a temporary variables
    a=19
    b=20
    print(f'a and b before swapping are {a} and {b}')
    temp=a
    a = b
    b=temp
    print(f'a and b after swapping are {a} and {b}')

    #without using temp variable
    a,b=b,a
    print(f'swapped a and b values by using packing unpacking  are {a} and {b}')

    #using '==' and 'is' operator
    x=(1,2,3,4)
    y=(1,2,3,4)
    print(x==y)
    print(id(x),id(y)) #It's because a tuple is an immutable type. And Python uses this approach as part of memory management, not only with tuples. As a result, the Python interpreter does not create a duplicate of the tuple in memory for optimizing purposes.
    print(x is y)

    #checking the same for list
    x=[1,2,3,4]
    y=[1,2,3,4]
    print(x==y)
    print(id(x),id(y))
    print(x is y)

    x=2*100
    y=2*100
    print('for x=2*100 y=2*100',x==y,id(x),id(y),x is y)

    x=(1,2,"python"*100)
    y=(1,2,"python"*100)
    print('for x=(1,2,"python"*100) y=(1,2,"python"*100)',x==y,id(x),id(y),x is y)

def set_and_dict():
    #SETS
    new_set=set((1,4,'34','sahil'))
    print(new_set)
    my_set={1,2,3,'34','sahil'}
    print(type(my_set))
    my_dict={}
    print(type(my_dict))

    #Sets are iterable but do not record element position or order of insertion. Accordingly, sets do not support indexing, slicing, or other sequence-like behavior
    int_set=set([1,2,4,2,1,3,4,1])
    print(int_set)
    #sets are iterable
    for num in int_set:
        print(num)
    if int('2') in int_set:
        print("yayaa")

    # A hash value is used for identifying data.
    # All the not hashable objects are commented , only tuples are hashable
    # print(hash(int_set))          #set
    # print(hash(list(int_set)))    #list
    print(hash(tuple(int_set)))     #tuple
    # print(hash(my_dict))          #dictionary


    # Set Manipulations
    # By Operators
    # Union
    a={1,2,3,4,5,6}
    b={5,6,7,8,9}
    print("Set a :",a,'\n Set b :',b)
    union=a|b # or you can use a.union(b)
    print(f"Union of the set {a} and {b} are :",union,type(union))
    intersect=a&b # or you can use a.intersection(b)
    print(f"Intersection of set {a} and {b} are : ",intersect,type(intersect))
    difference=a-b # or you can use a.difference(b)
    print(f"Difference of the set {a} and {b} are : ",difference,type(difference))

    #By Methods
    c={11,12,12,14,15}
    a.update(b,c)
    print("you can use update method also to fetch the union of the sets :",a)

    a.add(999)
    print('you can add any element in a set by using .add() method , here we have added 999',a)
    a.remove(999)
    print('you can remove any element in a set by using .remove() method , here we have removed 999',a)
    a.clear()
    print('Or you can clear the whole set by calling .clear() method: a=',a)

    #DICTIONARY
    my_dict=dict([(1,'sahil'),(2,'shrivastava')])
    print(my_dict)
    print(f'the data type for {my_dict} is ',type(my_dict))

    print(my_dict[2])
    my_dict[3]='The'
    my_dict[4]='Boss'
    print(my_dict)

    # To remove a pair from the dictionary, use the del statement with an exact key to delete
    del my_dict[3]

    #Iteration in dictionary
    for i in my_dict.items():
        print(i,type(i))
    for i in my_dict.keys():
        print(i)
    for i in my_dict.values():
        print(i)

    #Dictionary Manipulations
    #The get() method takes a key as a parameter and returns the value by this key. The method doesn't raise an error if the key doesn't exist
    print(my_dict.get(4))
    print(my_dict.get(9))

    #The update() method takes another dictionary or some collection of key-value pairs as an argument and updates all matching pairs in the original dictionary and adds key-value pairs for keys that don’t exist in the original dictionary
    blank_d = {
        "name": "",
        "age": 0,
        "is_registered": False,
        "rate": 0,
        "total_score": 0,
        "linked_ids": []
    }

    my_dict.update(blank_d)
    print(my_dict)


set_and_dict()
