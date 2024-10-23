def main():
    numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
    print(numbers)
    numbers.sort()
    # sorts the list in ascending order
    print(numbers)
    for i in range(len(numbers)):
        if i == 1:
            del numbers[i]
        elif i != 1:
            continue
    print(numbers)
    # remove number if it is 1
    # Adds numbers 7 and 8 at the end of the list.

    # prints the final list
    print(numbers)
main()