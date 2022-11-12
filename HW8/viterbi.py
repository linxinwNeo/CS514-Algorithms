from heapq import heappush, heapify, heappop
from collections import defaultdict
# bottom up approach
def order( n, data ):
    visited = set()
    in_degrees = defaultdict(list)
    out_degrees = defaultdict(list)
    def is_traversable( nodes ):
        for node in nodes:
            if node not in visited:
                return False
        return True

    # building the graph
    for x, y in data:
        out_degrees[x].append(y)
        in_degrees[y].append(x)

    # putting starting nodes to a queue
    queue = []
    for key in range(n):
        in_degree = in_degrees[key]
        if len(in_degree) == 0: # no indegree
            queue.append( key )
    heapify(queue)

    # building output
    output = []
    while len(queue) != 0:
        cur_node = heappop(queue)
        output.append(cur_node)
        visited.add( cur_node )
        out_degree = out_degrees[cur_node]
        for node in out_degree:
            in_degree = in_degrees[node]
            if is_traversable( in_degree ) == True:
                heappush(queue, node)
    if len(visited) != n: # check if all nodes are visited
        return (0, None)
    return (in_degrees, output)


def longest( n, data ):
    def back_trace(path_end_node_idx):
        ancestor_idx = best_path[path_end_node_idx]
        if ancestor_idx < 0:
            return [path_end_node_idx]
        return back_trace( ancestor_idx ) + [path_end_node_idx]

    (in_degrees, topol_path) = order( n, data )
    if topol_path == None: return (0, [])
    best_values = [0] * n
    best_path = [-1] * n
    for node in topol_path:
        best = 0
        in_degree = in_degrees[node]
        for in_node in in_degree:
            if best < best_values[in_node] + 1:
                best = best_values[in_node] + 1
                best_path[node] = in_node
        best_values[node] = best
    
    best = (-1, 0) # idx, val
    
    for idx, val in enumerate(best_values):
        if best[1] < val:
            best = (idx, val)

    return (best[1], back_trace(best[0]))

# # testing cases
# print( longest(8, [(0,2), (1,2), (2,3), (2,4), (3,4), (3,5), (4,5), (5,6), (5,7)]) )
# # should be (5, [0, 2, 3, 4, 5, 6])

# print( longest(8, [(0,2), (1,2), (2,3), (2,4), (4,3), (3,5), (4,5), (5,6), (5,7)]) )
# # should be (5, [0, 2, 4, 3, 5, 6])

# print( longest(8, [(0,1), (0,2), (1,2), (2,3), (2,4), (4,3), (3,5), (4,5), (5,6), (5,7), (6,7)]) )
# # should be (7, [0, 1, 2, 4, 3, 5, 6, 7])  # unique answer