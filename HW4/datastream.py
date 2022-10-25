from heapq import heapreplace
from heapq import heappop
from heapq import heapify

def ksmallest( k, data ):
    heap = []

    if k > len(data):
        heap = [-x for x in data]
        heapify(heap)
        output = [0] * len(data)
        for i in reversed(range(len(data))):
            output[i] = -heappop(heap)
    else:
        for x in data[0:k]:
            heap.append(-x)
        heapify(heap)

        for x in data[k:]:
            if -heap[0] > x:
                heapreplace(heap, -x)
    
        output = [0] * k
        for i in reversed(range(k)):
            output[i] = -heappop(heap)
    return output
