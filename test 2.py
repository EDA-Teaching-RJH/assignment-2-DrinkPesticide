numbers_1 = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
numbers_2 = [7, 8]
zumba = ([x for x in numbers_1 if x != 1].sort) + numbers_2
print(zumba)