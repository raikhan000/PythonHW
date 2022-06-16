def superposition(funmod, *funseq):
    funres = []
    n = len(funseq[0])
    for i in range(n):
        def func(x, j = i):
            return funmod(funseq[0][j](x))
        funres.append(func)
    return funres
