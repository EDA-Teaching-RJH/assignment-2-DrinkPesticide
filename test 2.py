numbers_in = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
def odd(in_list):
    i = 0
    o_list = []
    while i < len(in_list):
        d = (in_list[i]%2)
        if d == 1:
            # current functionality limited by this line
            o_list = o_list + [in_list[i]]
        i = i + 1 
    return o_list
print(odd(numbers_in))