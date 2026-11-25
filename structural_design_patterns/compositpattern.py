'''
A folder in a folder , file in a folder, all 2 folders and text file in a 3rd folder
so on... parent- leaf-root-concept
try example in book  using Ternary Operatorsi
'''

from abc import ABCMeta,abstractmethod

class IDepartment(metaclass=ABCMeta):
    @staticmethod
    @abstractmethod
    def __init__(self, employees):
        pass
    'Implement in child class'

    def print_department(self):
        'Implement in the child class'

class Accounting(IDepartment):
    def __init__(self, employees):
        self.employees = employees

    def print_department(self):
        print(f"Accounting Department: {self.employees}")

class Developer(IDepartment):
    def __init__(self,employees):
        self.employees = employees

    def print_department(self):
        print(f"Developer Department: {self.employees}")

class ParentDepartment(IDepartment):
    def __init__(self,employees):
        self.employees = employees
        self.base_employees = employees
        self.sub_dept = []

    def add(self,dept):
        self.sub_dept.append(dept)
        self.employees+= dept.employees

    def print_department(self):
        print(f"Parent Department")
        print(f"Parent Department Base Employees: {self.base_employees}")
        for dept in self.sub_dept:
            dept.print_department()
            print(f"Total no of employees: {self.employees}")

dept1 = Accounting(100)
dept2 = Developer(10)

parent_dept = ParentDepartment(20)
parent_dept.add(dept1)
parent_dept.add(dept2)

parent_dept.print_department()


