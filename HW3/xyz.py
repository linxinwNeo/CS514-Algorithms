def find( data ):
    s = set(data)
    triples = []
    for idx, x in enumerate(data):
        for y in data[idx+1:]:
            if (x+y) in s:
                triples.append( (x, y, (x+y)) )

    return triples