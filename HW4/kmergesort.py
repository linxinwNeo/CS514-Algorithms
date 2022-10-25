from heapq import heappush
from heapq import heappop
from heapq import heapify
import math

def kmergesort(data, k):
    if len(data) == 0 or k <= 1:
        return
    
    if(len(data) == 1): return data

    interval = math.floor(len(data)/k)
    sections = [] # holds k sections for this recursion
    for i in range(k):
        lower_bound = interval*i
        upper_bound = interval*i + interval
        if interval == 0:
            if i < len(data):
                sections.append( [data[i]] )
                continue
        else:
            print(sections)
            if i == k-1:
                sections.append( kmergesort( data[lower_bound:], k ) )
                continue
            sections.append( kmergesort( data[lower_bound:upper_bound], k ) )

    # combine
    output = []
    heap = []
    for i in range(len(sections)):
        if len(sections[i]) == 0:
            continue
        heap.append((sections[i][0], i, 0))
    
    heapify(heap)
    while len(heap) != 0:
        item = heappop(heap)
        output.append(item[0])
        if item[2]+1 < len(sections[item[1]]):
            heappush(heap, (sections[item[1]][item[2]+1], item[1], item[2]+1) )

    return output

print( kmergesort([4,1,5,2,6,3,7,0], 3) )