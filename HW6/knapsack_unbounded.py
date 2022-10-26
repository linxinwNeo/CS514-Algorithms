# unbounded knapsack problem

# You have n items, each with weight w_i and value v_i, and each has infinite copies.
# **All numbers are positive integers.**
# the input to the best() function is W and a list of pairs (w_i, v_i).
# this output means to take 0 copies of item 1 and 1 copy of item 2.

# tie-breaking: *reverse* lexicographical: i.e., [1, 0] is better than [0, 1]:
# (i.e., take as many copies from the first item as possible, etc.)

# item = (weight, value)
def best( w, items, records = None ):
    if w <= 0: return (0, [0]*len(items)) # base case
    if records == None: # first call inits the record list
        records = [-1]*(w+1)

    best_items = None
    picked_item_idx = -1
    best_value = 0
    for idx, item in enumerate(items):
        if item[0] > w:
            continue
        if records[w-item[0]] != -1:
            value, picked_items = records[w-item[0]]
            picked_items = picked_items.copy()
        else:
            value, picked_items = best( w-item[0], items, records )
            records[w-item[0]] = (value, picked_items.copy())
        if value + item[1] > best_value:
            picked_item_idx = idx
            best_items = picked_items
            best_value = value + item[1]
            
    if best_items == None: # nothing can fit
        records[w] = (0, [0]*len(items))
        return (0, [0]*len(items))
    else: # we have found an item to be picked
        best_items[picked_item_idx] += 1
        records[w] = ( best_value, best_items.copy() )
        return ( best_value, best_items )
    
# print( best(3, [(2, 4), (3, 5)]) )

# print( best(3, [(1, 5), (1, 5)]) )

# print( best(3, [(1, 2), (1, 5)]) )

# print( best(3, [(1, 2), (2, 5)]) )

# print( best(58, [(5, 9), (9, 18), (6, 12)]) )

# print( best(92, [(8, 9), (9, 10), (10, 12), (5, 6)]) )