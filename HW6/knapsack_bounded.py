# the back matrix used to recover the items picked in the best solution
# the back matrix is bag_size+1 by len of items + 1
# each element in the matrix is in this format (item_idx, # of copies)
back = None

# item = (weight, value, # of copies)
def best( bag_size, items ):
    global back
    
    for idx, i in enumerate(items):
        weight, value, copies = i
        items[idx] = (weight, value, copies, idx)

    back = [[-1 for _ in range(len(items) + 1)] for _ in range(bag_size+1)] # init matrix with -1

    total_value = knapsack_bounded(bag_size, items) # knapsack_bounded will return the best value out and fill back matrix

    solution = [0] * len(items)
        
    back_trace(bag_size, items, solution) # using back matrix filled during knapsack_bounded recursions to build a solution

    return (total_value, solution) # return in a certain format required in homework description

def knapsack_bounded(bag_size, items):
    len_of_items = len(items)
    if bag_size == 0 or len_of_items == 0: # base cases, if bag is full or no item in the store, the value would be 0
        back[bag_size][len_of_items] = (-1, 0, (0, 0))
        return 0
    
    weight, value, num, item_idx = items[-1] # get current item properties
    new_items = items[:-1]
    best_choice = (0, 0) # (best_value, best_num)
    if back[bag_size][len_of_items] == -1:
        for i in range(num+1):
            total_weight = i*weight
            if bag_size >= total_weight:
                cur_value = value*i + knapsack_bounded( bag_size - total_weight, new_items )
                if cur_value > best_choice[0]:
                    # we found better solution, update best_choice
                    best_choice = (cur_value, i)

        if best_choice == (0, 0): # we dont choose item
            back[bag_size][len_of_items] = (-1, 0, (0, 0))
        else:
            back[bag_size][len_of_items] = (item_idx, weight, best_choice) # ( item_idx, item_weight, best_choice )
    else:
        best_choice = back[bag_size][len_of_items][2]
        
    return best_choice[0]


# function used to back trace the items given a back matrix
def back_trace( bag_size, items, solution ):
    length = len(items)
    # back trace always starts at the bottom-right corner of the matrix, in this case, matrix[bag_size][len(items)
    idx, weight, (_, best_num) = back[bag_size][length]
    if idx >= 0:
        solution[idx] += best_num
        back_trace( bag_size - weight * best_num, items[:-1], solution )
    return
        

#testing cases
if __name__ == "__main__":
    print( best(3, [(2, 4, 2), (3, 5, 3)]) )
    # expected to get: (5, [0, 1])

    print( best(3, [(1, 5, 2), (1, 5, 3)]) )
    # expected to get: (15, [2, 1])

    print( best(3, [(1, 5, 1), (1, 5, 3)]) )
    # expected to get: (15, [1, 2])

    print( best(20, [(1, 10, 6), (3, 15, 4), (2, 10, 3)]) )
    # expected to get: (130, [6, 4, 1])

    print( best(92, [(1, 6, 6), (6, 15, 7), (8, 9, 8), (2, 4, 7), (2, 20, 2)]) )
    # expected to get: (236, [6, 7, 3, 7, 2])