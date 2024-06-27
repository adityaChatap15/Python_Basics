import re
txt = "One Way Traffic"

# METHOD 1: search()
x = re.search("One.*Traffic$", txt)
if x:
    print("Yes I have found the Match")
else:
    print("No Match Found")



# METHOD 2: findall()
y = re.findall("[a-s]", txt)
print(y)


