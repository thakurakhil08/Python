# def double(x):
#     return x*2


def appl(fx, value):
    return 6 +fx(value)



double = lambda x: x*2
cube = lambda x: x*x*x
# avg = lambda x, y: (x + y)/2
avg = lambda x, y, z: (x + y + z)/3


print(double(5))
print(cube(5))
# print(avg(7, 3))
print(avg(5, 3, 10))
print(appl(cube, 2))
print(appl(lambda x: x*x*x, 2))