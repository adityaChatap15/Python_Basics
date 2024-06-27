nums = [7, 8, 9, 5]

it = iter(nums)

# METHOD 1: TO PRINT THE LIST ELEMENTS BY ITERATING
print(it.__next__());
print(it.__next__());

# METHOD 2: PRINT THE LIST ELEMENTS BY ITERATING
print(next(it))
print(next(it))

# METHOD 3: BY ITERATING THROUGH LOOP

for i in nums:
    print(i)