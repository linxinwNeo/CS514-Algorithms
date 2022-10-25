import random
def qselect(query, data):
    q_index = query - 1
    if len(data) == 0 or q_index < 0:
        return []
    
    rand_pivot_idx = random.randint(0, len(data)-1)
    pivot = data[rand_pivot_idx]
    left = [x for idx, x in enumerate(data) if x < pivot and idx != rand_pivot_idx]
    right = [x for idx, x in enumerate(data) if x >= pivot and idx != rand_pivot_idx]

    #print( left, ' ', pivot, ' ', right)
    if q_index == len(left): # check if hit pivot
        return pivot
    elif q_index < len(left): # check if hit left
        return qselect(query, left) 
    else: # check if hit right
        return qselect(query - len(left)-1, right) 