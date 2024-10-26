## Write a program that generates 10 random numbers with values between 1-100.
import random as rm

def odd(list_in):
    i = 0
    o_list = []
    while i < len(list_in):
        d = (list_in[i]%2)
        print(d)
        if d == 1: 
            o_list = o_list + [list_in[i]]
        i = i + 1
    return o_list

def main():
    ten_numbers = [rm.randint(0, 100) for x in range(0, 10)]
# list comprehension form of for loop
    print(ten_numbers)
    print(odd(ten_numbers))

main()