from bisect import bisect
def find( data, val, k ):
    k_idx = bisect(data, val) # find num-th idx
    ptr_l = k_idx - 1
    ptr_r = k_idx
    count = 0
    closest = []
    while count < k:
        if ptr_l < 0: # we want to take elements from right
            closest.push(data[ptr_r])
            ptr_r += 1
            count += 1
            continue
        if ptr_r >= len(data): # we want to take elements from left
            closest = [data[ptr_l]] + closest
            ptr_l -= 1
            count += 1
            continue

        # compare two value
        a = abs_diff( val, data[ptr_l] )
        b = abs_diff( val, data[ptr_r] )
        if a > b:
            closest.append(data[ptr_r])
            ptr_r += 1
        else:
            closest = [data[ptr_l]] + closest
            ptr_l -= 1
        count += 1

    return closest

def abs_diff(a, b):
    return abs(a-b)
