def joinseq(*seq):
    seq = [tuple(i) for i in seq]
    seq.sort()
    while True:
        if len(seq[0]) == 0:
            seq.pop(0)
        if seq == []:
            break
        yield seq[0][0]
        seq[0] = seq[0][1:]
        seq.sort()
