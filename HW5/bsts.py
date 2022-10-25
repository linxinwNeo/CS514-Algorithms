# Number of n-node BSTs

def bsts( n, array = None):
    if array == None:
        array = [-1] * (n+1)
        array[0] = 1 # base cases
        array[1] = 1 # base cases
    
    # check if the bsts(n) has been calculated already
    if array[n] != -1: return array[0]
    
    count = 0
    
    for i in range( n ): # i is the root node
        if array[i] != -1:
            left = array[i]
        else:
            left = bsts( i, array )


        if array[n- i -1] != -1:
            right = array[n-i-1]
        else:
            right = bsts( n-i-1, array )
        
        count += left * right


    array[n] = count
    return count
