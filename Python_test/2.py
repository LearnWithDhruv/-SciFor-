class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        self._name = value

    @staticmethod
    def greet(msg):
        print(msg)
    
    is_adult = lambda age: age >= 20

names = ["dhruv", "daksh", "akash", "ankush"]
upper_case_names = list(map(lambda x: x.upper(), names))
print("Names in uppercase:", upper_case_names)

@Person.greet
def greet():
    print("Hello, Welcome!")

person = Person("Dhruv", 20)
print("Original Name: ", person.name)
person.name = "Daksh"
print("Updated Name:", person.name)

age = 20
print(f"Is dhruv eligible for driving? {'Yes' if Person.is_adult(age) else 'No'}")