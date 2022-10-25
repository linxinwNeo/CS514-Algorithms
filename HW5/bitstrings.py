# Number of bit strings of length n that has
#   1) no two consecutive 0s.
#   2) two consecutive 0s.

def num_no( n ): # 1)
    # base cases
    if n == 0: return 1
    elif n == 1: return 2
    
    return num_no(n-2) + num_no(n-1)


def num_yes( n ): # 2)
    permutations = pow(2, n)

    return permutations - num_no(n)
