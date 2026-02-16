# Class declaration

class Student:
    def __init__(self, name = None, age = 0 ): # Constructor Method
        # Instance atributes
        self.name = name
        self.age = age

    # Instance Methods
    def birthday(self):
        self.age += 1

    def __str__(self):          # Dunder Method
        return f'{self.name} is student and has {self.age} years old.'
    
    def __getstate__(self):
        return f'Estado: name = {self.name} ; age = {self.age}'

# Object declaration
s1 = Student("Miguel", 23)
s1.birthday()
#print(s1)
print(s1.__dict__)      # Attribute 
print(s1.__getstate__()) # Method

# print(s1.__doc__)  #Dunder Attribute