# Class declaration

class Student:
    def __init__(self): # Constructor Method
        # Instance atributes
        self.name = ''
        self.age = 0

    # Instance Methods
    def birthday(self):
        self.age += 1

    def message(self):
        return f'{self.name} is student and has {self.age} years old.'

# Object declaration
s1 = Student()
s1.name = 'Miguel'
s1.age = 23
s1.birthday()
print(s1.message())

s2 = Student()
s2.name = 'Mariana'
s2.age = 31
s2.birthday()
print(s2.message())
