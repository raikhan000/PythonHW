import itertools
import random
def randomes(seq):
    seq = [tuple(i) for i in seq]
    d = itertools.cycle(seq)
    while(True):
        item = next(d)
        yield random.randint(*item)
