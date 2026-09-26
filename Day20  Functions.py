def calculateGmean(a, b):
    mean = (a*b)/(a+b)
    print(mean)

def isGreater(a, b):
    if(a>b):
        print("First number is greater")
    else:
        print("Second number is greater or equal")

def isLesser(a, b):
    pass


a = 9
b = 8
# if(a>b):
#     print("First number is greater")
# else:
#     print("Second number is greater or equal")
isGreater(a, b)

calculateGmean(a, b)
# gmean1 = (a*b)/(a+b)
# print(gmean1)
c = 8
d = 75
# if(c>d):
#     print("First number is greater")
# else:
#     print("Second number is greater or equal")
# gmean2 = (c*d)/(c+d)
# print(gmean2)
isGreater(c, d)
calculateGmean(c, d)