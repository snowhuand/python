"""
Create the following classes:
Student - derived from Person,
also has student_id
Musician - derived from Person,
also has play(text)
(Person has a name and an age, with an __init__ that defines these.)
"""

class Person:
    def __init__(self, name="", age=0):
        """
        This is the initialiser for Person class.
        :param name: name of a person
        :param age: age of a person
        """
        self.name = name
        self.age = age

    def __str__(self):
        return "Person class for {} age {}.".format(self.name, self.age)

class Student(Person):
    def __init__(self, name="", age=0, student_id=""):
        super().__init__(name, age)
        self.student_id = student_id

    def __str__(self):
        return "Student class for {} age {} student id {}.".format(self.name, self.age, self.student_id)

class Musician(Person):
    def play(self, text):
        print("Playing {}".format(text))

p1 = Person("John", 20)
print(p1)
s1 = Student("Ken", 23, "0001")
print(s1)
m1 = Musician("Kenny G", 40)
m1.play("Saxophone")
