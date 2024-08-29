from numpy.ma.core import left_shift


class Person:
    def __init__(self,name,gender,age,race):
        self.name=name
        self.gender=gender
        self.age=age
        self.race=race
    def person_info(self):
        return f'My name is {self.name}, and my age is {self.age}, my sex is {self.gender} and i belong from {self.race} race \n'

class Employees(Person):
    def __init__(self,name,gender,age,race,salary,job_title,yoe ):
        super().__init__(name,gender,age,race)
        self.salary=salary
        self.job_title=job_title
        self.yoe=yoe

    def employee_info(self):
        return f'{super().person_info()}My salary is {self.salary} and my job title is {self.job_title} and i have {self.yoe} years of experience \n'

#Data Hiding and access specifiers:
class Salary(Employees):
    def __init__(self,name,gender,age,race,salary,job_title,yoe,pf,tax,gratuity,invest):
        super().__init__( name,gender,age,race,salary,job_title,yoe)
        #To denote an attribute as protected, you need to put one underscore _ before the name of an attribute
        self._pf=pf
        #while to mark an attribute as private, put double underscore __.
        self.__tax=tax
        self._gratuity=gratuity
        self.invest=invest

    def deducted_salary(self):
        return(f'{super().employee_info()}Deducted salary of employee {self.name} is :{self.salary - self._pf -self.__tax -self._gratuity - self.invest} \n')


#DIAMOND PROBLEM
class Base():
    def call(self):
        print("ín the base class \n")
class Left(Base):
    def call(self):
        print("Inside the Left class \n")
class Right(Base):
    def call(self):
        print("Inside the right class \n")
class Top(Right,Left):
    # pass
    def call(self):
        print("Ïnside the top class \n")


def main():
    sahil=Employees('sahil','male',21,'índian',700000,'swe',9)
    print((sahil.employee_info()))

    rupesh= Salary('sahil','male',21,'índian',700000,'swe',9,2200,6000,900,10000)
    '''print(rupesh.__tax)''' #this line will throw an error because thr attribute tax is a private attribute thus its name has been changed to _ClassName__attribute name.
    print(rupesh._Salary__tax)
    print(rupesh.deducted_salary())

    # In Python, both built-in and user-defined classes are inherited from the object class. And all the objects are instances of the object class. So, if you try to access an attribute or call method, Python will search for it in the current class. If it's not found, it's searched in the parent classes. The parent classes are searched from left to right order, and each class is searched once.
    diamond=Top()
    print(diamond.call()) # Whichever class has been called first as a parent class that call function will be called , i.e. if Top(Left,Right) is there then Left.call() is called , if Top(Right,Left) is there then Right.call() is called .
    # If the Top has its own call class then it will be called.
    # Priority Method resolution order (MRO) : 1) Self/Top Class 2)Whichever parent class is first called.

main()