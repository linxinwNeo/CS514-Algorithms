import math
def longest( data ):
    if data == [] or len(data) == 0: return 0
    return longest_( data )[0]


def longest_( data ):
    # base case
    if data == [] or len(data) == 0 or (data[0] == [] and data[2] == []):
        return [0, 0]

    left_tree = data[0]
    # node = data[1]
    right_tree= data[2]

    [longest1, depth1] = longest_( left_tree )
    [longest2, depth2] = longest_( right_tree )

    longest3 = depth1 + depth2 + 2
    return [max(longest1, longest2, longest3), max(depth1+1, depth2+1)]