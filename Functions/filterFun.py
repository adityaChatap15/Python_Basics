def fun(variable):
    vowels = ['a', 'e', 'i', 'o', 'u']
    if variable in vowels:
        return True
    else:
        return False

sequence = ['a', 'c', 'r', 'b', 'g', 'i', 'm', 'o']
filtered = filter(fun, sequence)
for i in filtered:
    print(i)


def evenFun(var):
    if var % 2 == 0:
        return True
    else:
        return False

list1 = [1, 4, 5, 7, 8, 6, 25, 10]

evenFiltered = filter(evenFun, list1)
for x in evenFiltered:
    print(x)




