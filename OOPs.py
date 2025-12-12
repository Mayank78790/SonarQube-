# OOP- Object Oriented Programming

# using list - creating student records
# student details
student_1 = ['Madhav', 10] # Name, Grade
student_2 = ['Vishakha', 12] 
student_3 = 'Keshav'

student_1.append('A')
print(student_1)
print(f'{student_1[0]} is in class {student_1[1]}')
print(f'{student_2[0]} is in class {student_2[1]}')


# using OOPs- creating student records

# class - blueprint or template
# __init__ method - constructor, value initialize - fix
# self parameter - reference or connection build btw class and object - fix
class Student: # student class
    def __init__(self, name, grade, percentage):  # method
        self.name = name  # attribute 
        self.grade = grade # attribute 
        self.percentage = percentage # attribute

    def student_details(self): # method 
        print(f"{self.name} is in class {self.grade}, with {self.percentage}%")

# object - instance of class 
student1 = Student('Madhav', 11, 96)
print(student1.name, student1.grade)

student2 = Student('Vishakha', 12, 99)
print(student2.name, student2.grade)

print(student1.percentage)
student1.student_details()
student2.student_details()

print(student1.__dict__) 

# modify object property
print(student1.percentage) 
student1.percentage = 100 # modify
print(student1.percentage)

# delete object property 
print(student1.__dict__) 
del student1.percentage
print(student1.__dict__) 

# delete object 
del student1
print(student1)



# class - blueprint or template
class Student: # student class
    def __init__(self, name, grade, percentage, team):  # method
        self.name = name  # attribute 
        self.grade = grade # attribute 
        self.percentage = percentage # attribute
        self.team = team

    def student_details(self): # method 
        print(f"{self.name} is in class {self.grade}, with {self.percentage}% and is in team {self.team}")

team1 = 'A'
team2 = 'B'

# object - instance of class 
student1 = Student('Madhav', 11, 96, team1)
# print(student1.name, student1.grade)

student2 = Student('Vishakha', 12, 99, team2)
# print(student2.name, student2.grade)

# print(student2.team)
student1.student_details()
student2.student_details()



# 4 features in OOPs 
# Abstraction
# Encapsulation
# Inheritance
# Polymorphism


# Abstraction 
# hiding unnecessary details from users through class, methods 
# EX - 1. Abstract Bank Account
from abc import ABC, abstractmethod

class BankAccount(ABC):
    @abstractmethod
    def withdraw(self, amount):
        pass

    @abstractmethod
    def deposit(self, amount):
        pass

class SavingsAccount(BankAccount):
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print("Withdrawn:", amount)
        else:
            print("Insufficient funds.")

    def deposit(self, amount):
        self.balance += amount
        print("Deposited:", amount)

acc = SavingsAccount(1000)
acc.deposit(500)
acc.withdraw(200)

# EX - 2 Abstract Animal Movement

from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def move(self):
        pass

class Bird(Animal):
    def move(self):
        print("Flies in the sky.")

class Snake(Animal):
    def move(self):
        print("Crawls on ground.")

bird = Bird()
snake = Snake()
bird.move()
snake.move()

# Encapsulation 
# Restrict access to certain attributes or methods to protect data and enforce controlled access
#EX-1: Student Data Protection

class Student:
    def __init__(self, name, roll_no):
        self.__name = name
        self.__roll_no = roll_no

    def get_name(self):
        return self.__name

    def set_name(self, name):
        if name:
            self.__name = name

student = Student("Komal", 42)
print(student.get_name())
student.set_name("Aman")
print(student.get_name())

#EX-2:Inventory with Validation

class Inventory:
    def __init__(self):
        self.__stock = 100

    def get_stock(self):
        return self.__stock

    def add_stock(self, amount):
        if amount > 0:
            self.__stock += amount

    def remove_stock(self, amount):
        if 0 < amount <= self.__stock:
            self.__stock -= amount

inv = Inventory()
print(inv.get_stock())
inv.add_stock(20)
inv.remove_stock(50)
print(inv.get_stock())

