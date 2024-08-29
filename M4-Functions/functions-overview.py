#This file shares the knowledge related to the topic of Functions
from functools import reduce

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


#Functional Argument
def functional_argument():

    #argument by position or name
    def by_position(arg1, arg2):
        pass
    by_position(1,2)

    def by_name(arg1,arg2):
        pass
    by_name(arg1=1,arg2=3)
    by_name(arg2=4,arg1=0)

    def mixed_arguments(arg1,arg2,arg3):
        print(arg1,arg2,arg3)
    mixed_arguments(1,arg3=9,arg2=9)
    mixed_arguments(2,arg3=2,arg2=0)

    #required and optional argument
    def req_arg(arg1,arg2):
        pass # Here both the arg1 and arg2 are required as no default value has been allocated to them
    def optional_args(arg1,arg2=9):
        pass # Here the arg2 is an optional argument as it has been allocated a default value, so one dmay or may not neet to define it while calling the function
    optional_args(2,6)
    optional_args(9)

    #*args and **kwargs
    def show_argument(*args,**kwargs):
        print('args:',args,'kwargs',kwargs)
        print(args[1:3])
        for item in kwargs.items():
            print(item)
    show_argument(1,2,3,4,'sahil','shrivastava',sahil='The',shrivasta='Boss',kwarg3=[8,6,8,9,0])

    list_of_args=[1,2,'name','3',[3,23,2,3]]
    dict_of_keys={'epam':'company','datascience':'team'}
    show_argument(*list_of_args,**dict_of_keys)

    def foo(pos1, pos2, /, pos_or_kwd1, pos_or_kwd2='default', *args,
            kwd_only1, kwd_only2='default', **kwargs):
        print(
            f"pos1={pos1}",
            f"pos2={pos2}",
            f"pos_or_kwd1={pos_or_kwd1}",
            f"pos_or_kwd2={pos_or_kwd2}",
            f"args={args}",
            f"kwd_only1={kwd_only1}",
            f"kwd_only2={kwd_only2}",
            f"kwargs={kwargs}",
            sep="\n",
        )

    foo(1, 2, 3, 'not default', 6, 'it is an arg too', kwd_only1=4,
        kwd_only2='not default', kwarg1=5, kwarg2='it is a kwarg too')

def lambda_func():
    # The lambda function is an anonymous inline function consisting of a single expression which is evaluated when the function is called
    # universal function expression VS Lambda expression
    def sum(a,b):
        return a+b
    sum_lambda=lambda a,b : a+b
    sum_lambda(4,5)
    # print(help(list.sort))

    def key_arg():
        lst = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
        # print(sorted(lst))
        int_lst = ['123', '264', '345', '456']
        filter_function = lambda pair_item: pair_item[1]

        def filter_function2(pair_item):
            print(pair_item[1])
            return pair_item[1]

        # If a key function is given, apply it once to each list item and sort them,ascending or descending, according to their function values.
        # this lst.sort here is calling the 0th item out of every traversal in the data structure and then based on that key , the elements are sorted
        int_lst.sort(key=filter_function2, reverse=True)
        print(int_lst)
        lst.sort(key=lambda pair_item: pair_item[1], reverse=False)
        print(lst)

    def map_filter_reduce():
        # Map function
        # map(function, iterable) returns an iterator that applies a function to every item of the iterable.
        nums = [1, 2, 3, 4, 5, 6, 7, 8]
        strs = ['a', 'b', 'c']
        double_all = map(lambda x: x * 2, strs)
        square_all = map(lambda num: num ** 2, nums)
        print(list(square_all), '\n', list(double_all))

        # Filter function
        # filter(function, iterable) returns an iterator from elements of the iterable for which the function returns True. If the function is None, the identity function is assumed; that is, all elements of the iterable that are false are removed.
        nums2 = [23, 46, 78, 65, 32, 12, 90, 75, 34, 66, 43, 23]
        filter_even = filter(lambda x: x % 2 == 0, nums2)
        print(list(filter_even))
        bool_lst = [1, 0, 0, 21, 12, 10, 0, 0, 0, 1, 1, 1, 1, 0]

        # filter(None, iterable) Purpose: Filters elements from the iterable by removing elements that are considered False in a boolean context. Behavior: Here, None is used as a shorthand for filtering out elements that are falsy (i.e., False, None, 0, empty strings, empty lists, etc.).
        none_filter = filter(None, bool_lst)
        print(list(none_filter))

        reduce_lamb = reduce(lambda x, y: x + y, nums2)
        print(reduce_lamb)

        x = 5
        x_lst = [x for x in range(1, x + 1)]
        factorial = reduce(lambda z, y: z * y, x_lst)
        print(x_lst, factorial)

    def recursion():
        def fibonacci(n):
            if n==0 or n==1:
                value=1
            elif n==2:
                value =1
            else:
                value = fibonacci(n-2) + fibonacci(n-1)
            return value
        n=9
        print("LOCAL KEYWORDS ARE AS : ",locals())
        print(fibonacci(n))
    #The biggest con is that the recursion functions use a lot of space.
    recursion()


java='language'
print("GLOBAL KEYWORDS ARE AS : ",globals())
lambda_func()