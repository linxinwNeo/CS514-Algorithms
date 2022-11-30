from heapq import heappush, heapify, heappop

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
    n = len(data)

    record = [ [(0, -1, -1, -1, -1)] * n for _ in range(n) ]
    # record[i][j] meaning the best rna structure of rng segment from i to j
    # record[0][length-1] contains the solution
    # for back trace, we need to save triple at each index: (num, left_idx, right_idx, i, j)

    for size in range( 2, n + 1 ): # size of span
        for i in range( 0, n - size + 1 ): # left index of the span
            bestSoFar = (0, -1, -1, -1, -1)
            j = size + i
            has_pair = False
            for t in range( i, j ):
                pair = is_pair( data[t], data[j-1] )
                if pair:
                    num1, _, _, _, _ = record[i][t-1]
                    num2, _, _, _, _ = record[t+1][j-2]
                    num = num1 + num2 + 1
                    if num > bestSoFar[0]:
                        bestSoFar = (num, t, j-1, i, j)
                        has_pair = True

            if has_pair and bestSoFar[0] > record[i][j-2][0]:
                record[i][j-1] = bestSoFar
            else:
                record[i][j-1] = record[i][j-2]


    def back_trace( solution = None, i = 0, j = n-1 ):
        if solution == None:
            solution = ['.'] * n
        if i < 0 or j >= n: return solution
        v, left, right, ii, jj = record[i][j]
        if v == 0: return solution
        solution[left] = '('
        solution[right] = ')'
        if left-1 >= ii:
            back_trace(solution, ii, left-1)

        back_trace(solution, left+1, right-1)
        if right+1 <= jj:
            back_trace(solution, right+1, jj)

        return solution
    
    return( record[0][n-1][0], ''.join( back_trace() ) )

# num of all possible structures
def total( data ):
    n = len(data)

    record = [ [0] * n for _ in range(n) ]
    # for i in range(n):
    #     for j in range(n):
    #         if j > i:
    #             record[i][j] = 1

    for size in range( 2, n + 1 ): # size of span
        for i in range( 0, n - size + 1 ): # left index of the span
            sum = 1
            j = size + i
            for t in range( i, j ):
                pair = is_pair( data[t], data[j-1] )
                if pair:
                    num1 = record[i][t-1]
                    num2 = record[t+1][j-2]
                    num = num1 + num2 + 1
                    if i == 0 and j-1 == 4 and t == 0:
                        print(i, t-1, t+1, j-2, num)
                    sum += num

            if sum > record[i][j-2]:
                record[i][j-1] = sum
            else:
                record[i][j-1] = record[i][j-2]

    return record[i][n-1]



# k-best structures
def kbest( data, k ):
    n = len(data)
    
    record = [ [ [] ] * n for _ in range(n) ]
    # record[i][j] meaning the best rna structure of rng segment from i to j
    # record[0][length-1] contains the solution
    # for back trace, we need to save triple at each index: (num, best_k)

    for size in range( 2, n + 1 ): # size of span
        for i in range( 0, n - size + 1 ): # left index of the span
            bestSoFar = []
            j = size + i
            has_pair = False
            for t in range( i, j ):
                pair = is_pair( data[t], data[j-1] )
                if pair:
                    best_k1 = record[i][t-1]
                    best_k2 = record[t+1][j-2]
                    best_k, best1, best2 = copy_and_combine_queues(best_k1, best_k2, k)
                    num = best1 + best2 + 1
                    if num > best_rna_among_k(bestSoFar):
                        push_new(best_k, (num, t, j-1, i, j), k)
                        bestSoFar = best_k
                        has_pair = True

            if has_pair and best_rna_among_k(bestSoFar) > best_rna_among_k(record[i][j-2]):
                record[i][j-1] = bestSoFar
            else:
                record[i][j-1] = record[i][j-2]

    for l in record:
        print(l)
    return record[0]

def push_new(q, ele, k):
    heappush(q, ele)
    if len(q) > k:
        heappop(q)
    return q

def copy_and_combine_queues(q1, q2, k):
    q = []
    for ele in q1:
        q.append(ele)
    for ele in q2:
        q.append(ele)

    heapify(q)
    while len(q) > k:
        heappop(q)
    return q, best_rna_among_k(q1), best_rna_among_k(q2)

def best_rna_among_k(q):
    max = 0
    for ele in q:
        if ele[0] > max:
            max = ele[0]
    return max

# test cases
a = "GUAC"
print(kbest(a, 5))
#[(2, '((.))'), (1, '.(.).'), (1, '..(.)'), (1, '...()'), (1, '(...)'), (0, '.....')]
