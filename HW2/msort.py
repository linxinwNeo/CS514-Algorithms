import math
def mergesort( data ):
    length = len(data)

    if length == 0 or length == 1: return data

    mid_idx = math.floor( length/2 )

    return merge( mergesort(data[:mid_idx]), mergesort(data[mid_idx:]) )

def merge(d1, d2):
    if len(d1) == 0 : return d2
    if len(d2) == 0 : return d1

    idx1 = 0
    idx2 = 0
    len1 = len(d1)
    len2 = len(d2)
    new_d = []
    while(idx1 != len1 and idx2 != len2):
        if d1[idx1] < d2[idx2]:
            new_d.append(d1[idx1])
            idx1+=1
        else:
            new_d.append(d2[idx2])
            idx2+=1

    if idx1 < len1 :
        new_d += d1[idx1:]
    else:
        new_d += d2[idx2:]

    return  new_d