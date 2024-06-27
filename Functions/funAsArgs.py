# def upperText(text):
#     return text.upper()
# def lowerText(text):
#     return text.lower()
#
# def greet(func):
#     greeting = func("Hey there Aditya this side")
#     print(greeting)
# greet(upperText)
# greet(lowerText)



def create_adder(x):
    def adder(y):
        return x+y
    return adder
add = create_adder(10)
print(add(10))




