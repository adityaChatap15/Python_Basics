# list = ["aditya", "yash", "gaurav", "anuj", "kunal"]
# list.sort()
# print(list)

#  REVERSE SORTING LIST
# list.sort(reverse=True)
# print(list)

#CUSTOMIZE SORT FUNCTION

# ye fun particular n k liya - 20 krke return krenga aur niche uss n-20 k basis pr sorting hongi
def fun(n):
    return abs(n - 20)
list = [10, 40, 25, 21, 42]
list.sort(key=fun, reverse=True)  # reverse=True krenge toh reverse result denga
print(list)

list.reverse() # ye vala reverse kar denga puri string ko
print(list)

