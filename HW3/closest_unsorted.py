import random

def find( data, val, k ):
    diff = [ abs(x-val) for x in data ]
    k_val = qselect( k, diff ) # find num-th value
    
    count = 0
    for i in diff:
        if i < k_val:
            count += 1

    closest_k = []
    num_same = 0
    for idx, x in enumerate(diff):
        if x < k_val:
            closest_k.append(data[idx])
        elif x == k_val and num_same < (k-count):
            closest_k.append(data[idx])
            num_same += 1
    
    return closest_k

def qselect(query, data):
    q_index = query - 1
    if len(data) == 0 or q_index < 0:
        return []
    
    rand_pivot_idx = random.randint(0, len(data)-1)
    pivot = data[rand_pivot_idx]
    left = [x for idx, x in enumerate(data) if x < pivot and idx != rand_pivot_idx]
    right = [x for idx, x in enumerate(data) if x >= pivot and idx != rand_pivot_idx]

    if q_index == len(left): # check if hit pivot
        return pivot
    elif q_index < len(left): # check if hit left
        return qselect(query, left) 
    else: # check if hit right
        return qselect(query - len(left) - 1, right) 