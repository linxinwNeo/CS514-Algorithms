from math import inf
from heapdict import heapdict
from collections import defaultdict

def shortest( n, edges ):
    def back_trace(idx, path = []):
        if idx == 0: 
            path.append(idx)
            return path
        node_idx = back[idx]
        back_trace(node_idx, path)
        path.append(idx)
        return path

    dist = [inf] * n # init with inf
    queue = heapdict() # touched...grey nodes
    back = [-1] * (n) # back trace
    out_degrees = defaultdict(list)

    # build graph
    for x, y, d in edges:
        out_degrees[x].append( (y, d) )
    
    # put starting node into the queue
    queue[0] = 0

    while len(queue) != 0:
        node_idx, d = queue.popitem()
        if node_idx == n-1:
            return ( d, back_trace(idx=n-1) )
        next_edges = out_degrees[node_idx]
        for next_node_idx, dist in next_edges:
            if next_node_idx in queue: # update dist if necessary
                if queue[next_node_idx] > d + dist:
                    queue[next_node_idx] = d + dist
                    back[next_node_idx] = node_idx
            else: # this is a new node, add to the queue
                queue[next_node_idx] = d + dist
                back[next_node_idx] = node_idx
    

# testing cases
# print( shortest(4, [(0,1,1), (0,2,5), (1,2,1), (2,3,2), (1,3,6)]) )
# #should return (4, [0,1,2,3])

# print( shortest(5, [(0,1,1), (0,2,5), (1,2,1), (2,3,2), (1,3,6)]) )
# #should return None

# print( shortest(4, [(0,1,1), (2,3,1)]) )
# #should return None