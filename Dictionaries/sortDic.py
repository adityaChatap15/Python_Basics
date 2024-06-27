my_dict = {
    "Ravi": 20,
    "Abhinav": 16,
    "Ayush": 30,
    "Yash": 15
}

sorted_dict = dict(sorted(my_dict.items(), key=lambda item: item[1], reverse=False))
print(sorted_dict)


# METHOD 1: This will sort the dic on the basis of key by making new dictionary
# The items() method return a list of key-value pairs as tuples by passing this list to the sorted() function we can sort the tuples based on their first element

sort_dict1 = dict(sorted(my_dict.items(), reverse=False))
print(sort_dict1)

myKeys = list(my_dict.keys())
myKeys.sort()

sort_dict2 = {i: my_dict[i] for i in myKeys}

print(sort_dict2)