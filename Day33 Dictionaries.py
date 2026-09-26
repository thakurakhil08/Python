# dic = {
#     344: "Akhil",
#     56: "Shubham",
#     678: "Neha",
#     567: "Shahbaz",

# }

# print(dic[678])

info = {'name':'Karan', 'age':19, 'eligible':True}
# print(info)
# # print(info['name'])
# # print(info.get('name'))
# # print(info.keys())
# print(info.values())

# for key in info.keys():
#     # print(info[key])
#     print(f"The value corresponding to the key {key} is {info[key]}")

print(info.items())
for key, value in info.items():
    print(f"The value corresponding to the key {value}")