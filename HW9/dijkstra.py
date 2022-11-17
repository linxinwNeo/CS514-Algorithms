

# testing cases
print( shortest(4, [(0,1,1), (0,2,5), (1,2,1), (2,3,2), (1,3,6)]) )
#should return (4, [0,1,2,3])

print( shortest(5, [(0,1,1), (0,2,5), (1,2,1), (2,3,2), (1,3,6)]) )
#should return None

print( shortest(4, [(0,1,1), (2,3,1)]) )
#should return None