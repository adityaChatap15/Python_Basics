# x = -1
# if x < 0:
#     raise Exception("The number is below zero")



# y = 10
# z = 0
# sum = y/z
# print(sum)



# s = "aditya"
# if not type(s) is int:
    # raise Exception("This datatype is not a type of int")



a = 5
b = 0
try:
    print("resource Open")
    print(a/b)
    k = int(input("Enter a number"))
    print(k)

except ZeroDivisionError as e:
    print("You Cannot divide a Number by Zero", {e})

except ValueError as e:
    print("Invalid Input")

except Exception as e:
    print("Something went Wrong....")

finally:
    print("resource closed")


