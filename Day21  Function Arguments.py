# def average(a, b):
#     print("The average is ", (a+b)/2)

# average(4, 6)

# def average(a=9, b=1):
#      print("The average is ", (a+b)/2)

# average(4, 6)
# average(1, 5)

# def name(fname, mname = "Akhil", lname = "Thakur"):
#     print("Hello,", fname, mname, lname)

# name("Amy")

# average(b=9, a=21)

def average(*numbers):
    #print(type(numbers))
    sum = 0

    for i in numbers:
        sum = sum + i

    # print("Average is:", sum / len(numbers))
    return sum / len(numbers)

c = average(5, 6, 7, 1)
print(c)

# def name(**name):
#     # print(type(name))
#     print("Hello,", name["fname"], name["mname"], name["lname"])

# name(mname = "Kumar", lname = "Thakur", fname = "Akhil")