# fruits = ["apple", "banana", "kiwi", "cherry", "mango"]
# newList = []
# for x in fruits:
#     if x.__contains__("a"):
#         newList.append(x)
# print(newList)

# COMPREHENSION SYNTAX OF WRITING THE SAME CODE

fruits = ["apple", "banana", "kiwi", "cherry", "mango"]
newlist =  [x for x in fruits if "a" in x]
print(newlist)
