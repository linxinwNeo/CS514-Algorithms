from math import inf
from collections import defaultdict

def shortest( n, edges ):
    dist = [inf] * n # init with inf
    visited = set()
    graph = defaultdict(list)
    
    for x, y, w in edges:
        graph[x].append( (y,w) )
        graph[y].append( (x,w) )

    

    return output

# testing cases
print( shortest(4, [(0,1,1), (0,2,5), (1,2,1), (2,3,2), (1,3,6)]) )
#should return (4, [0,1,2,3])

#print( shortest(5, [(0,1,1), (0,2,5), (1,2,1), (2,3,2), (1,3,6)]) )
#should return None

#print( shortest(4, [(0,1,1), (2,3,1)]) )
#should return None