
# Tuple k anadar koi APPEND methid nhi hoti so ham multiple alag alag tarike use krke add krte hai element ko


# METHOD 1: convert the tuple into list add your item and then convert it back into the tuple:

# myTuple = ("aditya", "abhinav", "ayush")
# print("I am tuple before adding", myTuple)
# myList = list(myTuple)
# print("I am List ", myList)
# myList.append("adheera")
# myTuple = tuple(myList)
# print("I am tuple after adding", myTuple);

# METHOD 2: create a new tuple with items and add it to the existing tuple

myTuple = ("aman", "atharva", "akash")
print("Before adding", myTuple)
newTuple = ("aryan",)
myTuple += newTuple
print("After adding", myTuple)




