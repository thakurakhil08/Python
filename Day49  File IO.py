# READING A FILE



# f = open('myfile.txt', 'r')
# # f = open('myfile2.txt', 'w')
# # f = open('myfile.txt')
# # print(f)
# text = f.read()
# print(text)
# f.close()


# WRITING A FILE

# f = open('myfile2.txt', 'a')
# f.write("Hello world!")
# f.close()



with open('myfile2.txt', 'a') as f:
    f.write("Hey I am inside with")