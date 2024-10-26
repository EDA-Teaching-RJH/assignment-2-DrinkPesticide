numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
def odd(list_in):
    i = 0
    o_list = []
    while i < len(list_in):
        print(list_in[i]%2)
        o_list = o_list + [list_in[i]]
        i = i + 1
    return o_list
print(odd(numbers))
