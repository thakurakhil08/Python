tup = (1, 2, 3, 45, 345, "Akhil", True)
# tup[0:3]
#tup[0] = 90
print(type(tup), tup)
print(len(tup))
print(tup[0])
print(tup[-1])
print(tup[2])
# print(tup[34])

if 345 in tup:
    print("Yes 345 is present in this tuple")
tup2 = tup[1:4]
print(tup2)    