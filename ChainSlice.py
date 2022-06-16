import itertools

def chainslice(N, M, *c):
    myList = []
    c = itertools.chain(*c)
    for i in range(M + N):
        try:
            myList.append(next(c))
        except StopIteration:
            break
    return itertools.islice(myList, N, M)
