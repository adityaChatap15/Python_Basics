# f = open('hello.txt', 'w')
# f.write("How you doing ?")
# print(f.read())

f = open('hello.txt', 'a')  # 'a' will append the text in the existing file
f.write("Now i have added the content in the file")
# f.close()  # If we close the file then again we have to open while reading otherwise it will give me an error

f = open("hello.txt", 'r')
print(f.read())

# y = open("newFile", "x")  # using 'x' This create a new file

import  os
os.remove("newFile")