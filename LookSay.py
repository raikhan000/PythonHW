import itertools
def LookSay():
    yield 1
    s = "1"
    g = itertools.groupby(s)
    c = ""
    while True:
        try:
            p = next(g)
            helper1 = len(list(p[1]))
            yield helper1
            yield int(p[0])
            c = c + str(helper1)
            c = c + p[0]
        except StopIteration:
            g = itertools.groupby(c)
            c = ""
