class Person:
    # name = "Akhil"
    # occ = "Dealer"
    def __init__(self, name, occ):
        print("Hey I am a person")
        self.name = name
        self.occ = occ


    def info(self):
        print(f"{self.name} is a {self.occ}")


a = Person("Akhil", "Dealer")
b = Person("Golu", "HR")
a.info()
b.info()
# print(a.name)
# a.name = "Golu"
# a.occ = "HR"
# a.info()