marks = [3, 5, 7, "Akhil", True, 5, 6, 3, 6, 9, 355, 65, 636]
# print(marks)
# print(type(marks))
# print(marks[0])
# print(marks[1])
# print(marks[2])
# print(marks[3])
# print(marks[4])
# print(marks[5])

# print(marks[-3])  #Negative index
# print(marks[len(marks)-3])  #Positive index
# print(marks[5-3])  #Positive index
# print(marks[2])  #Positive index

# if 6 in marks:
#     print("Yes")
# else:
#     print("No")


#Same things applies for string as well!
# if "Ak" in "Akhil":
#     print("Yes")


# print(marks)
# print(marks[:])
# print(marks[1:])
# print(marks[1:-1])
# print(marks[1:8])
# print(marks[1:8:2])

lst = [i*i for i in range(10)]
print(lst)
lst = [i*i for i in range(10) if i%2==0]
print(lst)