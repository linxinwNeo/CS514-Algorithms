# Maximum Weighted Independent Set 

import random
import sys

def max_wis( data, array = None ):
    
    data_length = len(data)
    if array == None:
        array = [-1] * (data_length + 1)
    
    # base case
    if data_length == 0: return (0, [])
    elif data_length == 1: 
        return (data[-1], [data[-1]]) if data[-1] > 0 else (0, [])

    d2 = data[:-2]
    if array[ len(d2) ] == -1:
        choose_max, choose_eles = max_wis( d2, array )
        array[ len(d2) ] = (choose_max, choose_eles, len(choose_eles))

    else:
        choose_max, choose_eles, choose_eles_len = array[ len(d2) ]
        choose_eles = choose_eles[:choose_eles_len]

    d1 = data[:-1]
    if array[ len(d1) ] == -1:
        not_choose_max, not_choose_eles = max_wis( d1, array )
        array[ len(d1) ] = (not_choose_max, not_choose_eles, len(not_choose_eles))
    else:
        not_choose_max, not_choose_eles, not_choose_eles_len = array[ len(d1) ]
        not_choose_eles = not_choose_eles[:not_choose_eles_len]

    last_ele = data[-1]
    choose_max += last_ele
    
    if choose_max > not_choose_max:
        choose_eles.append( last_ele )
        array[ len(data) ] = (choose_max, choose_eles)
        return ( choose_max, choose_eles )
    else:
        array[ len(data) ] = (not_choose_max, not_choose_eles)
        return ( not_choose_max, not_choose_eles )