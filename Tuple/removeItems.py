# Remove the duplicate element from tuple

myTuple = ("aditya", "ayush", "abhinav", "aditya")
print("Before", myTuple)
newList = list(myTuple)
cnt = myTuple.count("aditya")
while cnt > 0:
    newList.remove("aditya")
    cnt = cnt-1
myTuple = tuple(newList)
print("After", myTuple)



