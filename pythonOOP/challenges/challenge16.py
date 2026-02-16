from rich import print
from rich import inspect

class Employee:
    #Class Attributes
    enterprise = 'Video curse'

    def __init__(self, name, sector, role):     # Constructor Method
        # Instance Attributes
        self.name = name
        self.sector = sector 
        self.role = role
    
    # Methods

    def introduce(self):
        return f":handshake: Hi! I'm [blue]{self.name}[/blue]. I work in the [red]{self.sector}[/red] sector as a [green]{self.role}[/green] of enterprise {self.__class__.enterprise} "

# Object declaration
emp1 = Employee("Miguel", "Finance", "Analyst")
emp2 = Employee("Mariana", "IT", "Developer")

# Employees introducing themselves
print(emp1.introduce())
print(emp1.enterprise)
