class Person:
    name = "Akhil"
    occupation = "Software Engineer"
    networth = 10
    def info(self):
        print(f"{self.name} is a {self.occupation}")


a = Person()
b = Person()
c = Person()
a.name = "John"
a.occupation = "Doctor"
# print(a.name, a.occupation)

b.name = "Golu"
b.occupation = "Engineer"
a.info()
b.info()
c.info()