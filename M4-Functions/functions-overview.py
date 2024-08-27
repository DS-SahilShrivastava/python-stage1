#This file shares the knowledge related to the topic of Functions
#FIRST CLASS FUNCTION
def first_class():
    #assigning functions to variables
    def square(c):
        return (f"Square of the number {c} is",c**2)

    square_2=square(2)
    print(square_2)

    #passing functions as an argument
    def apply_square(square,*args):
        lst=[]
        for arg in args:
            lst.append(square(arg))
        return(lst)

    print(apply_square(square,3,4,5,6,7,8))

    #storing functions in a data structure
    def cube(c):
        return c**3
    my_dict={'square':square , 'cube': cube}
    print(my_dict['square'](6))

    #'all' and 'any' built-in function
    def all_and_any():
        #It returns False only if any elements of the iterable are false.
        print(all({}))
        print(all([1, True, [2, 'name']]))
        print(all({1==2}))

        #It returns True only if any elements of the iterable are true.
        print(any({}))
        print(any([0, tuple(), False]))
        print(any([1, True, [2, 'name']]))


