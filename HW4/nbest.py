from heapq import heappush
from heapq import heappop
from heapq import heapify
import random

def add(a):
    return a[0] + a[1]


def qsort(data):
    if len(data) == 0:
        return []
    
    rand_pivot_idx = random.randint(0, len(data)-1)
    pivot = data[rand_pivot_idx]

    left = [ x for idx, x in enumerate(data) if add(x) < add(pivot) ]
    same = [ x for idx, x in enumerate(data) if add(x) == add(pivot) ]
    right = [ x for idx, x in enumerate(data) if add(x) > add(pivot) ]

    return qsort(left) + qsort_(same) + qsort(right)


def qsort_(data):
    if len(data) == 0:
        return []
    
    rand_pivot_idx = random.randint(0, len(data)-1)
    pivot = data[rand_pivot_idx]

    left = [ x for idx, x in enumerate(data) if x[1] < pivot[1] ]
    same = [ x for idx, x in enumerate(data) if x[1] == pivot[1] ] # we care order now
    right = [ x for idx, x in enumerate(data) if x[1] > pivot[1] ]

    return qsort_(left) + same + qsort_(right)


def qselect(query, data):
    q_index = query - 1
    if len(data) == 0 or q_index < 0:
        return []
    
    rand_pivot_idx = random.randint(0, len(data)-1)
    pivot = data[rand_pivot_idx]
    left = [ x for idx, x in enumerate(data) if add(x) < add(pivot) ]
    same = [ x for idx, x in enumerate(data) if add(x) == add(pivot) ]
    right = [ x for idx, x in enumerate(data) if add(x) > add(pivot) ]


    if q_index < len(left): # check if hit left
        return qselect(query, left)
    elif len(left) <= q_index < len(left) + len(same): # check if hit pivot
        return qselect_(query - len(left), same)
    else: # check if hit right
        return qselect(query - len(left) - len(same), right) 


def qselect_(query, data):
    q_index = query - 1
    if len(data) == 0 or q_index < 0:
        return []
    
    rand_pivot_idx = random.randint(0, len(data)-1)
    pivot = data[rand_pivot_idx]
    left = [ x for idx, x in enumerate(data) if x[1] < pivot[1] ]
    same = [ x for idx, x in enumerate(data) if x[1] == pivot[1] ] # we don't care order now
    right = [ x for idx, x in enumerate(data) if x[1] > pivot[1] ]
    if q_index < len(left): # check if hit left
        return qselect_(query, left)
    elif len(left) <= q_index < len(left) + len(same): # check if hit pivot
        return same[q_index - len(left)]
    else: # check if hit right
        return qselect_(query - len(left) - len(same), right) 


# (a) enumerate all n^2 pairs, sort, and take top n.
def nbesta( a, b ):
    pairs = []
    for x in a:
        for y in b:
            pairs.append((x, y))
    pairs = qsort( pairs )
    return pairs[:len(a)]


# (b) enumerate all n^2 pairs, but use qselect from hw1.
def nbestb( a, b ):
    pairs = []
    for x in a:
        for y in b:
            pairs.append((x, y))
    list = []

    for i in range(1, len(a)+1):
        list.append(qselect(i, pairs))
    return list


# (c) Dijkstra-style best-first, only enumerate O(n) (at most 2n) pairs.
def nbestc( a, b ):
    return
