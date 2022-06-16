class Pepelac:
    last = 0

    def __init__(self, line):
        self.sys = []
        self.sub = []
        self.dtl = []
        self.linear = []
        i = self.loops(line)
        if len(self.sys) > 1:
            self.last = 1
            self.fnd = []
            while i < len(line) - 1:
                el = line[i]
                i += 1
                if el == ' ':
                    break
                self.fnd.append(el)
        else:
            self.last = 0
    def __str__(self):
        return f'{self.sys} {self.sub} {self.linear} {self.dtl} {self.last}'


    def loops(self, line):
        line += ' '
        l = len(line)
        i = 0
        while i < l:
            el = line[i]
            i += 1
            if el == ' ':
                break
            self.sys.append(el)
            self.linear.append(el)

        while i < l:
            el = line[i]
            i += 1
            if el == ' ':
                break
            if not el.isupper():
                i -= 1
                break
            self.sub.append(el)

        while i < l - 1:
            if line[i] == ' ':
                i += 1
            if len(self.sys) > 1:
                if line[i + 1] != ' ':
                    break
            el = line[i]
            i += 1
            if el == ' ':
                break
            self.dtl.append(el)
        return i

def helper(p, i, j, s):
    len_pj = len(p[j].linear)
    len_pi = len(p[i].linear)
    f = 0
    if p[-1].sys == ['F', 'J', 'Q', 'R', 'T', 'Z']:
        f = p[j].linear.index(p[i].sub[s])
    prev_ind = -1
    add = 1
    for kk in range(f, len_pj):
        ind = -1
        for k in range(len_pi):
            if p[i].linear[k] == p[j].linear[kk]:
                ind = k
                break
        if ind < 0:
            if s - 1 < 0:
                p[i].linear.append(p[j].linear[kk])
            else:
                ind_prev_sub = p[i].linear.index(p[i].sub[s - 1])
                if kk > f:
                    ind_prev_sub += add
                if prev_ind > -1:
                    ind_prev_sub = prev_ind
                i_p = p[i].linear.index(p[i].sub[s - 1])
                if i_p + 1 < len_pi and p[i].linear[i_p + 1] in p[j].linear:
                    if kk < len_pj - 1 and p[j].linear[kk + 1] in p[i].linear:
                        ind_prev_sub = p[i].linear.index(p[j].linear[kk + 1]) - 1

                p[i].linear.insert(ind_prev_sub + 1, p[j].linear[kk])
                add += 1
            len_pi = len(p[i].linear)

        prev_ind = ind


def findRes(seq, res, last_i, not_last):
    last = seq[last_i].linear[-1]
    for el in seq:
        if last in el.linear:
            if el.linear.index(last) != (len(el.linear) - 1):
                not_last = 1
                break

    if not_last == 0:
        for el in seq:
            if last in el.linear:
                el.linear.pop()

        res.insert(0, last)
    return res


def c3(p, res):
    len_sys = len(p[-1].sys)
    l = len(p) - 1
    seq = []
    for i in range(len_sys):
        for j in range(l):
            if p[j].sys[0] == p[-1].sys[i]:
                seq.append(p[j])

    not_last = 0
    len_seq = len(seq)
    last_i = 0
    while len(seq[0].linear) != 0:
        if not_last == 1:
            last_i += 1
            if last_i >= len_seq:
                return False

        res = findRes(seq, res,last_i, not_last)
    return True

p = []
i = 0
while True:
    a = str(input())
    t = Pepelac(a)
    p.append(t)
    if p[i].last == 1:
        break
    i += 1

seq = []
l1 = len(p) - 1
mro = True
for i in range(l1):
    len_sub = len(p[i].sub)
    s = 0
    while s < len_sub:
        for j in range(i - 1, -1, -1):
            if p[i].sub[s] in p[j].linear:
                helper(p, i, j, s)
                break
        s = s + 1
    l2 = 0
    len_lin = len(p[i].linear)
    for ind in range(1, len_lin):
        if p[i].linear[ind] == p[i].sub[l2]:
            l2 += 1
            if l2 >= len_sub:
                break
    if l2 < len_sub:
        mro =  False
if mro:
    if c3(p, seq):
        l = len(p)
        dtl = p[-1].fnd
        l_dtl = len(dtl)
        res = [0 for i in range(l_dtl)]

        for sys in seq:
            for i in range(l):
                if sys == p[i].sys[0]:
                    for el in p[i].dtl:
                        if el in dtl:
                            j = dtl.index(el)
                            res[j] = 1

        if 0 in res:
            have_dtl =  False

        else:
            have_dtl = True

        if have_dtl:
            print("Correct")
        else:
            print("Incorrect")
else:
    print("Incorrect")
