import random

def sort(data):
    if len(data) == 0:
        return []
    
    rand_pivot_idx = random.randint(0, len(data)-1)
    pivot = data[rand_pivot_idx]

    left = [ x for idx, x in enumerate(data) if idx != rand_pivot_idx and x < pivot ]
    right = [ x for idx, x in enumerate(data) if idx != rand_pivot_idx and x >= pivot ]

    return [sort(left)] + [pivot] + [sort(right)]

def sorted(tree):
    if len(tree) < 3:
        return []

    node = tree[1]
    left = tree[0] # left tree of this node
    right = tree[2] # right tree of this node
    return sorted(left) + [node] + sorted(right)


def _search(tree, x):
    if len(tree) < 3:
        return tree

    node = tree[1]
    left = tree[0] # left tree of this node
    right = tree[2] # right tree of this node

    if x < node:
        return _search(left, x)
    elif x == node:
        return tree
    else:
        return _search(right, x)

def search(tree, x):
    if len(_search(tree, x)) == 0:
        return False
    return True


def insert(tree, x):
    subtree = _search(tree, x)
    if len(subtree) == 0:
        subtree.append([])
        subtree.append(x)
        subtree.append([])
    return
