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
        return None
    return output


# # testing cases
# print( order(8, [(0,2), (1,2), (2,3), (2,4), (3,4), (3,5), (4,5), (5,6), (5,7)]) )
# # should return [0, 1, 2, 3, 4, 5, 6, 7]

# print( order(4, [(0,1), (1,2), (2,1), (2,3)]) )
# # should return None

# print( order(5, [(0,1), (1,2), (2,3), (3,4)]) )
# # should return [0, 1, 2, 3, 4]

# print( order(5, []) )
# # should return [0, 1, 2, 3, 4]  # could be any order

# print( order(3, [(1,2), (2,1)]) )
# # should return None

# print( order(1, [(0,0)]) ) # self loop
# # should return None