# Inheritance 
# allows one class (child) to reuse the prop and methods of another class (parent). 
# 1. Single Inheritance
#  Ex- 1
class Employee:
    def work(self):
        print("Employee working.")

class Manager(Employee):
    def manage_team(self):
        print("Manager managing team.")
mgr = Manager()
mgr.work()
mgr.manage_team()

# Ex- 2
class Employee:
    def work(self):
        print("Employee working.")

class Developer(Employee):
    def write_code(self):
        print("Developer writing code.")
dev = Developer()
dev.work()
dev.write_code()

# 2. Multiple Inheritance
# Ex- 1
class Employee:
    def work(self):
        print("Employee working.")
class AdminRights:
    def approve_leave(self):
        print("Admin approving leave.")
class Manager(Employee, AdminRights):
    pass
mgr = Manager()
mgr.work()
mgr.approve_leave()

# Ex- 2
class Employee:
    def work(self):
        print("Employee working.")
class TechSkills:
    def code_review(self):
        print("Reviewing code.")
class Developer(Employee, TechSkills):
    pass
dev = Developer()
dev.work()
dev.code_review()

# 3. Multilevel Inheritance
# Ex- 1 
class Employee:
    def work(self):
        print("Employee working.")
class Manager(Employee):
    def manage_team(self):
        print("Manager managing team.")
class SeniorManager(Manager):
    def strategize(self):
        print("Senior Manager planning strategy.")
s_mgr = SeniorManager()
s_mgr.work()
s_mgr.manage_team()
s_mgr.strategize()

# Ex- 2
class Employee:
    def work(self):
        print("Employee working.")
class Developer(Employee):
    def develop(self):
        print("Developing software.")
class Tester(Developer):
    def test(self):
        print("Testing software.")
tester = Tester()
tester.work()
tester.develop()
tester.test()

# 4. Hierarchical Inheritance
# Ex- 1
class Employee:
    def work(self):
        print("Employee working.")
class Manager(Employee):
    def manage(self):
        print("Manager specific method.")
class Developer(Employee):
    def develop(self):
        print("Developer specific method.")
mgr = Manager()
dev = Developer()
mgr.work()
mgr.manage()
dev.work()
dev.develop()

# Ex- 2
class Employee:
    def work(self):
        print("Employee working.")
class Developer(Employee):
    def code(self):
        print("Developer coding.")
class Tester(Employee):
    def test(self):
        print("Tester testing.")
dev = Developer()
tester = Tester()
dev.work()
dev.code()
tester.work()
tester.test()

# 5. Hybrid Inheritance
# Ex- 1
class Employee:
    def work(self):
        print("Employee working.")
class Manager(Employee):
    def manage(self):
        print("Manager managing.")
class Developer(Employee):
    def develop(self):
        print("Developer developing.")
class Lead(Manager, Developer):
    def lead_team(self):
        print("Lead leads the team.")
lead = Lead()
lead.work()
lead.manage()
lead.develop()
lead.lead_team()

# Ex- 2
class Employee:
    pass
class Developer(Employee):
    pass
class Tester(Employee):
    pass
class DevTester(Developer, Tester):
    def multitask(self):
        print("DevTester can develop and test.")
dt = DevTester()
dt.multitask()


# Polymorphism
# allows methods in diff classes to have same name but diff behavior depending on objects 

#EX-1  Operator Polymorphism
print(2 + 3)       # Addition of numbers
print("a" + "b")   # Concatenation of strings
print([1, 2] + [3, 4])  # Concatenation of lists

# EX-2 Function Polymorphism
def volume(x, y=None, z=None):
    if y is None and z is None:
        return x * x * x
    elif z is None:
        return x * x * y
    else:
        return x * y * z

# Find the volume of different shapes
print(volume(3))       # Cube
print(volume(3, 4))    # Square Prism
print(volume(3, 4, 5)) # Cuboid

# EX-3 Method Polymorphism
class Drink:
    def show(self):
        print("Generic Drink")

class Juice(Drink):
    def show(self):
        print("Juice Drink")

d = Drink()
j = Juice()
for item in [d, j]:
    item.show()

