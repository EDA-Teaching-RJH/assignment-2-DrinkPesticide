## Write a program that generates 10 random numbers with values between 1-100.
import random as rm
def main():
    ten_numbers = [rm.randint(0, 100) for x in range(0, 10)]
# list comprehension form of for loop
    print(ten_numbers)
    odd_numbers = [x for x in ten_numbers if x%2 != 0]
    print(odd_numbers)
def odd(n_list):
    for index, element in n_list:
        