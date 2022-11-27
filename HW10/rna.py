# AU, GC, GU or inverse of them
rna_links = [   
                ('A', 'U'),
                ('U', 'A'),
                ('G', 'C'),
                ('C', 'G'),
                ('G', 'U'),
                ('U', 'G') 
            ]


def is_pair(l, r):
    for left_s, right_s in rna_links:
        if l == left_s and r == right_s:
            return True
    return False
        

# 1-best structure
def best( data ):
    length = len(data)

    record = [ [(0, -1, -1)] * length for _ in range(length) ]
    # record[i][j] meaning the best rna structure of rng segment from i to j
    # record[0][length] contains the solution
    # for back trace, we need to save triple at each index: (num, left_pair_idx, right_pair_idx)

    for size in range( 2, length+1 ): # size of span
        for i in range( 0, length - size + 1 ): # left index of the span
            best_record = (0, -1, -1)
            j = size + i - 1 # right index of the span
            for t in range( i, j + 1 ):
                pair = is_pair( data[t], data[j] )
                if not pair:
                    continue
                else:
                    num1 = num2 = 0
                    if t-1 >= 0: 
                        num1, _, _ = record[i][t-1]
                    if t+1 <= length and j-1 >= 0: 
                        num2, _, _ = record[t+1][j-1]
                    cur_val = num1 + num2 + 1
                    if cur_val > best_record[0]:
                        best_record = (cur_val, t, j)

            if best_record == (0, -1, -1):
                record[i][j] = record[i][j-1]
            else:
                record[i][j] = best_record


    def back_trace( solution = None, i = 0, j = length-1 ):
        if solution == None:
            solution = ['.'] * length

        v, left, right = record[i][j]
        if v == 0 or j < 0 or i >= j: return solution

        solution[left] = '('
        solution[right] = ')'
        back_trace( solution, 0, left-1 )
        back_trace( solution, left+1, right-1 )
        return solution

    print( record[0] )
    return( record[0][length-1][0], ''.join( back_trace() ) )


# num of all possible structures
def total( data ):
    length = len(data)

    record = [ [0] * length for _ in range(length) ]
    # record[i][j] meaning the best rna structure of rng segment from i to j
    # record[0][length] contains the solution
    # for back trace, we need to save triple at each index: (num, left_pair_idx, right_pair_idx)

    for size in range( 2, length+1 ): # size of span
        for i in range( 0, length - size + 1 ): # left index of the span
            best_record = 0
            j = size + i - 1 # right index of the span
            for t in range( i, j + 1 ):
                pair = is_pair( data[t], data[j] )
                if not pair:
                    continue
                else:
                    num1 = num2 = 0
                    if t-1 >= 0: 
                        num1 = record[i][t-1]
                    if t+1 <= length and j-1 >= 0: 
                        num2 = record[t+1][j-1]
                    cur_val = num1 + num2 + 1
                    best_record += cur_val

            record[i][j] = best_record

    return( record[0][length-1] )


# k-best structures
def kbest( data ):
    return


#testing cases
#print( best("GCACG") )

#print( best("AGGCAUCAAACCCUGCAUGGGAGCG") )
# (10, '.(()())...((((()()))).())')


print( total("ACAUG") )
# 6
print( total("CCCGGG") )
# 20
print ( total("UUCAGGA") )
# 24
print( total("AUAACCUA") )
# 19
print( total("UUUGGCACUA") )
# 179
print( total("UUGGACUUG") )
# 129
print( total("GAUGCCGUGUAGUCCAAAGACUUC") )
# 2977987
print( total("AGGCAUCAAACCCUGCAUGGGAGCG") )
# 560580