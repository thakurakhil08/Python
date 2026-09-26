name = "Akhil"
Friende = "Shahbaz"
anotherfriend = 'John'

# apple = ('He said, "I want to eat an apple".')

# apple = """He said,
# Hii Akhil
# I am good 
# "I want to eat an apple."""


apple = '''He said,
Hii Akhil
I am good 
"I want to eat an apple.'''

print("Hello " + name )
# print(apple)
print(name[0])
print(name[1])
print(name[2])
print(name[3])
print(name[4])
# print(name[5])  #Throws error as index out of range
print("Lets use a for loop\n")
for character in apple:
    print(character)