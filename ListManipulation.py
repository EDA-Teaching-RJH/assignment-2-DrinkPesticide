def main():
    numbers_1 = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
    print(f"{numbers_1} is the initial list")
    numbers_1.sort()
    # sorts the list in ascending order
    print(f"{numbers_1} is the list in ascending order")
    numbers_1 = [x for x in numbers_1 if x != 1]
    # list comprehension format sourced from https://stackoverflow.com/questions/19819907/python-using-del-in-for-loops
    print(f"{numbers_1} is the list when all 1's have been subtracted.")
    # remove number if it is 1
    # Adds numbers 7 and 8 at the end of the list.
    numbers_2 = [7, 8]
    numbers_1 = numbers_1 + numbers_2
    # prints the final list
    print(f"{numbers_1} is the final list, with 6 and then 7 added at the end")
main()